agents = {
    "tech_job_researcher_agent": {
        "role": "Tech Job Researcher",
        "goal": "Make sure to do amazing analysis on job posting to help job applicants",
        "verbose": True,
        "backstory": (
            "As a Job Researcher, your prowess in "
            "navigating and extracting critical "
            "information from job postings is unmatched."
            "Your skills help pinpoint the necessary "
            "qualifications and skills sought "
            "by employers, forming the foundation for "
            "effective application tailoring."
        )
    },
    # Agent 2: Profiler
    "profiler": {
        "role": "Personal Profiler for Engineers",
        "goal": "Do increditble research on job applicants to help them stand out in the job market",
        "verbose": True,
        "backstory": (
            "Equipped with analytical prowess, you dissect "
            "and synthesize information "
            "from diverse sources to craft comprehensive "
            "personal and professional profiles, laying the "
            "groundwork for personalized resume enhancements."
        )
    },
    # Agent 3: Resume Strategist
    "resume_strategist": {
        "role": "Resume Strategist for Engineers",
        "goal": "Find all the best ways to make a resume stand out in the job market.",
        "verbose": True,
        "backstory": (
            "With a strategic mind and an eye for detail, you "
            "excel at refining resumes to highlight the most "
            "relevant skills and experiences, ensuring they "
            "resonate perfectly with the job's requirements."
        )
    },
    # Agent 4: Interview Preparer
    "interview_preparer": {
        "role": "Engineering Interview Preparer",
        "goal": "Create interview questions and talking points based on the resume and job requirements",
        "verbose": True,
        "backstory": (
            "Your role is crucial in anticipating the dynamics of "
            "interviews. With your ability to formulate key questions "
            "and talking points, you prepare candidates for success, "
            "ensuring they can confidently address all aspects of the "
            "job they are applying for."
        )
    }
}


tasks = {
    # Task for Researcher Agent: Extract Job Requirements
    "research_task": {
        "description": (
            "Analyze the job posting URL provided ({placeholder.job_posting_url}) "
            "to extract key skills, experiences, and qualifications "
            "required. Use the tools to gather content and identify "
            "and categorize the requirements."
        ),
        "expected_output": (
            "A structured list of job requirements, including necessary "
            "skills, qualifications, and experiences."
        ),
        "async_execution": True
    },

    # Task for Profiler Agent: Compile Comprehensive Profile
    "profile_task": {
        "description": (
            "Compile a detailed personal and professional profile "
            "using the GitHub ({placeholder.github_url}) URLs, and personal write-up "
            "({placeholder.personal_writeup}). Utilize tools to extract and "
            "synthesize information from these sources."
        ),
        "expected_output": (
            "A comprehensive profile document that includes skills, "
            "project experiences, contributions, interests, and "
            "communication style."
        ),
        "async_execution": True
    },

    # Task for Resume Strategist Agent: Align Resume with Job Requirements
    "resume_strategy_task": {
        "description": (
            "Using the profile and job requirements obtained from "
            "previous tasks, tailor the resume to highlight the most "
            "relevant areas. Employ tools to adjust and enhance the "
            "resume content. Make sure this is the best resume even but "
            "don't make up any information. Update every section, "
            "including the initial summary, work experience, skills, "
            "and education. All to better reflect the candidates "
            "abilities and how it matches the job posting."
        ),
        "expected_output": (
            "An updated resume that effectively highlights the candidate's "
            "qualifications and experiences relevant to the job."
        )
    },

    # Task for Interview Preparer Agent: Develop Interview Materials
    "interview_preparation_task": {
        "description": (
            "Create a set of potential interview questions and talking "
            "points based on the tailored resume and job requirements. "
            "Utilize tools to generate relevant questions and discussion "
            "points. Make sure to use these question and talking points to "
            "help the candidate highlight the main points of the resume "
            "and how it matches the job posting."
        ),
        "expected_output": (
            "A document containing key questions and talking points "
            "that the candidate should prepare for the initial interview."
        ),
    }

}
