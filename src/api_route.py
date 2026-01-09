import fastapi
from fastapi import APIRouter, status, HTTPException
from fastapi import UploadFile, File

router = APIRouter()

@router.post('/question/', status_code=status.HTTP_200_OK)
async def question_user(question: str):
    return {"answer": "hello world"}

@router.post("/upload/", status_code=status.HTTP_200_OK)
async def upload_file(file: list[UploadFile] = File(...)):
    return {"status": "test"}

@router.post("/insert_data/", status_code=status.HTTP_200_OK)
async def insert_data(data1: str, data2: float):
    pass

@router.delete("/delete_data/")
async def delete_data(id:str):
    pass