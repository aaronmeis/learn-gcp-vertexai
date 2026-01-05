# Windows PowerShell Setup Script for Vertex AI Agent Builder
# This script sets up a Python virtual environment and installs dependencies

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "🚀 Vertex AI Agent Builder - Windows Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion found" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python 3.8+ from https://www.python.org/downloads/" -ForegroundColor Red
    exit 1
}

# Check if venv module is available
Write-Host "`nChecking Python venv module..." -ForegroundColor Yellow
try {
    python -m venv --help | Out-Null
    Write-Host "✓ venv module available" -ForegroundColor Green
} catch {
    Write-Host "❌ venv module not available. Please install Python with venv support." -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host "`nCreating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "⚠️  Virtual environment 'venv' already exists. Skipping creation." -ForegroundColor Yellow
} else {
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "`nActivating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "⚠️  If activation failed, you may need to run:" -ForegroundColor Yellow
    Write-Host "   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Cyan
    Write-Host "   Then run: .\venv\Scripts\Activate.ps1" -ForegroundColor Cyan
}

# Upgrade pip
Write-Host "`nUpgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip
Write-Host "✓ pip upgraded" -ForegroundColor Green

# Install dependencies
Write-Host "`nInstalling dependencies..." -ForegroundColor Yellow
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
    } else {
        Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "⚠️  requirements.txt not found" -ForegroundColor Yellow
}

# Check for .env file
Write-Host "`nChecking environment configuration..." -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host "✓ .env file found" -ForegroundColor Green
} else {
    Write-Host "⚠️  .env file not found. Creating from template..." -ForegroundColor Yellow
    if (Test-Path "env.example.txt") {
        Copy-Item "env.example.txt" ".env"
        Write-Host "✓ .env file created from template" -ForegroundColor Green
        Write-Host "⚠️  Please edit .env file with your GCP project details" -ForegroundColor Yellow
    } else {
        Write-Host "⚠️  env.example.txt not found. Please create .env manually." -ForegroundColor Yellow
    }
}

# Check gcloud CLI
Write-Host "`nChecking gcloud CLI..." -ForegroundColor Yellow
try {
    $gcloudVersion = gcloud --version 2>&1 | Select-Object -First 1
    Write-Host "✓ $gcloudVersion found" -ForegroundColor Green
} catch {
    Write-Host "⚠️  gcloud CLI not found. Install from: https://cloud.google.com/sdk/docs/install" -ForegroundColor Yellow
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "✅ Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Activate the virtual environment:" -ForegroundColor White
Write-Host "   .\venv\Scripts\Activate.ps1" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. Set your GCP project ID:" -ForegroundColor White
Write-Host "   `$env:GOOGLE_CLOUD_PROJECT='your-project-id'" -ForegroundColor Cyan
Write-Host "   `$env:GOOGLE_CLOUD_LOCATION='us-central1'" -ForegroundColor Cyan
Write-Host ""
Write-Host "3. Authenticate with GCP:" -ForegroundColor White
Write-Host "   gcloud auth application-default login" -ForegroundColor Cyan
Write-Host ""
Write-Host "4. Run the local agent:" -ForegroundColor White
Write-Host "   python week-01-gemini-fundamentals\demos\hello_world_agent_local.py" -ForegroundColor Cyan
Write-Host ""

