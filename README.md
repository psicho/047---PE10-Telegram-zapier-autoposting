# Авто-генерация постов с использованием OpenAI и Currents API

Этот сервис реализован на FastAPI и предназначен для генерации блоговых постов и статей с помощью GPT-4/OpenAI и использования новостных данных от Currents API.

## Возможности
- Генерирует уникальный заголовок, мета-описание и статью по теме с учетом свежих новостей.
- REST API для подачі темы и получения сгенерированного контента.

---

## Быстрый старт

### 1. Клонирование и подготовка среды
```bash
git clone <repo-url>
cd <project-folder>
python -m venv .venv
source .venv/bin/activate  # или .venv\Scripts\activate в Windows
pip install -r requirements.txt
```

### 2. Добавьте файл `.env` в корень проекта:
```
OPENAI_API_KEY=sk-ваш-openai-ключ
CURRENTS_API_KEY=ваш-ключ-currentsapi
OPENAI_BASE_URL=https://api.proxyapi.ru/openai/v1  # по желанию
PORT=8000  # по желанию
```

### 3. Запуск локально
```bash
python app.py
# или через uvicorn
uvicorn app:app --reload
```

### 4. Запуск через Docker и Docker Compose
```bash
docker-compose up --build
```

Сервис будет доступен на http://localhost:8000

---
## Эндпоинты

### `POST /generate-post`
**Параметры:**
```json
{
  "topic": "Ваша тема для статьи"
}
```
**Ответ:**
```json
{
  "title": "...",
  "meta_description": "...",
  "post_content": "..."
}
```

### `GET /`
Проверка статуса сервиса.

### `GET /heartbeat`
Проверка статуса (возвращает {"status": "OK"}).

---
## Используемые переменные среды
- `OPENAI_API_KEY` — API-ключ OpenAI, обязательное поле.
- `OPENAI_BASE_URL` — (опционально) базовый адрес API, по умолчанию https://api.proxyapi.ru/openai/v1
- `CURRENTS_API_KEY` — API-ключ Currents API, обязательное поле.
- `PORT` — порт запуска сервера (по умолчанию 8000).

---
## Зависимости

Они указаны в requirements.txt и автоматически собираются при сборке Docker-образа.

---

## Лицензия
Проект для учебных/демонстрационных целей.
