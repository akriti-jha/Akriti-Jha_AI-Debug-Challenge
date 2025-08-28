```markdown
# Financial Document Analyzer - Debug Assignment

## Project Overview
This project is an AI-powered Financial Document Analyzer designed to process corporate reports, financial statements, and investment documents. Leveraging CrewAI agents, it provides comprehensive investment recommendations, risk assessments, and market insights. The system supports uploading PDF financial documents for automated analysis using advanced AI agents, orchestrated through a scalable backend.

---

## Bugs Found and Fixes

Throughout the codebase, *deterministic bugs* and *inefficient prompts* were identified and fixed to make the system functional and reliable:

- **Agent Initialization and LLM Setup**:  
  - Bug: The language model (`llm`) was uninitialized (`llm = llm`), resulting in runtime errors.  
  - Fix: Proper initialization or import of the LLM instance was required before agent creation.

- **Agent Configuration Errors**:  
  - Bug: Incorrect use of parameters such as `tool` instead of `tools` in `Agent` instantiation.  
  - Fix: Changed `tool` to `tools` (list) for compatibility and correct functioning.

- **Unprofessional & Contradictory Prompts**:  
  - Bug: Agents and tasks had misleading or confusing prompt/backstory texts causing unpredictable AI output.  
  - Fix: Rewrote prompts to be clear, professional, and focused on genuine financial analysis.

- **PDF Reading Implementation**:  
  - Bug: The `tools.py` PDF reader used an undefined `Pdf` class without proper import or implementation.  
  - Fix: Replaced with a functional PDF reading method using the `PyPDF2` library, carefully extracting and cleaning text.

- **API Handling Bugs**:  
  - Bug: In `main.py`, the API upload function had missing exception handling, incorrect async file handling, and misconfigured Crew kickoff parameters.  
  - Fix: Added proper error catching, file directory checks, and corrected synchronous/asynchronous handling. Confirmed Crew API calls correctly use passed parameters.

- **Concurrency and Storage**:  
  - Added a **Celery + Redis** queue worker system for scalable asynchronous processing of financial analysis tasks.  
  - Integrated a **PostgreSQL database with SQLAlchemy and async libraries** to persist uploaded document metadata and analysis results.

- **Miscellaneous**:  
  - Added file cleanup on all exit paths to avoid clutter and potential data leaks.  
  - Refined API responses to improve client usability and error transparency.

---

## Setup and Usage Instructions

### Prerequisites  
- Python 3.9 or higher  
- Redis server running locally or accessible remotely  
- PostgreSQL server running locally or accessible remotely  

### Clone the Repository  
```
git clone <your-repo-url>
cd <your-repo-directory>
```

### Install Dependencies  
```
pip install -r requirements.txt
pip install celery[redis] redis uvicorn fastapi sqlalchemy databases asyncpg
```

### Environment Setup  
- Create a `.env` file or set environment variables to configure:  
  - `DATABASE_URL` - PostgreSQL connection string, e.g., `postgresql://user:password@localhost/dbname`  
  - Any LLM API keys/configurations expected by the loaded LLM  

### Database Initialization  
Create database tables before running the app, for example:  
```
# Run as script or via a migration tool
from database import Base, engine

Base.metadata.create_all(bind=engine)
```

### Running the System  

#### Step 1: Start Redis Server  
Make sure Redis is running on `localhost:6379` or configured broker URL.

#### Step 2: Start Celery Worker  
```
celery -A worker_tasks.celery_app worker --loglevel=info --concurrency=4
```

#### Step 3: Run FastAPI Application  
```
uvicorn main:app --reload
```

---

## API Documentation

### 1. Health Check  
- **Method**: `GET`  
- **Endpoint**: `/`  
- **Response**:  
```
{
  "message": "Financial Document Analyzer API is running"
}
```

### 2. Analyze Document  
- **Method**: `POST`  
- **Endpoint**: `/analyze`  
- **Description**: Accepts PDF file and optional query string input.  
- **Request Form Data**:  
  - `file`: Binary PDF file upload  
  - `query`: String (optional) query or instruction  
- **Response**:  
```
{
  "task_id": "unique-task-id-string"
}
```

### 3. Task Status  
- **Method**: `GET`  
- **Endpoint**: `/status/{task_id}`  
- **Description**: Check the processing status and result of an analysis task.  
- **Responses**:  
  - Pending/Started:  
    ```
    {"status": "Pending"}
    ```  
  - Completed:  
    ```
    {
      "status": "Completed",
      "result": "Full financial analysis results as text"
    }
    ```  
  - Failed:  
    ```
    {
      "status": "Failed",
      "error": "Error description"
    }
    ```

---

## Example Usage

**Upload and Analyze PDF:**  
```
curl -X POST "http://localhost:8000/analyze" -F "file=@data/sample.pdf" -F "query=Analyze Q2 2025 financials"
```
Response:  
```
{"task_id": "c8aefe70-1abd-4a8c-a8af-d5c01abc1234"}
```

**Poll Task Status:**  
```
curl "http://localhost:8000/status/c8aefe70-1abd-4a8c-a8af-d5c01abc1234"
```
Response when complete:  
```
{
  "status": "Completed",
  "result": "Tesla Q2 2025 report analysis: Revenue up 20%, recommend moderate investment..."
}
```

---

## Bonus Features Implemented

- Asynchronous task handling and concurrency enabled via **Celery + Redis** queue worker model.  
- Persistent storage of uploaded files and analysis results using **PostgreSQL** with async ORM.  
- API design supports scalability and client-friendly polling of long-running tasks.

---

## Notes

- Replace all placeholder LLM initialization with your actual language model API or library.  
- Ensure Redis and PostgreSQL configurations are secure and adapted to your production environment if applicable.  
- The AI-generated advice is fictional and for demonstration purposes only; real investments require qualified human advice.

---

**Happy Debugging and Best of Luck with the Internship!**

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26063764/3e9cf8c3-93fd-4d19-b444-0d19f073b7a6/AI-Internship-Assignment-Debug-Challenge.pdf)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26063764/23e8ad2f-2e56-4bb5-89e0-af1c57c85f6c/agents.py)
[3](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26063764/30aa7d77-7193-4e3e-a993-365814b438cd/main.py)
[4](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26063764/5369e960-214f-4da1-8d51-2604a3eefd91/README.md)
[5](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26063764/39bbb433-ed64-49fd-9c6c-401dc1f44f9f/requirements.txt)
[6](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26063764/2fbea6fa-913c-4597-89f5-dc21d1af2b53/task.py)
[7](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26063764/881de08c-e514-4525-aa8a-7a03ed32c314/tools.py)
