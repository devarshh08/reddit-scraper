import os
from dotenv import load_dotenv

print("=== Environment Variable Test ===")
print(f"Current working directory: {os.getcwd()}")
print(f"Script directory: {os.path.dirname(os.path.abspath(__file__))}")
print(f".env file exists in cwd: {os.path.exists('.env')}")
print(f".env file exists in script dir: {os.path.exists(os.path.join(os.path.dirname(__file__), '.env'))}")

# Try loading environment variables
result1 = load_dotenv()
print(f"load_dotenv() result: {result1}")

result2 = load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
print(f"load_dotenv(script_dir/.env) result: {result2}")

print("\n=== Environment Variables ===")
print(f"CLIENT_ID: {os.getenv('CLIENT_ID')}")
print(f"CLIENT_SECRET: {os.getenv('CLIENT_SECRET')}")
print(f"USER_AGENT: {os.getenv('USER_AGENT')}")

print(f"\n=== Validation ===")
print(f"All credentials present: {all([os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'), os.getenv('USER_AGENT')])}")