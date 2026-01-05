"""
Ollama-style Local AI Agent
This demonstrates how to use a truly local LLM (like Ollama) as an alternative to cloud-based solutions.

For Google/Gemini: Use the Gemini API version (hello_world_agent_local_gemini.py)
For truly local: Install Ollama and use this script
"""

import os
import requests
import json
import sys
from typing import Optional

# Fix Windows console encoding for Unicode characters
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2")  # or "mistral", "codellama", etc.

def check_ollama_running() -> bool:
    """Check if Ollama is running locally."""
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=2)
        return response.status_code == 200
    except:
        return False

def chat_with_ollama(prompt: str, model: str = None) -> Optional[str]:
    """Send a prompt to Ollama and get a response."""
    if not model:
        model = OLLAMA_MODEL
    
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            return f"[ERROR] Ollama API error: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return None
    except Exception as e:
        return f"[ERROR] {str(e)}"

def create_hello_world_agent():
    """Create a Hello World agent using Ollama."""
    if not check_ollama_running():
        print("\n[ERROR] Ollama is not running!")
        print("\nTo use this script:")
        print("1. Install Ollama: https://ollama.ai")
        print("2. Start Ollama service")
        print("3. Pull a model: ollama pull llama2")
        print("4. Run this script again")
        return None
    
    print(f"[OK] Ollama is running at {OLLAMA_BASE_URL}")
    print(f"[OK] Using model: {OLLAMA_MODEL}")
    return True

def run_demo():
    """Run a demo conversation."""
    print("\n" + "=" * 50)
    print("Hello World Agent - Ollama (Truly Local)")
    print("=" * 50)
    
    if not create_hello_world_agent():
        return
    
    # System prompt
    system_prompt = """You are a helpful Hello World agent. 
    Answer questions about AI, help users learn about local LLMs, and be friendly and concise."""
    
    # Example interactions
    interactions = [
        "Hello! What can you do?",
        "Tell me about running AI models locally.",
        "How is this different from cloud AI?"
    ]
    
    print("\n[INFO] Example interactions:\n")
    for user_input in interactions:
        print(f"[USER] {user_input}")
        full_prompt = f"{system_prompt}\n\nUser: {user_input}\nAssistant:"
        response = chat_with_ollama(full_prompt)
        
        if response:
            print(f"[AGENT] {response}\n")
        else:
            print("[ERROR] Failed to get response from Ollama\n")
    
    print("=" * 50)
    print("\n[INFO] For interactive mode, modify this script or use Ollama CLI directly")
    print("       Example: ollama run llama2")

def main():
    """Main function."""
    print("=" * 50)
    print("Ollama - Hello World Agent (Truly Local)")
    print("=" * 50)
    print("\n[INFO] This uses Ollama for truly local AI (no internet required after setup)")
    print("[INFO] Alternative to cloud-based Vertex AI/Gemini")
    print()
    
    run_demo()
    
    print("\n[SUCCESS] Demo completed!")
    print("\n[INFO] Comparison:")
    print("  Ollama: Truly local, no API keys, works offline")
    print("  Gemini API: Cloud-based, needs API key, simpler than Vertex AI")
    print("  Vertex AI: Full GCP setup, most features, cloud-only")

if __name__ == "__main__":
    main()

