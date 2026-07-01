from fastapi import FastAPI
from app.chatbot.chatbot import SHLChatbot
from app.models.schemas import ChatRequest

app = FastAPI(
    title="SHL Assessment Recommendation API"
)

chatbot = SHLChatbot()


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    messages = [
        message.model_dump()
        for message in request.messages
    ]

    return chatbot.chat(messages)