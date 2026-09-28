import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development")
SOLANA_RPC_URL = os.getenv(
    "SOLANA_RPC_URL",
    "http://127.0.0.1:8899"
)
DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "db/sol_ai_agent.db"
)