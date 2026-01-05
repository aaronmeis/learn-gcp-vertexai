@echo off
REM Quick launcher for Hello World Agents
REM This batch file activates the virtual environment and runs the agent

echo ========================================
echo Hello World Agents - Quick Launcher
echo ========================================
echo.

REM Get the directory where this batch file is located
set "DEMOS_DIR=%~dp0"
REM Navigate to project root (go up two levels from demos folder: demos -> week-01-gemini-fundamentals -> project root)
cd /d "%DEMOS_DIR%..\..\"
set "PROJECT_ROOT=%CD%"

REM Check if venv exists
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found at: %CD%\venv
    echo [INFO] Make sure you've run setup-windows.bat first from the project root
    echo [INFO] Project root should be: %CD%
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment
    echo [INFO] Make sure you've run setup-windows.bat first
    pause
    exit /b 1
)

REM Navigate back to demos folder
cd /d "%DEMOS_DIR%"

echo [OK] Virtual environment activated
echo [OK] Current directory: %CD%
echo.

REM Show menu
echo Select an agent to run:
echo   1. Vertex AI Agent Builder
echo   2. Gemini API Agent
echo   3. Ollama Agent (Local)
echo   4. Run Comparison Script
echo   5. Exit
echo.

set /p choice="Enter choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo Running Vertex AI Agent...
    python hello_world_agent_local.py
) else if "%choice%"=="2" (
    echo.
    echo Running Gemini API Agent...
    python hello_world_agent_local_gemini.py
) else if "%choice%"=="3" (
    echo.
    echo Running Ollama Agent...
    python hello_world_agent_local_ollama.py
) else if "%choice%"=="4" (
    echo.
    echo Running Comparison Script...
    python run_all_agents.py
) else if "%choice%"=="5" (
    echo.
    echo [OK] Exiting...
    exit /b 0
) else (
    echo.
    echo [ERROR] Invalid choice
)

echo.
pause

