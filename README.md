# LM Studio FastAPI Wrapper

A FastAPI-based REST API that wraps [LM Studio](https://lmstudio.ai/)'s local server, allowing you to interact with local language models through a clean HTTP API.

## Features

- 🚀 Simple `/ask` endpoint to chat with local AI models
- 📋 `/models` endpoint to list available models
- ✅ Request/response validation with Pydantic
- 🏗️ Clean project structure following industry best practices
- 🔄 Async HTTP client for efficient communication

## Prerequisites

- Python 3.9+
- [LM Studio](https://lmstudio.ai/) installed and running
- A loaded model in LM Studio (e.g., llama-3.2-1b-instruct)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd fastapi-lmstudio
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start LM Studio:**
   - Open LM Studio
   - Load a model (e.g., llama-3.2-1b-instruct)
   - Go to the "Local Server" tab
   - Click "Start Server" (default: http://127.0.0.1:1234)

## Usage

### Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### Interactive API docs

Open your browser and visit:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### Example requests

#### Ask the AI a question

**Request:**
```bash
curl -X POST "http://127.0.0.1:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is FastAPI?"}'
```

**Response:**
```json
{
  "answer": "FastAPI is a modern, fast web framework for building APIs with Python..."
}
```

#### List available models

**Request:**
```bash
curl "http://127.0.0.1:8000/models"
```

**Response:**
```json
{
  "data": [
    {
      "id": "llama-3.2-1b-instruct",
      "object": "model"
    }
  ]
}
```

## Project Structure

```
fastapi-lmstudio/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Configuration settings
│   ├── models/
│   │   └── schemas.py       # Pydantic models
│   ├── routers/
│   │   └── chat.py          # API endpoints
│   └── services/
│       └── lmstudio.py      # LM Studio communication logic
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Configuration

Edit `app/config.py` to customize:

- `LM_STUDIO_BASE_URL` — LM Studio server URL (default: `http://127.0.0.1:1234`)
- `DEFAULT_MODEL` — Model to use (default: `llama-3.2-1b-instruct`)
- `DEFAULT_TEMPERATURE` — Response randomness (default: `0.7`)
- `DEFAULT_MAX_TOKENS` — Max response length (default: `-1` for unlimited)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/models` | List available LM Studio models |
| POST | `/ask` | Send a prompt and get AI response |

### `/ask` Request Body

```json
{
  "prompt": "Your question here"
}
```

### `/ask` Response

```json
{
  "answer": "AI-generated response"
}
```

## Troubleshooting

### Connection refused error
- **Problem:** `Cannot connect to LM Studio: Connection refused`
- **Solution:** Make sure LM Studio's local server is running on port 1234

### Model not loaded
- **Problem:** `LM Studio error: No model loaded`
- **Solution:** Load a model in LM Studio before starting the FastAPI server

### Import errors
- **Problem:** `ModuleNotFoundError: No module named 'app'`
- **Solution:** Run `uvicorn app.main:app --reload` from the project root directory (where `app/` folder is)

## Development

### Running tests (future)
```bash
pytest
```

### Code formatting (recommended)
```bash
pip install black
black app/
```

## License

MIT License

## Author

Arun Praseeth - Learning FastAPI with LM Studio

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LM Studio](https://lmstudio.ai/)
- [Pydantic](https://docs.pydantic.dev/)
- [HTTPX](https://www.python-httpx.org/)
