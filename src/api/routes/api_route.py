import fastapi
from fastapi import APIRouter, status
from fastapi import UploadFile, File
from fastapi import APIRouter, status
from pydantic import BaseModel

from src.agents.pipeline import app
from src.agents.state import AgentSQLstate

router = APIRouter()

@router.post("/upload_file/", status_code=status.HTTP_200_OK)
async def upload_file(file: list[UploadFile] = File(...)):
    return {"status":"sent!!"}

class QuestionRequest(BaseModel):
    question: str


@router.post("/get_answer/", status_code=status.HTTP_200_OK)
async def question(payload: QuestionRequest):

    initial_state: AgentSQLstate = {
        "question": payload.question,
        "sql_query": None,
        "sql_result": None,
        "answer": None,
        "error": None,
    }

    result = app.invoke(initial_state)

    if result.get("error"):
        return {
            "error": result["error"]
        }

    return {
        "question": payload.question,
        "sql_query": result["sql_query"],
        "sql_result": result["sql_result"],
        "answer": result["answer"],
    }