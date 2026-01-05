# Quick launcher for Hello World Agents (PowerShell)
# This script activates the virtual environment and runs the agent

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Hello World Agents - Quick Launcher" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to project root (assuming we're in demos folder)
$projectRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $projectRoot

# Activate virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
    Write-Host "[OK] Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Virtual environment not found" -ForegroundColor Red
    Write-Host "[INFO] Make sure you've run setup-windows.ps1 first" -ForegroundColor Yellow
    exit 1
}

# Navigate to demos folder
Set-Location "week-01-gemini-fundamentals\demos"

Write-Host "[OK] Current directory: $PWD" -ForegroundColor Green
Write-Host ""

# Show menu
Write-Host "Select an agent to run:" -ForegroundColor Yellow
Write-Host "  1. Vertex AI Agent Builder"
Write-Host "  2. Gemini API Agent"
Write-Host "  3. Ollama Agent (Local)"
Write-Host "  4. Run Comparison Script"
Write-Host "  5. Exit"
Write-Host ""

$choice = Read-Host "Enter choice (1-5)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "Running Vertex AI Agent..." -ForegroundColor Cyan
        python hello_world_agent_local.py
    }
    "2" {
        Write-Host ""
        Write-Host "Running Gemini API Agent..." -ForegroundColor Cyan
        python hello_world_agent_local_gemini.py
    }
    "3" {
        Write-Host ""
        Write-Host "Running Ollama Agent..." -ForegroundColor Cyan
        python hello_world_agent_local_ollama.py
    }
    "4" {
        Write-Host ""
        Write-Host "Running Comparison Script..." -ForegroundColor Cyan
        python run_all_agents.py
    }
    "5" {
        Write-Host ""
        Write-Host "[OK] Exiting..." -ForegroundColor Green
        exit 0
    }
    default {
        Write-Host ""
        Write-Host "[ERROR] Invalid choice" -ForegroundColor Red
    }
}

Write-Host ""

