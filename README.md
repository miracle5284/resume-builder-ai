# Resume Builder AI

## Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Technologies Used](#technologies-used)
4. [High-Level Workflow](#high-level-workflow)
5. [Project Structure](#project-structure)
6. [Installation and Setup](#installation-and-setup)
   - [Prerequisites](#prerequisites)
   - [Local Setup](#local-setup)
   - [Dockerized Setup](#dockerized-setup)
7. [Deployment](#deployment)
8. [Usage](#usage)
9. [License](#license)

## Overview
Resume Builder AI is a cutting-edge application that leverages Generative AI (GenAI), Large Language Models (LLMs), and Multi-Agent Systems to craft tailored, professional resumes. By harnessing these advanced technologies, the project aims to automate and optimize the resume creation process, ensuring alignment with industry standards and individual preferences.

## Key Features
- **Job Posting Analysis**: Extracts key skills and qualifications from job postings to align resumes with job requirements.
- **Personal Profile Refinement**: Generates detailed professional profiles using GitHub links, personal write-ups, and other sources.
- **Resume Tailoring**: Customizes resumes to highlight relevant skills and experiences for specific roles.
- **Interview Preparation**: Generates potential interview questions and talking points based on resumes and job descriptions.
- **Modular Design**: Features a multi-agent architecture for easy extension and customization of agents and tasks.
- **Secure Deployment**: Utilizes Docker Swarm to securely manage secrets and configurations.

## Technologies Used
- **Programming Language**: Python 3.10+
- **Framework**: FastAPI
- **AI Models**: ChatGPT, Large Language Models (LLMs) for natural language processing
- **Multi-Agent System**: CrewAI for task collaboration
- **Validation**: Pydantic for data validation
- **Scripting**: Bash for automation scripts
- **Containerization**: Docker and Docker Compose
- **Orchestration**: Docker Swarm for scalable and secure deployment
- **Version Control**: Git

## High-Level Workflow
1. **User Input**: Users provide their details and desired job roles via the application interface.
2. **Data Processing**: Multi-agents validate and preprocess the input.
3. **Resume Generation**: LLMs generate personalized resumes based on the input.
4. **Output Delivery**: The generated resume is formatted and delivered to the user for download.

## Project Structure
```
.
├── resume_builder/             # Core application logic
│   ├── __init__.py             # Package initialization
│   ├── param_config.py         # Parameter configuration logic
│   ├── resume.py               # Main resume builder logic
│   ├── routes.py               # API routes
│   ├── schemas.py              # Validation schemas
│   ├── server.py               # Application entry point
│   ├── settings.py             # App configurations
│   ├── crews/                  # Helper modules and tools
│       ├── agents.py           # Agent-related utilities
│       ├── tools.py            # General utility functions
├── docker-compose.yml          # Compose configuration for services
├── docker-compose.secrets.yml  # Compose configuration for secrets
├── config.env                  # Configuration file for environment variables
├── deploy.sh                   # Deployment script
├── load-docker-env.sh          # Docker environment setup script
├── install.sh                  # Installation script
├── LICENSE                     # License details
├── README.md                   # Documentation
├── .dockerignore               # Exclusions for Docker context
├── .gitignore                  # Exclusions for git context
├── .gitattributes              # Force LF for shell scripts in the project
├── requirements.txt            # Python dependencies
```

## Installation and Setup

### Prerequisites
- Python 3.10 or later
- Docker and Docker Compose
- Docker Swarm (for deployment)
- Git

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/miracle5284/resume-builder-ai
   cd resume-builder-ai
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the application locally:
   ```bash
   uvicorn resume_builder.server:app --host 0.0.0.0 --port 8000
   ```

### Dockerized Setup
1. Build and run the Docker image:
   ```bash
   docker-compose --env-file /path/to/your/env/file up --build
   ```
2. Access the application at `http://localhost:8000`.

## Deployment
The deployment process uses Docker Swarm for secure management of secrets and scalable deployment.

1. Ensure that your `config.env` file is correctly configured with the necessary environment variables.
2. Deploy the stack using the `deploy.sh` script:
   ```bash
   ./deploy.sh
   ```
   This script configures Docker secrets as specified in `config.env` and deploys the stack using Docker Stack.

3. Verify the deployment:
   ```bash
   docker ps
   ```

## Usage
The application provides an API endpoint for building resumes. Users can submit a job posting URL, GitHub profile URL, personal write-up, and an existing resume file. Below is an example of how to use the API:

1. Submit a POST request to the endpoint:
   ```http
   POST http://127.0.0.1:8000/resume_builder/
   ```
   Example payloads:
   
   **Form Data:**
   ```plaintext
   job_posting_url=https://example.com/job-posting
   github_url=https://github.com/example
   personal_writeup=Experienced Backend Engineer with expertise in Python and AI
   resume_file=(file attachment: /path/to/resume.pdf)
   ```

   **JSON Data:**
   ```json
   {
       "job_posting_url": "https://example.com/job-posting",
       "github_url": "https://github.com/example",
       "personal_writeup": "Experienced Backend Engineer with expertise in Python and AI",
       "resume_file": "data:application/pdf;base64,...base64-encoded-pdf-content..."
   }
   ```

2. Example Request:
   ```bash
   curl --location 'http://127.0.0.1:8000/resume_builder/' \
   --form 'job_posting_url="https://example.com/job-posting"' \
   --form 'github_url="https://github.com/example"' \
   --form 'personal_writeup="Experienced Backend Engineer with expertise in Python and AI"' \
   --form 'resume_file=@"/path/to/resume.pdf"'
   ```

3. Example Response:
   ```json
   {
       "data": {
           "raw": "### Tailored Resume for Candidate...",
           "interview_questions": [
               "What are your core competencies in Python and Django?",
               "Can you discuss a time you led a team for a high-impact project?"
           ],
           "talking_points": [
               "Highlight leadership in developing scalable backend systems.",
               "Discuss AI/ML integration into IoT platforms for efficiency improvements."
           ],
           "download_links": {
               "resume": "//resume_builder/download/generated_resume.md",
               "interview_prep": "//resume_builder/download/generated_interview_prep.md"
           }
       },
       "status": "success"
   }
   ```

## Future Improvements
- Add a comprehensive test suite using `pytest`.
- Enhance agent capabilities with AI-driven insights.
- Support additional output formats like PDF.
- Improve error handling and input validation.


## License
This project is licensed under the terms outlined in the `LICENSE` file.

