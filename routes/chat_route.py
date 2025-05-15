from fastapi import APIRouter, Depends
from models.chat import ChatMessage
from services.chat_service import ChatService
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/chat")
async def chat(
    chat_message: ChatMessage,
    chat_service: ChatService = Depends()
):
    """
    Send farmer query to llm process it and return the response.
    
    Args:
    
        query: User query to be sent to the llm.
        
    Returns:
    
        json: Response from the llm.
        
    Raises:
    
        HTTPException: If anything goes wrong.
    """
    
    response = chat_service.chat(chat_message.content)
    return {"response": response}

        
    
   