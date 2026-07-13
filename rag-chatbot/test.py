from dotenv import load_dotenv
import os

loaded = load_dotenv()

print("Loaded:", loaded)
print("Key:", repr(os.getenv("OPENAI_API_KEY")))