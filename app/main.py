from fastapi import FastAPI, Query
from dotenv import load_dotenv
from app.router import router
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin as fa
from config.config import get_settings
load_dotenv()
app = FastAPI()
app.include_router(router)
fa.initialize_app()

settings = get_settings()

origin=[settings.frontend_url, "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_method=["*"],
    allow_headers=["*"],
)