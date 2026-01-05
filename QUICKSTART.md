# Quick Start Guide - Vertex AI Agent Builder

Get your Hello World agent up and running in 5 minutes!

## 🚀 Step-by-Step Setup

### Windows Users (Recommended)

**1. Run the automated setup:**
```powershell
# PowerShell (Recommended)
.\setup-windows.ps1

# Or Command Prompt
setup-windows.bat
```
This automatically:
- Creates a Python virtual environment
- Installs all dependencies
- Sets up environment configuration

**2. Activate the environment:**
```powershell
# PowerShell
.\activate-env.ps1

# Or Command Prompt
activate-env.bat
```

**3. Configure your GCP project:**
Edit the `.env` file (created automatically) or set:
```powershell
$env:GOOGLE_CLOUD_PROJECT="your-project-id"
$env:GOOGLE_CLOUD_LOCATION="us-central1"
```

**4. Authenticate and enable APIs:**
```powershell
gcloud auth application-default login
gcloud services enable aiplatform.googleapis.com --project=$env:GOOGLE_CLOUD_PROJECT
```

**5. Run an agent (choose one):**

**Option A: Use Quick Launcher (Easiest)**
```cmd
cd week-01-gemini-fundamentals\demos
RUN_ME.bat
```

**Option B: Run Individual Agents**
```powershell
# Vertex AI (requires GCP setup)
python week-01-gemini-fundamentals\demos\hello_world_agent_local.py

# Gemini API (needs API key)
python week-01-gemini-fundamentals\demos\hello_world_agent_local_gemini.py

# Ollama (truly local, needs Ollama installed)
python week-01-gemini-fundamentals\demos\hello_world_agent_local_ollama.py
```

### Linux/Mac Users

**1. Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Configure GCP:**
```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

**4. Authenticate and enable APIs:**
```bash
gcloud auth application-default login
gcloud services enable aiplatform.googleapis.com --project=$GOOGLE_CLOUD_PROJECT
```

**5. Run the local agent:**
```bash
python week-01-gemini-fundamentals/demos/hello_world_agent_local.py
```

### 5. Deploy to Cloud

**Generate deployment configuration:**
```bash
python week-01-gemini-fundamentals/demos/deploy_agent.py
```

**Deploy in Console:**
1. Open [Vertex AI Agent Builder Console](https://console.cloud.google.com/ai/agents)
2. Click "Create Agent"
3. Use settings from `agent_config.json`
4. Add intents and flows
5. Train and deploy

## 📝 What You Get

- ✅ **Three Hello World agents** (Vertex AI, Gemini API, Ollama)
- ✅ **Interactive notebooks** for each agent type
- ✅ **Quick launcher** (`RUN_ME.bat`) for easy access
- ✅ **Comparison script** to test all three agents
- ✅ **Cloud deployment** configuration
- ✅ **Complete documentation**

## 🎯 Test Your Agents

**Try all three agents:**
- Vertex AI: Full-featured, production-ready
- Gemini API: Simple, cloud-based, just needs API key
- Ollama: Truly local, works offline, no API keys

**Test phrases:**
- "Hello"
- "What is Vertex AI?"
- "What can you do?"
- "Tell me about local AI"

See [LOCAL_AI_OPTIONS.md](LOCAL_AI_OPTIONS.md) for detailed comparison.

## 🆘 Need Help?

Check the main [README.md](README.md) for detailed documentation and troubleshooting.

