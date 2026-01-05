# How to Run the Hello World Agents

## ✅ Easiest Method: Use RUN_ME.bat

**From Command Prompt (Recommended):**
```cmd
cd week-01-gemini-fundamentals\demos
RUN_ME.bat
```

**From PowerShell:**
```powershell
cd week-01-gemini-fundamentals\demos
.\RUN_ME.bat
```

The `RUN_ME.bat` script will:
- ✅ Automatically find and activate the virtual environment
- ✅ Show you a menu to select which agent to run
- ✅ Handle all the path navigation for you

## 🔧 Manual Method

If you prefer to run manually:

### Step 1: Activate Virtual Environment

**From project root:**
```cmd
activate-env.bat
```

**Or manually:**
```cmd
venv\Scripts\activate.bat
```

### Step 2: Navigate to Demos Folder
```cmd
cd week-01-gemini-fundamentals\demos
```

### Step 3: Run an Agent
```cmd
python hello_world_agent_local.py          # Vertex AI
python hello_world_agent_local_gemini.py   # Gemini API
python hello_world_agent_local_ollama.py   # Ollama
```

## 🆘 Troubleshooting

### "The system cannot find the path specified"

**Solution:** Make sure you're running `RUN_ME.bat` from the `demos` folder:
```cmd
cd week-01-gemini-fundamentals\demos
RUN_ME.bat
```

### "Failed to activate virtual environment"

**Solution:** Make sure you've run the setup script first:
```cmd
# From project root
setup-windows.bat
```

### "ModuleNotFoundError"

**Solution:** Make sure virtual environment is activated (you should see `(venv)` in your prompt):
```cmd
venv\Scripts\activate.bat
pip install -r requirements.txt
```

## 📝 Quick Reference

| Task | Command |
|------|---------|
| Setup (first time) | `setup-windows.bat` |
| Activate environment | `activate-env.bat` |
| Run launcher | `cd week-01-gemini-fundamentals\demos` then `RUN_ME.bat` |
| Run Vertex AI | `python hello_world_agent_local.py` |
| Run Gemini API | `python hello_world_agent_local_gemini.py` |
| Run Ollama | `python hello_world_agent_local_ollama.py` |

