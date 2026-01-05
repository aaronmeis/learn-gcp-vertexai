"""
Run All Hello World Agents - Comparison Script
This script allows you to run and compare all three Hello World agents:
1. Vertex AI Agent Builder
2. Gemini API
3. Ollama (local)
"""

import os
import sys
import subprocess

def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def run_vertex_ai_agent():
    """Run the Vertex AI Agent Builder version."""
    print_header("1. Vertex AI Agent Builder - Hello World Agent")
    print("[INFO] This requires GCP project setup and credentials")
    print("[INFO] Running: hello_world_agent_local.py\n")
    
    try:
        subprocess.run([sys.executable, "hello_world_agent_local.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to run Vertex AI agent: {e}")
    except FileNotFoundError:
        print("[ERROR] Python not found. Make sure virtual environment is activated.")

def run_gemini_api_agent():
    """Run the Gemini API version."""
    print_header("2. Gemini API - Hello World Agent")
    print("[INFO] This requires GEMINI_API_KEY in .env file")
    print("[INFO] Get free key from: https://makersuite.google.com/app/apikey")
    print("[INFO] Running: hello_world_agent_local_gemini.py\n")
    
    try:
        subprocess.run([sys.executable, "hello_world_agent_local_gemini.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to run Gemini API agent: {e}")
    except FileNotFoundError:
        print("[ERROR] Python not found. Make sure virtual environment is activated.")

def run_ollama_agent():
    """Run the Ollama version."""
    print_header("3. Ollama - Hello World Agent (Truly Local)")
    print("[INFO] This requires Ollama installed and running locally")
    print("[INFO] Install from: https://ollama.ai")
    print("[INFO] Running: hello_world_agent_local_ollama.py\n")
    
    try:
        subprocess.run([sys.executable, "hello_world_agent_local_ollama.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to run Ollama agent: {e}")
    except FileNotFoundError:
        print("[ERROR] Python not found. Make sure virtual environment is activated.")

def show_comparison():
    """Show a comparison table of all three agents."""
    print_header("Agent Comparison")
    print("\n" + "-" * 70)
    print(f"{'Feature':<25} {'Vertex AI':<15} {'Gemini API':<15} {'Ollama':<15}")
    print("-" * 70)
    print(f"{'Setup Complexity':<25} {'Complex':<15} {'Easy':<15} {'Easy':<15}")
    print(f"{'Internet Required':<25} {'Yes':<15} {'Yes':<15} {'No':<15}")
    print(f"{'API Key Needed':<25} {'No (GCP)':<15} {'Yes':<15} {'No':<15}")
    print(f"{'Cost':<25} {'Pay-as-you-go':<15} {'Free tier':<15} {'Free':<15}")
    print(f"{'Best For':<25} {'Production':<15} {'Development':<15} {'Offline':<15}")
    print("-" * 70)

def main():
    """Main menu for running agents."""
    print("=" * 70)
    print("  Hello World Agents - Comparison Runner")
    print("=" * 70)
    print("\n[INFO] This script helps you run and compare all three Hello World agents")
    print("\nAvailable agents:")
    print("  1. Vertex AI Agent Builder (Full GCP setup)")
    print("  2. Gemini API (Simple API key)")
    print("  3. Ollama (Truly local, no internet)")
    print("  4. Show comparison table")
    print("  5. Exit")
    
    while True:
        print("\n" + "-" * 70)
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == "1":
            run_vertex_ai_agent()
        elif choice == "2":
            run_gemini_api_agent()
        elif choice == "3":
            run_ollama_agent()
        elif choice == "4":
            show_comparison()
        elif choice == "5":
            print("\n[OK] Exiting. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    main()

