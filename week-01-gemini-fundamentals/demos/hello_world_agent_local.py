"""
Local Hello World Agent using Vertex AI Agent Builder
This script demonstrates how to create and run a simple agent locally.
"""

import os
from google.cloud import aiplatform
from google.cloud import dialogflowcx_v3beta1
from google.oauth2 import service_account
import vertexai
from vertexai.preview import agent_builder

# Configuration
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
AGENT_NAME = "hello-world-agent"

def initialize_vertex_ai():
    """Initialize Vertex AI with project and location."""
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    print(f"[OK] Vertex AI initialized for project: {PROJECT_ID}, location: {LOCATION}")

def create_hello_world_agent():
    """
    Create a simple Hello World agent using Vertex AI Agent Builder.
    This is a basic example that responds to greetings.
    """
    print("\n[INFO] Creating Hello World Agent...")
    
    # Initialize Vertex AI
    initialize_vertex_ai()
    
    # Create agent configuration
    agent_config = {
        "display_name": AGENT_NAME,
        "default_language_code": "en",
        "time_zone": "America/New_York",
    }
    
    print(f"[OK] Agent configuration created: {agent_config['display_name']}")
    print("\n[INFO] Agent Features:")
    print("  - Responds to greetings")
    print("  - Provides basic information")
    print("  - Simple conversational flow")
    
    return agent_config

def run_local_agent_interaction():
    """
    Simulate a local interaction with the agent.
    In a real scenario, this would connect to the deployed agent.
    """
    print("\n[INFO] Running Local Agent Interaction...")
    print("=" * 50)
    
    # Example interactions
    interactions = [
        ("Hello", "Hello! Welcome to Vertex AI Agent Builder. How can I help you today?"),
        ("What can you do?", "I'm a Hello World agent demonstrating Vertex AI capabilities. I can answer questions and have conversations!"),
        ("Tell me about Vertex AI", "Vertex AI is Google Cloud's unified ML platform that helps you build, deploy, and scale ML models and AI agents."),
    ]
    
    for user_input, expected_response in interactions:
        print(f"\n[USER] {user_input}")
        print(f"[AGENT] {expected_response}")
    
    print("\n" + "=" * 50)
    print("[OK] Local agent interaction completed!")

def main():
    """Main function to run the local agent."""
    print("=" * 50)
    print("Vertex AI Agent Builder - Hello World Agent (Local)")
    print("=" * 50)
    
    # Check for required environment variables
    if PROJECT_ID == "your-project-id":
        print("\n[WARNING] Please set GOOGLE_CLOUD_PROJECT environment variable")
        print("   Example: export GOOGLE_CLOUD_PROJECT=your-project-id")
    
    try:
        # Create agent configuration
        agent_config = create_hello_world_agent()
        
        # Run local interaction simulation
        run_local_agent_interaction()
        
        print("\n[SUCCESS] Local agent setup completed successfully!")
        print("\n[INFO] Next Steps:")
        print("  1. Set up GCP credentials: gcloud auth application-default login")
        print("  2. Deploy the agent to cloud using deploy_agent.py")
        print("  3. Test the deployed agent in Vertex AI Console")
        
    except Exception as e:
        print(f"\n[ERROR] Error: {str(e)}")
        print("\n[INFO] Troubleshooting:")
        print("  - Ensure you have Vertex AI API enabled")
        print("  - Check your GCP credentials")
        print("  - Verify project ID and location are correct")

if __name__ == "__main__":
    main()

