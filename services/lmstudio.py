#Business logic (talk to LM Studio, process data)

"""Service layer for LM Studio API communication."""
import httpx
from fastapi import HTTPException
from models.schemas import ChatMessage, LMStudioRequest

from config import (
    LM_STUDIO_MODELS_URL,
    LM_STUDIO_CHAT_URL,
    REQUEST_TIMEOUT,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS,
    DEFAULT_STREAM,
)


async def get_available_models():
    """Fetch available models from LM Studio."""
    async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
        response = await client.get(LM_STUDIO_MODELS_URL)
        response.raise_for_status()
        return response.json()


async def generate_response(prompt: str) -> str:
    cleaned_prompt = prompt.replace("\\'", "'").replace("\\", "")
    """
    Generate AI response from LM Studio.
    
    Args:
        prompt: User's input text
        
    Returns:
        AI-generated response text
    """
    # Build payload
    lm_payload = LMStudioRequest(
        model=DEFAULT_MODEL,
        temperature=DEFAULT_TEMPERATURE,
        max_tokens=DEFAULT_MAX_TOKENS,
        stream=DEFAULT_STREAM,
        messages=[ChatMessage(role="user", content=cleaned_prompt)]
    ).model_dump(exclude_none=True)

    # Send request
    try:
        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            response = await client.post(LM_STUDIO_CHAT_URL, json=lm_payload)
            response.raise_for_status()

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"LM Studio error: {e.response.text}"
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Cannot connect to LM Studio: {str(e)}"
        )

    # Extract response
    data = response.json()
    return data["choices"][0]["message"]["content"]
