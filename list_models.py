import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("ERROR: GOOGLE_API_KEY not found in environment or .env file.")
    exit(1)

genai.configure(api_key=api_key)

print(f"API Key found: {api_key[:5]}...{api_key[-5:]}")

try:
    print("Listing available models...")
    models = genai.list_models()
    found = False
    for m in models:
        print(f"- {m.name} (Supported: {m.supported_generation_methods})")
        found = True
    if not found:
        print("No models found!")
except Exception as e:
    print(f"Error listing models: {e}")
