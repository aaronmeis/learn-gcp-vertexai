# Documentation Guide - Where to Start

This guide helps you navigate all the documentation files in this project.

## 🗺️ Documentation Flow

```mermaid
flowchart TD
    Start([New User?<br/>Start Here!]) --> Main[README.md<br/>📘 Main Project Overview]
    
    Main --> Q1{What do you<br/>need?}
    
    Q1 -->|🚀 Quick Start<br/>Get running fast| Quick[QUICKSTART.md<br/>⚡ 5-Minute Quick Start]
    Q1 -->|🪟 Windows Setup<br/>Step-by-step help| Win[WINDOWS_SETUP.md<br/>🪟 Complete Windows Guide]
    Q1 -->|🤔 Compare Options<br/>Which AI to use?| Local[LOCAL_AI_OPTIONS.md<br/>🔀 AI Options Comparison]
    Q1 -->|💻 Run Scripts<br/>Python demos| Demos[demos/README.md<br/>🐍 Demo Scripts Guide]
    Q1 -->|📓 Use Notebooks<br/>Jupyter demos| Notebooks[notebooks/README.md<br/>📓 Notebooks Guide]
    
    Quick --> Setup{First Time<br/>Setup?}
    Setup -->|Yes| Win
    Setup -->|No| Run[Ready to Run]
    
    Win --> Run
    Run --> Method{How to Run?}
    
    Method -->|Easiest Way| Launcher[RUN_ME.bat<br/>🎯 Quick Launcher<br/>Interactive Menu]
    Method -->|Direct Script| Agents{Which Agent?}
    
    Agents -->|Production<br/>Full Features| VA[hello_world_agent_local.py<br/>☁️ Vertex AI<br/>Requires GCP Setup]
    Agents -->|Simple<br/>API Key| GA[hello_world_agent_local_gemini.py<br/>🔑 Gemini API<br/>Just API Key]
    Agents -->|Local<br/>Offline| OA[hello_world_agent_local_ollama.py<br/>🏠 Ollama<br/>No Internet Needed]
    
    Local --> Decision{Choose Your<br/>AI Solution}
    Decision -->|Cloud Simple| GA
    Decision -->|Truly Local| OA
    Decision -->|Production| VA
    
    Demos --> Launcher
    Demos --> Compare[run_all_agents.py<br/>📊 Compare All Three]
    
    Notebooks --> NB{Which Notebook?}
    NB -->|Vertex AI| VNB[hello_world_agent_demo.ipynb<br/>☁️ Vertex AI Notebook]
    NB -->|Gemini API| GNB[hello_world_agent_gemini_demo.ipynb<br/>🔑 Gemini API Notebook]
    NB -->|Ollama| ONB[hello_world_agent_ollama_demo.ipynb<br/>🏠 Ollama Notebook]
    
    style Start fill:#e1f5ff,stroke:#01579b,stroke-width:3px
    style Main fill:#fff4e1,stroke:#e65100,stroke-width:2px
    style Quick fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Win fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Local fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Launcher fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style VA fill:#ffebee,stroke:#c62828,stroke-width:2px
    style GA fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style OA fill:#e0f2f1,stroke:#00695c,stroke-width:2px
```

## 📚 Documentation Files Overview

### Main Documentation

| File | Purpose | When to Use |
|------|---------|-------------|
| **[README.md](README.md)** | Main project overview | Start here for project introduction |
| **[QUICKSTART.md](QUICKSTART.md)** | 5-minute quick start | Want to get running fast |
| **[WINDOWS_SETUP.md](WINDOWS_SETUP.md)** | Complete Windows guide | Windows user, need detailed setup |
| **[LOCAL_AI_OPTIONS.md](LOCAL_AI_OPTIONS.md)** | AI options comparison | Deciding which AI solution to use |

### Code Documentation

| File | Purpose | When to Use |
|------|---------|-------------|
| **[demos/README.md](week-01-gemini-fundamentals/demos/README.md)** | Demo scripts guide | Running Python scripts |
| **[notebooks/README.md](week-01-gemini-fundamentals/notebooks/README.md)** | Notebooks guide | Using Jupyter notebooks |
| **[demos/QUICK_RUN.md](week-01-gemini-fundamentals/demos/QUICK_RUN.md)** | Quick run reference | Quick reference for running scripts |
| **[demos/README_RUN.md](week-01-gemini-fundamentals/demos/README_RUN.md)** | Run instructions | Detailed run instructions |

## 🎯 Recommended Paths

### Path 1: Quick Start (5 minutes)
```
QUICKSTART.md → Setup → RUN_ME.bat → Select Agent
```

### Path 2: Windows User (First Time)
```
WINDOWS_SETUP.md → setup-windows.bat → activate-env.bat → RUN_ME.bat
```

### Path 3: Compare Options First
```
LOCAL_AI_OPTIONS.md → Choose Option → Setup → Run Agent
```

### Path 4: Notebook User
```
notebooks/README.md → jupyter notebook → Open Notebook → Run Cells
```

### Path 5: Direct Script Runner
```
demos/README.md → activate-env.bat → python script_name.py
```

## 🚀 Quick Decision Tree

**I want to...**

- **Get started in 5 minutes** → [QUICKSTART.md](QUICKSTART.md)
- **Set up on Windows** → [WINDOWS_SETUP.md](WINDOWS_SETUP.md)
- **Understand my options** → [LOCAL_AI_OPTIONS.md](LOCAL_AI_OPTIONS.md)
- **Run code easily** → `cd week-01-gemini-fundamentals\demos` then `RUN_ME.bat`
- **Use notebooks** → [notebooks/README.md](week-01-gemini-fundamentals/notebooks/README.md)
- **See all documentation** → [README.md](README.md)

## 💡 Pro Tips

1. **First time?** Start with [QUICKSTART.md](QUICKSTART.md)
2. **Windows user?** Bookmark [WINDOWS_SETUP.md](WINDOWS_SETUP.md)
3. **Not sure which AI?** Read [LOCAL_AI_OPTIONS.md](LOCAL_AI_OPTIONS.md) first
4. **Want easiest way?** Use `RUN_ME.bat` - it handles everything
5. **Prefer notebooks?** Check [notebooks/README.md](week-01-gemini-fundamentals/notebooks/README.md)

## 🔗 All Documentation Files

- [README.md](README.md) - Main project documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [WINDOWS_SETUP.md](WINDOWS_SETUP.md) - Windows setup guide
- [LOCAL_AI_OPTIONS.md](LOCAL_AI_OPTIONS.md) - AI options comparison
- [week-01-gemini-fundamentals/demos/README.md](week-01-gemini-fundamentals/demos/README.md) - Demo scripts
- [week-01-gemini-fundamentals/notebooks/README.md](week-01-gemini-fundamentals/notebooks/README.md) - Notebooks guide
- [week-01-gemini-fundamentals/demos/QUICK_RUN.md](week-01-gemini-fundamentals/demos/QUICK_RUN.md) - Quick run reference
- [week-01-gemini-fundamentals/demos/README_RUN.md](week-01-gemini-fundamentals/demos/README_RUN.md) - Run instructions

