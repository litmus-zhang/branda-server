from fastapi import FastAPI, Query
from dotenv import load_dotenv
import os
from app.router import router
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin as fa
from firebase_admin import storage
from config.config import get_settings
load_dotenv()
app = FastAPI()
app.include_router(router)

origin=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_headers=["*"],
)