# Hello World Agents - Demo Scripts

This directory contains three different Hello World agent implementations, each demonstrating a different approach to building AI agents.

## 📁 Available Agents

### 1. Vertex AI Agent Builder
**File:** `hello_world_agent_local.py`

**Description:** Full-featured agent using Google Cloud Vertex AI Agent Builder. Requires complete GCP setup.

**Requirements:**
- GCP project with billing enabled
- Vertex AI API enabled
- GCP credentials configured
- Environment variables: `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`

**Run:**
```bash
python hello_world_agent_local.py
```

**Best For:** Production applications, full feature set, enterprise use

---

### 2. Gemini API
**File:** `hello_world_agent_local_gemini.py`

**Description:** Simple agent using Google's Gemini API. Similar simplicity to Ollama, but cloud-based.

**Requirements:**
- Gemini API key (free from https://makersuite.google.com/app/apikey)
- Environment variable: `GEMINI_API_KEY`

**Run:**
```bash
python hello_world_agent_local_gemini.py
```

**Best For:** Quick development, learning, simple integrations

---

### 3. Ollama (Truly Local)
**File:** `hello_world_agent_local_ollama.py`

**Description:** Completely local agent using Ollama. Works offline, no API keys needed.

**Requirements:**
- Ollama installed (https://ollama.ai)
- Ollama service running
- A model pulled (e.g., `ollama pull llama2`)

**Run:**
```bash
python hello_world_agent_local_ollama.py
```

**Best For:** Offline development, privacy-sensitive applications, local experimentation

---

## 🚀 Quick Start

### Easiest Method: Use Quick Launcher

**Windows Command Prompt (Recommended):**
```cmd
cd week-01-gemini-fundamentals\demos
RUN_ME.bat
```

**PowerShell:**
```powershell
cd week-01-gemini-fundamentals\demos
.\RUN_ME.ps1
```

The launcher automatically:
- ✅ Activates the virtual environment
- ✅ Shows a menu to select which agent to run
- ✅ Handles all path navigation

### Manual Method: Activate Virtual Environment First

**PowerShell:**
```powershell
# From project root
.\activate-env.ps1
cd week-01-gemini-fundamentals\demos
```

**Command Prompt:**
```cmd
# From project root
activate-env.bat
cd week-01-gemini-fundamentals\demos
```

### Run All Agents (Comparison)
```bash
python run_all_agents.py
```

This interactive script lets you:
- Run any of the three agents
- Compare their features
- See side-by-side differences

### Run Individual Agents

**Vertex AI:**
```bash
python hello_world_agent_local.py
```

**Gemini API:**
```bash
python hello_world_agent_local_gemini.py
```

**Ollama:**
```bash
python hello_world_agent_local_ollama.py
```

## 📊 Comparison

| Feature | Vertex AI | Gemini API | Ollama |
|---------|-----------|------------|--------|
| **Setup** | Complex | Easy | Easy |
| **Internet** | Required | Required | Not needed |
| **API Key** | No (GCP) | Yes | No |
| **Cost** | Pay-as-you-go | Free tier | Free |
| **Best For** | Production | Development | Offline |

## 🔧 Setup Instructions

### Vertex AI Setup
1. Create GCP project
2. Enable Vertex AI API
3. Set up credentials: `gcloud auth application-default login`
4. Set environment variables in `.env`:
   ```
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_CLOUD_LOCATION=us-central1
   ```

### Gemini API Setup
1. Get API key: https://makersuite.google.com/app/apikey
2. Add to `.env`:
   ```
   GEMINI_API_KEY=your-api-key-here
   ```

### Ollama Setup
1. Install Ollama: https://ollama.ai
2. Start Ollama service
3. Pull a model:
   ```bash
   ollama pull llama2
   # or
   ollama pull mistral
   ```

## 📝 Notes

- All agents use ASCII-safe output for Windows compatibility
- All agents follow similar structure for easy comparison
- Each agent demonstrates the same "Hello World" functionality
- See `LOCAL_AI_OPTIONS.md` in the project root for detailed comparison

## 🆘 Troubleshooting

**Vertex AI:**
- Ensure GCP project is set correctly
- Check API is enabled
- Verify credentials are configured

**Gemini API:**
- Check API key is correct in `.env`
- Verify internet connection
- Check API quota/limits

**Ollama:**
- Ensure Ollama service is running
- Verify model is pulled
- Check Ollama is accessible at `http://localhost:11434`

