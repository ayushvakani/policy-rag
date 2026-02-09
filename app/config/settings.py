import os
from dotenv import load_dotenv

load_dotenv()

# --------------------------------------------------
# Base directory (must resolve to Policy_RAG2)
# --------------------------------------------------
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

# --------------------------------------------------
# Vector DB (EXISTING, DO NOT CHANGE)
# --------------------------------------------------
VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    os.path.join(BASE_DIR, "notebooks", "Data", "vector_store")
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "policy_documents_final"
)

# --------------------------------------------------
# Ollama (LOCAL LLM ONLY)
# --------------------------------------------------
OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.1:latest"
)



# --------------------------------------------------
# Debug (safe to keep for now)
# --------------------------------------------------
print("🔍 BASE_DIR:", BASE_DIR)
print("🔍 VECTOR_DB_PATH:", VECTOR_DB_PATH)
print("🤖 OLLAMA_MODEL:", OLLAMA_MODEL)
