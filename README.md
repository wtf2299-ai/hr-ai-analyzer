# HR AI Analyzer

Инструмент для автоматического анализа текстовых транскриптов собеседований с помощью локальной языковой модели.

## Что делает

- Парсит транскрипт интервью и извлекает вопросы, ответы и факты
- Оценивает кандидата по hard skills, коммуникации и культурному соответствию
- Формирует итоговый вывод с рекомендацией на русском языке
- Работает полностью локально через Ollama без внешних API

## Технологии

- Python 3.11
- FastAPI
- Ollama (llama3)
- Swagger UI для тестирования

## Запуск

1. Установи зависимости: pip install -r requirements.txt
2. Запусти Ollama с моделью llama3: ollama run llama3
3. Запусти сервер: python -m uvicorn app.main:app --reload
4. Открой браузер: `http://127.0.0.1:8000/docs`

## Эндпоинты

- `POST /analyze` - анализ через JSON
- `POST /analyze-form` - анализ через форму (удобно для длинных текстов)

## Пример ответа

```json
{
  "parsed": {
    "qa_items": [...],
    "facts": [...]
  },
  "scoring": {
    "scores": {
      "hard_skills": {"value": 7, "rationale": "..."},
      "communication": {"value": 8, "rationale": "..."}
    },
    "recommendation": {"decision": "Рекомендуем"},
    "summary": "Итоговый вывод по кандидату..."
  }
}
```
