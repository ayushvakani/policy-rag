from langchain_community.chat_models import ChatOllama
from app.config.settings import OLLAMA_MODEL, OLLAMA_BASE_URL

def get_llm():
    return ChatOllama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0.1,
        num_ctx=4096,
    )
