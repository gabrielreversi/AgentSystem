import fastapi
from fastapi import APIRouter, status
from fastapi import UploadFile, File

router = APIRouter()

@router.post("/get_answer/", status_code=status.HTTP_200_OK)
async def question(input: str):
    return {"answer":"hello world"}

@router.post("/upload_file/", status_code=status.HTTP_200_OK)
async def upload_file(file: list[UploadFile] = File(...)):
    return {"status":"sent!!"}

