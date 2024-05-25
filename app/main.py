from fastapi import FastAPI, Query
from dotenv import load_dotenv
from app.router import router
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin as fa
from strawberry.fastapi import GraphQLRouter
from models.graphql import schema
from config.config import get_settings
load_dotenv()
app = FastAPI()
app.include_router(router)
fa.initialize_app()

graphql_app = GraphQLRouter(schema=schema, graphql_ide="apollo-sandbox")
app.include_router(graphql_app, prefix="/graphql")

settings = get_settings()

origin=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)