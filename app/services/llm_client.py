import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def ask_llm(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "format": "json"   # 🔥 ВОТ ЭТО КЛЮЧЕВОЕ
        }
    )

    if response.status_code != 200:
        raise Exception(f"Ollama error: {response.text}")

    # 🔥 теперь ответ уже JSON
    return response.json()["response"]