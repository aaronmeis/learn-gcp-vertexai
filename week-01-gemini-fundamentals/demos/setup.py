"""
Setup script for Vertex AI Agent Builder project
This script helps set up the environment and verify prerequisites.
"""

import os
import subprocess
import sys

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_gcloud_installed():
    """Check if gcloud CLI is installed."""
    try:
        result = subprocess.run(
            ["gcloud", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✓ gcloud CLI is installed")
            return True
    except FileNotFoundError:
        pass
    print("⚠️  gcloud CLI not found. Install from: https://cloud.google.com/sdk/docs/install")
    return False

def check_environment_variables():
    """Check if required environment variables are set."""
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
    
    if not project_id or project_id == "your-project-id":
        print("⚠️  GOOGLE_CLOUD_PROJECT not set")
        print("   Set it with: export GOOGLE_CLOUD_PROJECT=your-project-id")
        return False
    
    print(f"✓ GOOGLE_CLOUD_PROJECT: {project_id}")
    print(f"✓ GOOGLE_CLOUD_LOCATION: {location}")
    return True

def check_authentication():
    """Check if user is authenticated with gcloud."""
    try:
        result = subprocess.run(
            ["gcloud", "auth", "list"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0 and "ACTIVE" in result.stdout:
            print("✓ gcloud authentication configured")
            return True
    except:
        pass
    print("⚠️  Not authenticated. Run: gcloud auth application-default login")
    return False

def install_dependencies():
    """Install Python dependencies."""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True
        )
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def main():
    """Run setup checks."""
    print("=" * 50)
    print("🚀 Vertex AI Agent Builder - Setup Check")
    print("=" * 50)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("gcloud CLI", check_gcloud_installed),
        ("Environment Variables", check_environment_variables),
        ("Authentication", check_authentication),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\nChecking {name}...")
        results.append(check_func())
    
    print("\n" + "=" * 50)
    
    if all(results):
        print("✅ All checks passed!")
        print("\n📚 Next steps:")
        print("  1. Run: python demos/hello_world_agent_local.py")
        print("  2. Deploy: python demos/deploy_agent.py")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print("\n💡 Quick fixes:")
        print("  - Install gcloud: https://cloud.google.com/sdk/docs/install")
        print("  - Set project: export GOOGLE_CLOUD_PROJECT=your-project-id")
        print("  - Authenticate: gcloud auth application-default login")
        print("  - Enable API: gcloud services enable aiplatform.googleapis.com")
    
    # Ask about installing dependencies
    if all(results):
        response = input("\n📦 Install Python dependencies? (y/n): ")
        if response.lower() == 'y':
            install_dependencies()

if __name__ == "__main__":
    main()

