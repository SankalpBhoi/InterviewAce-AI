from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.auth import router as auth_router
from app.database.database import db
from app.routers import resume


app = FastAPI(
    title="InterviewAce AI API",
    version="1.0.0"
)

app.include_router(auth_router)

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "InterviewAce AI Backend is Running 🚀"
    }

@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "database": db.name
    }
    
app.include_router(resume.router)