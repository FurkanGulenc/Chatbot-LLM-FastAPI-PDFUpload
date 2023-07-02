from typing import Union
from typing import List

from fastapi import FastAPI, File, UploadFile, Body, Depends
from pydantic import BaseModel


from src import ConversationalRetrievialChain

import os

if not os.path.exists("/Users/furkangulenc/Desktop/FastApi/uploads"):
    os.makedirs("/Users/furkangulenc/Desktop/FastApi/uploads")

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    save_path = "/Users/furkangulenc/Desktop/FastApi/uploads/" + file.filename
    with open(save_path, "wb") as f:
        f.write(await file.read())

    ConversationalRetrievialChain.vector_store.vectorstore = (
        ConversationalRetrievialChain.split_pdf_add_db(save_path)
    )
    print("-----------")
    print(ConversationalRetrievialChain.vector_store.vectorstore)
    print("-----------")
    return {"message": "PDF uploaded successfully."}


@app.post("/question")
def question(question_request: QuestionRequest):
    print("Received Question:", question_request.question)

    result = ConversationalRetrievialChain.answer_question(question_request.dict())

    return {"message": "Question received successfully.", "result": result}
