# Quick activation script for Windows PowerShell
# Run this script to activate the virtual environment and set up environment variables

Write-Host "Activating virtual environment..." -ForegroundColor Yellow

# Activate virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
    Write-Host "[OK] Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Virtual environment not found. Run setup-windows.ps1 first." -ForegroundColor Red
    exit 1
}

# Load environment variables from .env file if it exists
if (Test-Path ".env") {
    Write-Host "`nLoading environment variables from .env..." -ForegroundColor Yellow
    Get-Content .env | ForEach-Object {
        # Skip empty lines and comments
        $line = $_.Trim()
        if ($line -and -not $line.StartsWith('#')) {
            # Match KEY=VALUE pattern (with optional spaces around =)
            if ($line -match '^\s*([^#=]+?)\s*=\s*(.*)$') {
                $key = $matches[1].Trim()
                $value = $matches[2].Trim()
                # Only set if key exists and value is not the placeholder
                if ($key -and $value -and $value -ne "your-project-id") {
                    [Environment]::SetEnvironmentVariable($key, $value, "Process")
                    Write-Host "  [OK] $key = $value" -ForegroundColor Gray
                }
            }
        }
    }
    Write-Host "[OK] Environment variables loaded" -ForegroundColor Green
} else {
    Write-Host "`n[WARNING] .env file not found. Using system environment variables." -ForegroundColor Yellow
}

# Check if project ID is set
$projectId = $env:GOOGLE_CLOUD_PROJECT
if (-not $projectId -or $projectId -eq "your-project-id") {
    Write-Host "`n[WARNING] GOOGLE_CLOUD_PROJECT not set. Set it with:" -ForegroundColor Yellow
    Write-Host "   `$env:GOOGLE_CLOUD_PROJECT='your-project-id'" -ForegroundColor Cyan
} else {
    Write-Host "`n[OK] Project ID: $projectId" -ForegroundColor Green
}

Write-Host "`n[SUCCESS] Environment ready!" -ForegroundColor Green
Write-Host "You can now run:" -ForegroundColor Yellow
Write-Host "  python week-01-gemini-fundamentals\demos\hello_world_agent_local.py" -ForegroundColor Cyan

