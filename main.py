"""FastAPI application entry point."""
from fastapi import FastAPI

from routers import chat

app = FastAPI(
    title="LM Studio API",
    description="FastAPI wrapper for LM Studio local server",
    version="1.0.0"
)

# Include routers
app.include_router(chat.router, tags=["chat"])


@app.get("/")
async def root():
    """Health check endpoint."""
    return {"status": "running", "message": "LM Studio FastAPI server"}




# #Creates the FastAPI app and includes routers for handling AI model interactions.

# import httpx
# from typing import List
# from pydantic import BaseModel, Field
# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# base_url = 'http://127.0.0.1:1234'
# getModels_url = f'{base_url}/v1/models'
# post_url = f'{base_url}/v1/chat/completions'

# DEFAULT_MODEL = "llama-3.2-1b-instruct"
# DEFAULT_TEMPERATURE = 0.7
# DEFAULT_MAX_TOKENS = -1
# DEFAULT_STREAM = False

# class AskRequest(BaseModel):
#     prompt: str = Field(..., description="This is the user's input prompt.")

# class AskResponse(BaseModel):
#     prompt: str

# class ChatMessage(BaseModel):
#     role: str = "user"
#     content: str

# class LMStudioRequest(BaseModel):
#     model: str = Field(default="llama-3.2-1b-instruct", description="This is the AI model in use.")
#     temperature: float = Field(default=0.7, description="Sampling temperature.")
#     max_tokens: int = Field(default=-1, description="Maximum tokens to generate.")
#     stream: bool = Field(default=False, description="Whether to stream the response.")
#     messages: List[ChatMessage]

# @app.get("/models")
# async def get_models():
#     async with httpx.AsyncClient() as client:
#         response = await client.get(f"{getModels_url}")
#         return response.json()

# @app.post("/ask", response_model= AskResponse)
# async def ask_ai(askreq: AskRequest):
#     lm_payload = LMStudioRequest(
#         model=DEFAULT_MODEL,
#         temperature=DEFAULT_TEMPERATURE,
#         stream=DEFAULT_STREAM,
#         max_tokens=DEFAULT_MAX_TOKENS,
#         messages= [ChatMessage(role="user", content=askreq.prompt)]
#     ).model_dump(exclude_none=True)

#     try:
#         async with httpx.AsyncClient(timeout=30.0) as client:
#             response = await client.post(f"{post_url}", json=lm_payload)
#             response.raise_for_status()
#     except httpx.HTTPError as e:
#         raise HTTPException(status_code=e.response.status_code, detail=str(e))
    
#     lm_response = response.json()
#     return AskResponse(prompt=lm_response['choices'][0]['message']['content'])