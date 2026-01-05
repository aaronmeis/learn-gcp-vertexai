# Local AI Options - Google/Gemini Alternatives

This document explains the different options for running AI locally, similar to Ollama, but using Google's technologies.

## 🎯 Quick Comparison

| Solution | Setup Complexity | Internet Required | Cost | Best For |
|----------|-----------------|-------------------|------|----------|
| **Ollama** | ⭐ Easy | ❌ No (after setup) | 💰 Free | Truly local, offline |
| **Gemini API** | ⭐⭐ Medium | ✅ Yes | 💰 Free tier | Simple, cloud-based |
| **Vertex AI** | ⭐⭐⭐ Complex | ✅ Yes | 💰 Pay-as-you-go | Production, full features |

## Option 1: Google Gemini API (Simplest Cloud Option)

**Similar to Ollama in simplicity, but requires internet connection.**

### Setup

1. **Get a free API key:**
   - Visit: https://makersuite.google.com/app/apikey
   - Sign in with Google account
   - Create a new API key

2. **Add to `.env` file:**
   ```
   GEMINI_API_KEY=your-api-key-here
   GEMINI_MODEL=gemini-pro
   ```

3. **Run the demo:**
   ```bash
   # Quick launcher (Windows)
   cd week-01-gemini-fundamentals\demos
   RUN_ME.bat
   # Then select option 2
   
   # Or run directly
   python week-01-gemini-fundamentals\demos\hello_world_agent_local_gemini.py
   ```

### Pros
- ✅ Simple setup (just API key)
- ✅ No GCP project needed
- ✅ Free tier available
- ✅ Easy to use in Python

### Cons
- ❌ Requires internet connection
- ❌ API rate limits
- ❌ Not truly "local"

### Code Example

```python
import google.generativeai as genai

genai.configure(api_key="your-api-key")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Hello!")
print(response.text)
```

## Option 2: Ollama (Truly Local)

**Completely local, works offline, no API keys needed.**

### Setup

1. **Install Ollama:**
   - Download from: https://ollama.ai
   - Install and start the service

2. **Pull a model:**
   ```bash
   ollama pull llama2
   # or
   ollama pull mistral
   ```

3. **Run the demo:**
   ```bash
   # Quick launcher (Windows)
   cd week-01-gemini-fundamentals\demos
   RUN_ME.bat
   # Then select option 3
   
   # Or run directly
   python week-01-gemini-fundamentals\demos\hello_world_agent_local_ollama.py
   ```

### Pros
- ✅ Works completely offline
- ✅ No API keys or accounts
- ✅ Full control over models
- ✅ Privacy (data stays local)

### Cons
- ❌ Requires significant disk space (models are large)
- ❌ Requires good hardware (GPU recommended)
- ❌ Not Google/Gemini models

### Code Example

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama2", "prompt": "Hello!"}
)
print(response.json()["response"])
```

## Option 3: Vertex AI (Full Cloud Solution)

**Most features, but requires full GCP setup.**

### Setup

See the main README.md for full setup instructions.

### Pros
- ✅ Most features and capabilities
- ✅ Production-ready
- ✅ Scalable
- ✅ Full Google Cloud integration

### Cons
- ❌ Complex setup (GCP project, billing, etc.)
- ❌ Requires internet
- ❌ Costs money (pay-as-you-go)

## 🚀 Recommended Path

### For Learning/Development:
1. **Start with Gemini API** - Simplest, free tier, good for learning
2. **Try Ollama** - If you want truly local, offline capability
3. **Move to Vertex AI** - When you need production features

### For Production:
- Use **Vertex AI** for scalable, managed infrastructure
- Use **Gemini API** for simple integrations
- Use **Ollama** for on-premises/offline requirements

## 📝 Code Examples

All examples are in `week-01-gemini-fundamentals/demos/`:

- `hello_world_agent_local_gemini.py` - Gemini API version
- `hello_world_agent_local_ollama.py` - Ollama version  
- `hello_world_agent_local.py` - Vertex AI version
- `run_all_agents.py` - Comparison script to run all three
- `RUN_ME.bat` / `RUN_ME.ps1` - Quick launcher scripts

**Notebooks** are in `week-01-gemini-fundamentals/notebooks/`:

- `hello_world_agent_gemini_demo.ipynb` - Gemini API notebook
- `hello_world_agent_ollama_demo.ipynb` - Ollama notebook
- `hello_world_agent_demo.ipynb` - Vertex AI notebook

## 🔗 Resources

- **Gemini API**: https://ai.google.dev/
- **Ollama**: https://ollama.ai
- **Vertex AI**: https://cloud.google.com/vertex-ai
- **Gemini API Key**: https://makersuite.google.com/app/apikey

## 💡 Which Should You Choose?

- **Just want to try AI quickly?** → Gemini API (just needs API key)
- **Want offline/local?** → Ollama (works completely offline)
- **Building production app?** → Vertex AI (full features, scalable)
- **Learning/experimenting?** → Start with Gemini API, try Ollama for local
- **Want to compare all three?** → Use `RUN_ME.bat` or `run_all_agents.py`

## 🚀 Quick Start

**Easiest way to try all three:**

1. Run setup: `setup-windows.bat` (or `setup-windows.ps1`)
2. Use quick launcher: `cd week-01-gemini-fundamentals\demos` then `RUN_ME.bat`
3. Select an agent from the menu (1-4)
4. Or explore notebooks: `jupyter notebook`

