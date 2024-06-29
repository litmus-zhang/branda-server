from fastapi import FastAPI
from dotenv import load_dotenv
from routes.router import router
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import models
from config.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
load_dotenv()
app = FastAPI()
app.include_router(router, prefix="/api/v1")
origin = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_headers=["*"],
)
