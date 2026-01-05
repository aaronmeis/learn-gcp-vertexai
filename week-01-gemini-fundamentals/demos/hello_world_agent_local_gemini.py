"""
Local Hello World Agent using Google Generative AI (Gemini API)
This version uses the simpler Gemini API with just an API key - no full GCP setup required!
Similar to how Ollama works - simpler local development.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-pro")  # or "gemini-1.5-flash" for faster responses

def initialize_gemini():
    """Initialize Gemini API with API key."""
    if not API_KEY:
        print("\n[WARNING] GEMINI_API_KEY not found in environment variables!")
        print("Get your free API key from: https://makersuite.google.com/app/apikey")
        print("Then add it to your .env file: GEMINI_API_KEY=your-api-key-here")
        return False
    
    genai.configure(api_key=API_KEY)
    print(f"[OK] Gemini API initialized with model: {MODEL_NAME}")
    return True

def create_simple_agent():
    """
    Create a simple conversational agent using Gemini.
    This is much simpler than Vertex AI Agent Builder - just direct API calls!
    """
    if not initialize_gemini():
        return None
    
    # Create the model instance
    model = genai.GenerativeModel(MODEL_NAME)
    
    # Set up a simple system instruction (like a prompt)
    system_instruction = """You are a helpful Hello World agent demonstrating Google's Gemini AI capabilities.
    You can:
    - Answer questions about Vertex AI and Google Cloud
    - Have friendly conversations
    - Help users get started with AI development
    
    Keep responses concise and friendly."""
    
    return model, system_instruction

def chat_with_agent(model, system_instruction, user_input):
    """Send a message to the agent and get a response."""
    try:
        # Combine system instruction with user input
        prompt = f"{system_instruction}\n\nUser: {user_input}\nAgent:"
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[ERROR] Failed to get response: {str(e)}"

def run_interactive_chat():
    """Run an interactive chat session with the agent."""
    print("\n" + "=" * 50)
    print("Hello World Agent - Gemini API (Local-like)")
    print("=" * 50)
    print("\n[INFO] Type 'quit' or 'exit' to end the conversation\n")
    
    # Initialize agent
    result = create_simple_agent()
    if not result:
        return
    
    model, system_instruction = result
    
    # Example interactions
    example_interactions = [
        ("Hello", None),
        ("What is Vertex AI?", None),
        ("What can you do?", None),
    ]
    
    print("[INFO] Example interactions:")
    for user_msg, _ in example_interactions:
        print(f"\n[USER] {user_msg}")
        response = chat_with_agent(model, system_instruction, user_msg)
        print(f"[AGENT] {response}")
    
    print("\n" + "=" * 50)
    print("\n[INFO] For interactive mode, uncomment the code below or run:")
    print("       python -i hello_world_agent_local_gemini.py")
    print("=" * 50)
    
    # Uncomment below for interactive mode
    # while True:
    #     user_input = input("\n👤 You: ").strip()
    #     if user_input.lower() in ['quit', 'exit', 'q']:
    #         print("\n[OK] Goodbye!")
    #         break
    #     if user_input:
    #         response = chat_with_agent(model, system_instruction, user_input)
    #         print(f"🤖 Agent: {response}")

def main():
    """Main function to run the local Gemini agent."""
    print("=" * 50)
    print("Google Gemini API - Hello World Agent")
    print("=" * 50)
    print("\n[INFO] This version uses Gemini API directly (simpler than Vertex AI)")
    print("[INFO] Similar to Ollama - just needs an API key, no full GCP setup!")
    print()
    
    run_interactive_chat()
    
    print("\n[SUCCESS] Demo completed!")
    print("\n[INFO] Next Steps:")
    print("  1. Get a free Gemini API key: https://makersuite.google.com/app/apikey")
    print("  2. Add to .env: GEMINI_API_KEY=your-api-key")
    print("  3. Run this script again for interactive chat")
    print("  4. Or use in your own Python scripts!")

if __name__ == "__main__":
    main()

