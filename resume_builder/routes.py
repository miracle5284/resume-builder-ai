import os

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from .schemas import Query
from .resume import ResumeCrew
from .crews.tools import (
    search_tool, scrape_tool,
    get_reader_tool, get_semantic_search_tool
)
from resume_builder.settings import TEMP_DIR, DOWNLOADS_DIR


# Initialize the router for the resume builder API
router = APIRouter(
    prefix="/resume_builder",
    tags=["Resume Builder"],
)

@router.post("/")
async def job_application(query: Query = Depends(Query.as_form)):
    """
    Handles job applications by processing uploaded resumes.
    Extracts and processes the resume file, and performs tasks like
    job research, profiling, resume strategy, and interview preparation.

    Args:
        query (Query): Input query containing job posting URL, GitHub URL, 
        personal writeup, and uploaded resume file.

    Returns:
        dict: Processed results and file download links.
    """
    resume_file = query.pop('resume_file')
    tmp_file_path = str(TEMP_DIR / resume_file.filename)

    with open(tmp_file_path, "wb+") as tmp_file:
        tmp_file.write(await resume_file.read())

    reader_tool = get_reader_tool(tmp_file_path)
    semantic_search_tool = get_semantic_search_tool(tmp_file_path)
    tools = [scrape_tool, search_tool, reader_tool, semantic_search_tool]

    resume_crew = ResumeCrew(
        agents={
            agent: {
                "tools": agent != "tech_job_researcher_agent" and tools or tools[:2]
            } for agent in ["tech_job_researcher_agent", 'profiler', "resume_strategist", "interview_preparer"]
        },
        tasks={
            "research_task": {"agent": "{{tech_job_researcher_agent}}"},
            "profile_task": {"agent": "{{profiler}}"},
            "resume_strategy_task": {
                "agent": "{{resume_strategist}}",
                "context": ["{{research_task}}", "{{profile_task}}"],
                "output_file": str(DOWNLOADS_DIR / "generated_resume.md")
            },
            "interview_preparation_task": {
                "agent": "{{interview_preparer}}",
                "context": ["{{research_task}}", "{{profile_task}}", '{{resume_strategy_task}}'],
                "output_file": str(DOWNLOADS_DIR / "generated_interview_prep.md")
            }
        },
    )

    result = resume_crew.crew.kickoff(inputs={'placeholder': query})
    os.remove(tmp_file_path)

    return {
        'data': result,
        "files": {
            "resume.md": f"/{router.prefix}/download/generated_resume.md",
            "interview.md": f"/{router.prefix}/download/generated_interview_prep.md"
        }
    }

@router.get('/download/{filename}')
async def download_file(filename: str):
    """
    Endpoint to serve files for download.

    Args:
        filename (str): Name of the file to download.

    Returns:
        FileResponse: File response for downloading the specified file.
    """
    return FileResponse(
        str(DOWNLOADS_DIR / filename),
        media_type='application/octet-stream',
        filename=filename
    )