# Hello World Agents - Jupyter Notebooks

Interactive notebooks demonstrating all three Hello World agent implementations.

## 📓 Available Notebooks

### 1. Vertex AI Agent Builder
**File:** `hello_world_agent_demo.ipynb`

**Description:** Full-featured agent using Google Cloud Vertex AI Agent Builder.

**Requirements:**
- GCP project with billing enabled
- Vertex AI API enabled
- GCP credentials configured
- Environment variables: `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`

**Best For:** Production applications, full feature set

---

### 2. Gemini API
**File:** `hello_world_agent_gemini_demo.ipynb`

**Description:** Simple agent using Google's Gemini API. Just needs an API key!

**Requirements:**
- Gemini API key (free from https://makersuite.google.com/app/apikey)
- Environment variable: `GEMINI_API_KEY` in `.env` file

**Best For:** Quick development, learning, simple integrations

---

### 3. Ollama (Truly Local)
**File:** `hello_world_agent_ollama_demo.ipynb`

**Description:** Completely local agent using Ollama. Works offline, no API keys needed.

**Requirements:**
- Ollama installed (https://ollama.ai)
- Ollama service running
- A model pulled (e.g., `ollama pull llama2`)

**Best For:** Offline development, privacy-sensitive applications

---

## 🚀 Running the Notebooks

### Step 1: Activate Virtual Environment

**From project root:**
```powershell
# PowerShell
.\activate-env.ps1

# Command Prompt
activate-env.bat
```

### Step 2: Start Jupyter

```bash
jupyter notebook
# or
jupyter lab
```

### Step 3: Open a Notebook

Navigate to `week-01-gemini-fundamentals/notebooks/` and open:
- `hello_world_agent_demo.ipynb` - Vertex AI
- `hello_world_agent_gemini_demo.ipynb` - Gemini API
- `hello_world_agent_ollama_demo.ipynb` - Ollama

### Step 4: Run Cells

- Run cells sequentially (Shift+Enter)
- Each notebook includes:
  - Setup and configuration
  - Connection checks
  - Example interactions
  - Interactive functions you can use

## 📊 Comparison

| Feature | Vertex AI | Gemini API | Ollama |
|---------|-----------|------------|--------|
| **Setup** | Complex | Easy | Easy |
| **Internet** | Required | Required | Not needed |
| **API Key** | No (GCP) | Yes | No |
| **Cost** | Pay-as-you-go | Free tier | Free |
| **Best For** | Production | Development | Offline |

## 🔧 Setup Instructions

### Vertex AI Notebook
1. Set up GCP project and credentials
2. Set `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` in `.env`
3. Run cells in order

### Gemini API Notebook
1. Get API key: https://makersuite.google.com/app/apikey
2. Add `GEMINI_API_KEY=your-key` to `.env` file
3. Run cells in order

### Ollama Notebook
1. Install Ollama: https://ollama.ai
2. Start Ollama service
3. Pull a model: `ollama pull llama2`
4. Run cells in order

## 💡 Tips

- **Start with Gemini API** - Easiest to set up, just needs API key
- **Try Ollama** - For truly local, offline experimentation
- **Use Vertex AI** - When you need production features
- **Compare all three** - See the differences side-by-side

## 🆘 Troubleshooting

**Notebook won't start:**
- Make sure virtual environment is activated
- Install jupyter: `pip install jupyter`

**Import errors:**
- Ensure virtual environment is activated
- Install dependencies: `pip install -r requirements.txt`

**Ollama connection failed:**
- Check Ollama is running: `ollama list`
- Verify model is pulled: `ollama list`

**Gemini API errors:**
- Check API key is set in `.env` file
- Verify internet connection
- Check API quota/limits

## 📚 Related Resources

- [Main README](../../README.md) - Project overview
- [LOCAL_AI_OPTIONS.md](../../LOCAL_AI_OPTIONS.md) - Detailed comparison
- [Demos README](../demos/README.md) - Python script versions

