from fastapi import APIRouter, Depends
from services.chat_service import ChatService
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/")
async def root():
    """
    Check if the API is running.
    
    Returns:
    
        dict: A status message indicating the API is online
    """
    
    return {"message": "Welcome to the Agri ChatBot API!"}

        
    
    
 
 
