@echo off
REM Windows Batch Setup Script for Vertex AI Agent Builder
REM This script sets up a Python virtual environment and installs dependencies

echo ========================================
echo Vertex AI Agent Builder - Windows Setup
echo ========================================
echo.

REM Check Python installation
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.8+ from https://www.python.org/downloads/
    pause
    exit /b 1
)
python --version
echo [OK] Python found
echo.

REM Create virtual environment
echo Creating virtual environment...
if exist venv (
    echo [WARNING] Virtual environment 'venv' already exists. Skipping creation.
) else (
    python -m venv venv
    echo [OK] Virtual environment created
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
echo [OK] pip upgraded
echo.

REM Install dependencies
echo Installing dependencies...
if exist requirements.txt (
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install dependencies
        pause
        exit /b 1
    )
    echo [OK] Dependencies installed successfully
) else (
    echo [WARNING] requirements.txt not found
)
echo.

REM Check for .env file
echo Checking environment configuration...
if exist .env (
    echo [OK] .env file found
) else (
    echo [WARNING] .env file not found. Creating from template...
    if exist env.example.txt (
        copy env.example.txt .env >nul
        echo [OK] .env file created from template
        echo [WARNING] Please edit .env file with your GCP project details
    ) else (
        echo [WARNING] env.example.txt not found. Please create .env manually.
    )
)
echo.

REM Check gcloud CLI
echo Checking gcloud CLI...
gcloud --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] gcloud CLI not found. Install from: https://cloud.google.com/sdk/docs/install
) else (
    echo [OK] gcloud CLI found
)
echo.

echo ========================================
echo [SUCCESS] Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 2. Set your GCP project ID:
echo    set GOOGLE_CLOUD_PROJECT=your-project-id
echo    set GOOGLE_CLOUD_LOCATION=us-central1
echo.
echo 3. Authenticate with GCP:
echo    gcloud auth application-default login
echo.
echo 4. Run the local agent:
echo    python week-01-gemini-fundamentals\demos\hello_world_agent_local.py
echo.
pause

