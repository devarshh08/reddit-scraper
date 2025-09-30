#!/usr/bin/env python3
"""
Setup script for Reddit Scraper & Data Cleaner
This script helps users set up their environment and credentials.
"""

import os
import shutil

def setup_environment():
    print("🚀 Setting up Reddit Scraper & Data Cleaner")
    print("=" * 50)
    
    # Check if .env exists
    if os.path.exists('.env'):
        response = input("⚠️  .env file already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            return
    
    # Copy example file
    if os.path.exists('.env.example'):
        shutil.copy('.env.example', '.env')
        print("✅ Created .env file from template")
    else:
        # Create basic .env file
        with open('.env', 'w') as f:
            f.write("CLIENT_ID=your_client_id_here\n")
            f.write("CLIENT_SECRET=your_client_secret_here\n")
            f.write("USER_AGENT=script:your-app-name:v1.0 (by u/your_username)\n")
        print("✅ Created basic .env file")
    
    print("\n📝 Next steps:")
    print("1. Go to https://www.reddit.com/prefs/apps")
    print("2. Create a new app (choose 'script' type)")
    print("3. Copy your CLIENT_ID and CLIENT_SECRET")
    print("4. Edit the .env file and replace the placeholder values")
    print("5. Run: python -m streamlit run app.py")
    
    print("\n🔧 Your .env file location:", os.path.abspath('.env'))
    
    # Ask if user wants to edit now
    response = input("\n📝 Would you like to edit the .env file now? (y/N): ")
    if response.lower() == 'y':
        try:
            # Try to open with default editor
            if os.name == 'nt':  # Windows
                os.startfile('.env')
            else:  # Unix-like
                os.system('$EDITOR .env || nano .env || vi .env')
        except:
            print("Please manually edit the .env file with your preferred text editor.")

if __name__ == "__main__":
    setup_environment()