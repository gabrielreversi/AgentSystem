import fastapi
from fastapi import FastAPI
from src.api.routes.api_route import router as agent_input_router

app = FastAPI()

app.include_router(agent_input_router, prefix='/input', tags=['user_input & upload_file'])