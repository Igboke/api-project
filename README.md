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
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # macOS/Linux:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
6. **Run the flask App:**
   **Set environment variables:**
   ```bash
   export FLASK_APP=app.py  # macOS/Linux
   set FLASK_APP=app.py     # Windows (Command Prompt)
   $env:FLASK_APP = "app.py" # Windows (PowerShell)
   
   flask run --port=5000
8. **Test the API:**
   ```bash
   curl http://localhost:5000
