# Resume Builder API

## Overview
Resume Builder API is a FastAPI-based application designed to simplify the job application process. It leverages specialized agents to analyze job postings, refine resumes, and prepare interview materials. The application aims to help job seekers present their best selves by tailoring their profiles to meet specific job requirements.

## Features
- **Job Posting Analysis**: Extract key skills and qualifications from job postings.
- **Personal Profile Refinement**: Generate detailed profiles using GitHub links and personal write-ups.
- **Resume Tailoring**: Customize resumes to highlight relevant skills and experiences.
- **Interview Preparation**: Generate potential questions and talking points based on resumes and job descriptions.
- **Modular Design**: Easily extend or customize agents and tasks.

## Technologies Used
- **FastAPI**: For building the API.
- **Pydantic**: For data validation and modeling.
- **Python**: Core programming language.
- **CrewAI**: To manage agents and tasks.
- **Pathlib**: For robust file and directory handling.

## Project Structure
```
project/
├── routes.py       # API endpoints
├── schemas.py      # Data models and validation
├── server.py       # Application entry point
├── settings.py     # Configuration and paths
├── param_config.py # Agents and tasks configuration
├── resume.py       # Core logic for processing tasks
├── assets/         # Temporary and export directories
└── crews/          # Utility tools and agents
```

## How It Works
1. **Job Posting Input**: The user provides a job posting URL, GitHub URL, personal write-up, and resume file.
2. **Processing**: Agents analyze the job posting, refine the profile, and tailor the resume to match the job requirements.
3. **Output**: The API generates a tailored resume and interview preparation materials for download.

## Getting Started

### Prerequisites
- Python 3.8 or higher

### Setup
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn server:app --reload
   ```

### Usage
- Access the API documentation at `http://127.0.0.1:8000/docs` after running the server.
- Use the `/resume_builder/` endpoint to submit job applications.
- Download generated files using the `/resume_builder/download/{filename}` endpoint.

## Future Improvements
- Add a comprehensive test suite using `pytest`.
- Enhance agent capabilities with AI-driven insights.
- Support additional output formats like PDF.
- Improve error handling and input validation.

## License
This project is licensed under the MIT License.

---

Feel free to contribute by submitting issues or pull requests. Your feedback is highly appreciated!
