"""
Deploy Hello World Agent to Vertex AI Agent Builder Console
This script deploys the agent to Google Cloud Platform.
"""

import os
import json
from google.cloud import aiplatform
from google.cloud import dialogflowcx_v3beta1
from google.oauth2 import service_account
import vertexai
from vertexai.preview import agent_builder

# Configuration
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
AGENT_NAME = "hello-world-agent"
AGENT_DISPLAY_NAME = "Hello World Agent"

def initialize_vertex_ai():
    """Initialize Vertex AI with project and location."""
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    print(f"✓ Vertex AI initialized for project: {PROJECT_ID}, location: {LOCATION}")

def create_agent_in_console():
    """
    Create and deploy the agent to Vertex AI Agent Builder Console.
    This function sets up the agent configuration for cloud deployment.
    """
    print("\n🌐 Deploying Agent to Vertex AI Console...")
    
    # Initialize Vertex AI
    initialize_vertex_ai()
    
    # Agent configuration for deployment
    agent_config = {
        "display_name": AGENT_DISPLAY_NAME,
        "default_language_code": "en",
        "time_zone": "America/New_York",
        "description": "A simple Hello World agent demonstrating Vertex AI Agent Builder capabilities",
    }
    
    print(f"✓ Agent configuration prepared: {agent_config['display_name']}")
    
    # Note: Actual deployment requires using the Vertex AI Agent Builder API
    # or the Google Cloud Console. This script prepares the configuration.
    print("\n📋 Deployment Steps:")
    print("  1. Go to Vertex AI Agent Builder Console:")
    print(f"     https://console.cloud.google.com/ai/agents?project={PROJECT_ID}")
    print("  2. Click 'Create Agent'")
    print("  3. Use the following configuration:")
    print(f"     - Display Name: {AGENT_DISPLAY_NAME}")
    print(f"     - Language: English")
    print(f"     - Time Zone: America/New_York")
    print("  4. Add a simple flow:")
    print("     - Intent: 'greeting'")
    print("     - Training Phrases: ['hello', 'hi', 'hey']")
    print("     - Response: 'Hello! Welcome to Vertex AI Agent Builder.'")
    print("  5. Train and deploy the agent")
    
    return agent_config

def create_agent_flow_config():
    """
    Create a basic flow configuration for the Hello World agent.
    This can be imported into the Agent Builder console.
    """
    flow_config = {
        "display_name": "Hello World Flow",
        "description": "Basic greeting flow for Hello World agent",
        "intents": [
            {
                "display_name": "greeting",
                "training_phrases": [
                    "hello",
                    "hi",
                    "hey",
                    "good morning",
                    "good afternoon",
                    "greetings"
                ],
                "responses": [
                    {
                        "text": [
                            "Hello! Welcome to Vertex AI Agent Builder. How can I help you today?"
                        ]
                    }
                ]
            },
            {
                "display_name": "about_vertex_ai",
                "training_phrases": [
                    "what is vertex ai",
                    "tell me about vertex ai",
                    "what can vertex ai do",
                    "explain vertex ai"
                ],
                "responses": [
                    {
                        "text": [
                            "Vertex AI is Google Cloud's unified machine learning platform. "
                            "It helps you build, deploy, and scale ML models and AI agents efficiently."
                        ]
                    }
                ]
            },
            {
                "display_name": "agent_capabilities",
                "training_phrases": [
                    "what can you do",
                    "what are your capabilities",
                    "how can you help",
                    "what do you do"
                ],
                "responses": [
                    {
                        "text": [
                            "I'm a Hello World agent demonstrating Vertex AI Agent Builder capabilities. "
                            "I can answer questions, have conversations, and help you get started with AI agents!"
                        ]
                    }
                ]
            }
        ]
    }
    
    return flow_config

def save_agent_config(agent_config, flow_config):
    """Save agent configuration to a JSON file for reference."""
    config_file = "agent_config.json"
    full_config = {
        "agent": agent_config,
        "flow": flow_config
    }
    
    with open(config_file, "w") as f:
        json.dump(full_config, f, indent=2)
    
    print(f"\n✓ Agent configuration saved to: {config_file}")
    print("  You can use this file as a reference when creating the agent in the console.")

def main():
    """Main function to deploy the agent."""
    print("=" * 50)
    print("🚀 Vertex AI Agent Builder - Deploy Hello World Agent")
    print("=" * 50)
    
    # Check for required environment variables
    if PROJECT_ID == "your-project-id":
        print("\n⚠️  WARNING: Please set GOOGLE_CLOUD_PROJECT environment variable")
        print("   Example: export GOOGLE_CLOUD_PROJECT=your-project-id")
        return
    
    try:
        # Create agent configuration
        agent_config = create_agent_in_console()
        
        # Create flow configuration
        flow_config = create_agent_flow_config()
        
        # Save configuration
        save_agent_config(agent_config, flow_config)
        
        print("\n✅ Agent deployment configuration completed!")
        print("\n📚 Next Steps:")
        print("  1. Open the Vertex AI Agent Builder Console using the link above")
        print("  2. Create a new agent with the provided configuration")
        print("  3. Import or manually create the flows using agent_config.json")
        print("  4. Train and deploy your agent")
        print("  5. Test your agent using the test console")
        print("\n💡 Tip: Check agent_config.json for the complete configuration")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\n💡 Troubleshooting:")
        print("  - Ensure Vertex AI API is enabled in your project")
        print("  - Check your GCP credentials: gcloud auth application-default login")
        print("  - Verify project ID and location are correct")
        print("  - Ensure you have necessary permissions (Agent Builder Admin)")

if __name__ == "__main__":
    main()

