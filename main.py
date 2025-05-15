from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chat_route, root_route
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Agri ChatBot API",
    
    description="""
    This API allows you to answer farmers agriculture related question.
    
    ## Features
    
    * Answering questions related to agriculture
    
    """,
    version="1.0.0",
    license_info={
        "name": "Private",
    },
    openapi_tags=[
        {
            "name": "Health",
            "description": "API health checking operations",
        },
        {
            "name": "Chat",
            "description": "Answering questions related to agriculture",
        }
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root_route.router, tags=["Health"])
app.include_router(chat_route.router, tags=["Chat"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)