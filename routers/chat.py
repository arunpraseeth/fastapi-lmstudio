#API endpoints (your @app.get and @app.post functions) for handling chat requests.

"""API endpoints for chat functionality."""
from fastapi import APIRouter

from models.schemas import AskRequest, AskResponse
from services.lmstudio import get_available_models, generate_response

router = APIRouter()


@router.get("/models")
async def list_models():
    """Get available LM Studio models."""
    return await get_available_models()


@router.post("/ask", response_model=AskResponse)
async def ask_ai(request: AskRequest):
    """
    Ask the AI a question.
    
    Args:
        request: User prompt
        
    Returns:
        AI-generated answer
    """
    answer = await generate_response(request.prompt)
    return AskResponse(answer=answer)
