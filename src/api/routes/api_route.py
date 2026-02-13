import fastapi
from fastapi import APIRouter, status
from fastapi import UploadFile, File
from fastapi import APIRouter, status
from pydantic import BaseModel
import uuid

from src.agents.pipeline import app
from src.agents.state import AgentSQLstate

router = APIRouter()

@router.post("/upload_file/", status_code=status.HTTP_200_OK)
async def upload_file(file: list[UploadFile] = File(...)):
    return {"status":"sent!!"}

class QuestionRequest(BaseModel):
    question: str
    session_id: str | None = None


@router.post("/get_answer/", status_code=status.HTTP_200_OK)
async def question(payload: QuestionRequest):

    session_id = payload.session_id or str(uuid.uuid4())

    initial_state: AgentSQLstate = {
        "question": payload.question,
        "sql_query": None,
        "sql_result": None,
        "answer": None,
        "error": None,
    }

    result = app.invoke(
        initial_state,
        config={"configurable": {"thread_id": session_id}},
    )

    if result.get("error"):
        return {
            "error": result["error"],
            "session_id": session_id
        }

    return {
        "session_id": session_id,
        "question": payload.question,
        "sql_query": result["sql_query"],
        "sql_result": result["sql_result"],
        "answer": result["answer"],
    }