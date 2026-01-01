#Pydantic models (request/response shapes) for FastAPI app.

"""Pydantic models for request/response validation."""
from typing import List
from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    """Request model for /ask endpoint."""
    prompt: str = Field(..., min_length=1, description="User's input prompt")


class AskResponse(BaseModel):
    """Response model for /ask endpoint."""
    answer: str


class ChatMessage(BaseModel):
    """Single chat message for LM Studio API."""
    role: str = "user"
    content: str

class LMStudioRequest(BaseModel):
    model: str = Field(default="llama-3.2-1b-instruct", description="This is the AI model in use.")
    temperature: float = Field(default=0.7, description="Sampling temperature.")
    max_tokens: int = Field(default=-1, description="Maximum tokens to generate.")
    stream: bool = Field(default=False, description="Whether to stream the response.")
    messages: List[ChatMessage]