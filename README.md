# Flask API Project

A simple Flask-based API that returns a JSON response containing:
- Registered email address
- Current UTC datetime in ISO 8601 format
- GitHub repository URL

## Features
- Handles CORS (Cross-Origin Resource Sharing) for cross-domain requests.
- Dynamically generates UTC datetime.
- Deployed to a publicly accessible endpoint (Render).

## Setup (Local Development)

### Prerequisites
- Python 3.7+
- `pip` (Python package manager)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Igboke/api-project.git
   cd api-project
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # macOS/Linux:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run the flask App:**
   **Set environment variables:**
   ```bash
   export FLASK_APP=app.py  # macOS/Linux
   set FLASK_APP=app.py     # Windows (Command Prompt)
   $env:FLASK_APP = "app.py" # Windows (PowerShell)
   
   flask run --port=5000
   ```
8. **Test the API:**
   ```bash
   curl http://localhost:5000
   ```


## API Documentation

### Base URL
`GET https://api-project-3dlb.onrender.com`

### Endpoint
- **Method**: `GET`
- **Path**: `/`
- **Description**: Returns a JSON object with email, UTC datetime, and GitHub URL.

### Request Example
```bash
curl https://api-project-3dlb.onrender.com
```
### Response Format (200 OK)
```json
{
  "email": "danieligboke669@gmail.com",
  "current_datetime": "2024-02-15T12:34:56Z",
  "github_url": "https://github.com/Igboke/api-project"
}
``` 

### Backlink
[Hire Python Developers at HNG](https://hng.tech/hire/python-developers)

