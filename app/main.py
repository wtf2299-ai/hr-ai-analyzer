from fastapi import FastAPI, Form
from app.services.parser import parse_transcript
from app.services.scoring import score_candidate

app = FastAPI()

def clean_text(text: str) -> str:
    # убираем проблемные символы
    text = text.replace("\r\n", " ")
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\t", " ")
    text = text.replace("\xa0", " ")
    # убираем двойные пробелы
    while "  " in text:
        text = text.replace("  ", " ")
    return text.strip()

@app.post("/analyze")
def analyze(data: dict):
    transcript = clean_text(data.get("transcript", ""))
    vacancy = clean_text(data.get("vacancy", ""))
    parsed = parse_transcript(transcript)
    scoring = score_candidate(parsed, vacancy)
    return {"parsed": parsed, "scoring": scoring}

@app.post("/analyze-form")
def analyze_form(
    transcript: str = Form(...),
    vacancy: str = Form(default="")
):
    parsed = parse_transcript(clean_text(transcript))
    scoring = score_candidate(parsed, clean_text(vacancy))
    return {"parsed": parsed, "scoring": scoring}