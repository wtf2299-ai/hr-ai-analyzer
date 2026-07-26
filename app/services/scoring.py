import json
from app.services.llm_client import ask_llm
from app.utils.json_utils import extract_json


def load_prompt():
    with open("app/prompts/scoring_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()


def score_candidate(parsed, vacancy):
    prompt_template = load_prompt()

    data = {
        "parsed": parsed,
        "vacancy": vacancy
    }

    prompt = prompt_template.replace(
        "{{data}}",
        json.dumps(data, ensure_ascii=False)
    )

    response = ask_llm(prompt)

    return extract_json(response)