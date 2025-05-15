import logging
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage


logger = logging.getLogger(__name__)

class ChatService:
    def __init__(self):
        self.llm = ChatGroq(
            model="deepseek-r1-distill-llama-70b",
            temperature=0.6,
        )
        self.system_message = SystemMessage(content="""You are a llm specialized in answering qustions related about farming.
                                          You should give answer to any agricultural question in simple language that is easy to understand even for farmers.
                                          """)
        
    def chat(self, message: str) -> str:
        
        messages = [
            self.system_message,
            HumanMessage(content=message)
        ]

        # Get the response from the model
        return self.parse_llm_response(self.llm.invoke(messages))
    
    def parse_llm_response(self, llm_response: str) -> str:
        return llm_response.content.split("</think>")[-1]