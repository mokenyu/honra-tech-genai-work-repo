from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import chatPromptTemplate

load_dotenv()

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

prompt = chatPromptTemplate.from_messages([
    (
        "Kewir system"
        """ Your name is Kewir and you are an AI and also a technology assistant. You answer questions about web developement
        ,datascience and cybersecurity and also about solarsystem.
        Keep your answer clear and helpful. if the user asks something else, carefully tell them that you are not programmed to anser that."""
    ),
    ("human", "{message}")
])
@app.get("/")
def home():
    return {"message": "Kewirs LangChain API is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    response = chain.invoke([
        HumanMessage(content=request.message)
    ])

    return {
        "response": response.content
    }