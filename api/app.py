import os
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key
load_dotenv()
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Init FastAPI
app = FastAPI()

# Allow CORS (for frontend or testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Init Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.4,
    max_tokens=2048,
    timeout=60,
)

@app.post("/chat/")
def chat(question: str = Form(...)):
    messages = [
        ("system", "You are a helpful assistant. Answer clearly."),
        ("human", question),
    ]
    response = llm.invoke(messages)
    return {"answer": response.content}
