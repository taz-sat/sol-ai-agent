import os

from dotenv import load_dotenv

load_dotenv()

app_env = os.getenv("APP_ENV")

print("SOL AI Agent")
print("Environment:", app_env)