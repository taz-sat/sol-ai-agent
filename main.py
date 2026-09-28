from app.config import (
    APP_ENV,
    SOLANA_RPC_URL,
    DATABASE_PATH,
)


def main():
    print("SOL AI Agent")
    print(f"Environment: {APP_ENV}")
    print(f"Solana RPC: {SOLANA_RPC_URL}")
    print(f"Database: {DATABASE_PATH}")


if __name__ == "__main__":
    main()