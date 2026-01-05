# Quick Run Guide - Hello World Agents

## ⚠️ Important: Activate Virtual Environment First!

### Easiest Way: Use the Quick Launcher

**Windows Command Prompt (Recommended - No execution policy issues):**
```cmd
# From project root or demos folder
cd week-01-gemini-fundamentals\demos
RUN_ME.bat
```

**PowerShell:**
```powershell
# From project root or demos folder
cd week-01-gemini-fundamentals\demos
.\RUN_ME.ps1
```

### Manual Activation

**Windows Command Prompt:**
```cmd
# From project root
activate-env.bat
cd week-01-gemini-fundamentals\demos
```

**Windows PowerShell:**
```powershell
# From project root
.\activate-env.ps1
cd week-01-gemini-fundamentals\demos
```

**Note:** If you get PowerShell execution policy errors, use the `.bat` file instead or run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 🚀 Running the Agents

### Option 1: Run Individual Agents

**Vertex AI Agent:**
```bash
python hello_world_agent_local.py
```

**Gemini API Agent:**
```bash
python hello_world_agent_local_gemini.py
```

**Ollama Agent:**
```bash
python hello_world_agent_local_ollama.py
```

### Option 2: Run Comparison Script

```bash
python run_all_agents.py
```

This gives you an interactive menu to run and compare all three agents.

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"

**Solution:** Activate the virtual environment first!
```powershell
.\venv\Scripts\Activate.ps1
```

### "ModuleNotFoundError" for any package

**Solution:** 
1. Make sure virtual environment is activated (you should see `(venv)` in your prompt)
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### "Ollama is not running"

**Solution:**
1. Install Ollama: https://ollama.ai
2. Start Ollama service
3. Pull a model: `ollama pull llama2`

### "GEMINI_API_KEY not found"

**Solution:**
1. Get API key: https://makersuite.google.com/app/apikey
2. Add to `.env` file: `GEMINI_API_KEY=your-key-here`

## ✅ Quick Checklist

Before running scripts, ensure:
- [ ] Virtual environment is activated (`(venv)` in prompt)
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Required environment variables set (check `.env` file)
- [ ] Required services running (Ollama, if using Ollama agent)

## 📝 Example Workflow

```powershell
# 1. Activate environment
.\activate-env.ps1

# 2. Navigate to demos
cd week-01-gemini-fundamentals\demos

# 3. Run an agent
python hello_world_agent_local_gemini.py

# Or run comparison
python run_all_agents.py
```

