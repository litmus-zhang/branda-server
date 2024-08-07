from fastapi import FastAPI
from dotenv import load_dotenv
from routes.router import router
from fastapi.middleware.cors import CORSMiddleware
from models import models
from config.database import engine

models.Base.metadata.create_all(bind=engine)
load_dotenv()
app = FastAPI()
app.include_router(router, prefix="/api/v1")
origin = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://branda.vercel.app",
    "https://branda-admin.vercel.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
