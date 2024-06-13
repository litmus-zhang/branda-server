from fastapi import FastAPI
from dotenv import load_dotenv
from app.router import router
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()
app.include_router(router, prefix="/api/v1")
origin=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_headers=["*"],
)