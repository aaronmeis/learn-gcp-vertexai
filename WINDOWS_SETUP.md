# Windows Setup Guide - Vertex AI Agent Builder

Complete guide for setting up and running the Vertex AI Agent Builder project on Windows.

## 🎯 Quick Setup (Automated)

The easiest way to get started on Windows:

### Option 1: PowerShell (Recommended)

1. **Open PowerShell** in the project directory
2. **Run the setup script**:
   ```powershell
   .\setup-windows.ps1
   ```
3. **If you get an execution policy error**, run this first:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   Then run `.\setup-windows.ps1` again.

### Option 2: Command Prompt

1. **Open Command Prompt** in the project directory
2. **Run the batch file**:
   ```cmd
   setup-windows.bat
   ```

## 📋 What the Setup Scripts Do

Both scripts (`setup-windows.ps1` and `setup-windows.bat`) will:

1. ✅ Check Python installation (requires Python 3.8+)
2. ✅ Create a Python virtual environment (`venv` folder)
3. ✅ Activate the virtual environment
4. ✅ Upgrade pip to the latest version
5. ✅ Install all required dependencies from `requirements.txt`
6. ✅ Create a `.env` file from `env.example.txt` template
7. ✅ Check for gcloud CLI installation

## 🔧 Manual Setup (If Needed)

If you prefer to set up manually:

### 1. Create Virtual Environment

```powershell
python -m venv venv
```

### 2. Activate Virtual Environment

**PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables

**Option A: Using .env file (Recommended)**

1. Copy `env.example.txt` to `.env`
2. Edit `.env` and set your project ID:
   ```
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_CLOUD_LOCATION=us-central1
   ```

**Option B: Set in PowerShell session**

```powershell
$env:GOOGLE_CLOUD_PROJECT="your-project-id"
$env:GOOGLE_CLOUD_LOCATION="us-central1"
```

**Option C: Set in Command Prompt session**

```cmd
set GOOGLE_CLOUD_PROJECT=your-project-id
set GOOGLE_CLOUD_LOCATION=us-central1
```

## 🚀 Running the Project

### Activate Environment First

Always activate your virtual environment before running scripts:

**PowerShell:**
```powershell
.\activate-env.ps1
```

**Command Prompt:**
```cmd
activate-env.bat
```

Or manually:
```powershell
.\venv\Scripts\Activate.ps1
```

### Run Agents

**Easiest: Use Quick Launcher**
```cmd
cd week-01-gemini-fundamentals\demos
RUN_ME.bat
```

**Or run individually:**

**Vertex AI Agent:**
```powershell
python week-01-gemini-fundamentals\demos\hello_world_agent_local.py
```

**Gemini API Agent:**
```powershell
python week-01-gemini-fundamentals\demos\hello_world_agent_local_gemini.py
```

**Ollama Agent (Local):**
```powershell
python week-01-gemini-fundamentals\demos\hello_world_agent_local_ollama.py
```

**Compare All Three:**
```powershell
python week-01-gemini-fundamentals\demos\run_all_agents.py
```

### Run Jupyter Notebooks

```powershell
jupyter notebook
# or
jupyter lab
```

Then open notebooks from `week-01-gemini-fundamentals/notebooks/`

### Deploy to Cloud

```powershell
python week-01-gemini-fundamentals\demos\deploy_agent.py
```

## 🔍 Troubleshooting

### PowerShell Execution Policy Error

**Error:** `cannot be loaded because running scripts is disabled`

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try running the script again.

### Virtual Environment Not Activating

**Check:**
- Make sure you're in the project root directory
- Verify `venv` folder exists (run setup script if not)
- Try activating manually: `.\venv\Scripts\Activate.ps1`

### Python Not Found

**Error:** `python: command not found` or `'python' is not recognized`

**Solutions:**
1. Install Python from [python.org](https://www.python.org/downloads/)
2. Make sure Python is added to PATH during installation
3. Restart your terminal after installation
4. Try `py` instead of `python` (Windows Python Launcher)

### Module Not Found Errors

**Solution:**
1. Make sure virtual environment is activated (you should see `(venv)` in prompt)
2. Reinstall dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

### gcloud Not Found

**Solution:**
1. Install Google Cloud SDK from [cloud.google.com/sdk](https://cloud.google.com/sdk/docs/install)
2. Restart your terminal after installation
3. Run `gcloud init` to configure

### Environment Variables Not Persisting

**Note:** Environment variables set in PowerShell/CMD only last for that session.

**Solutions:**
1. Use `.env` file (loaded automatically by `activate-env.ps1`)
2. Set variables each time you open a new terminal
3. Add to Windows System Environment Variables (permanent)

## 📚 Next Steps

1. ✅ Complete setup (run `setup-windows.ps1`)
2. ✅ Configure GCP project (edit `.env` file) - *Optional for Gemini API/Ollama*
3. ✅ Try the quick launcher: `cd week-01-gemini-fundamentals\demos` then `RUN_ME.bat`
4. ✅ Test all three agents (Vertex AI, Gemini API, Ollama)
5. ✅ Explore notebooks: `jupyter notebook`
6. ✅ For Vertex AI: Authenticate and enable API
   - `gcloud auth application-default login`
   - `gcloud services enable aiplatform.googleapis.com`
7. ✅ Deploy to cloud: `python week-01-gemini-fundamentals\demos\deploy_agent.py`

## 💡 Tips

- **Always activate virtual environment** before running Python scripts
- **Use `.env` file** for persistent environment variable configuration
- **Keep PowerShell/CMD open** to maintain environment variables in that session
- **Check Python version**: `python --version` (should be 3.8+)
- **Verify virtual environment**: You should see `(venv)` in your prompt when activated

## 🆘 Still Having Issues?

Check the main [README.md](README.md) for more troubleshooting tips and detailed documentation.

