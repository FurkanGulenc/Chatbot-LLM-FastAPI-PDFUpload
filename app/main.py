from typing import Union
from typing import List

from fastapi import FastAPI, File, UploadFile, Body, Depends
from pydantic import BaseModel


from src import ConversationalRetrievialChain

import os

# Creating upload folder for saving pdf uploads
if not os.path.exists("/Users/furkangulenc/Desktop/FastApi/uploads"):
    os.makedirs("/Users/furkangulenc/Desktop/FastApi/uploads")

app = FastAPI()

 
class QuestionRequest(BaseModel):
    question: str


@app.post("/upload-pdf") # Upload, Save and Process PDF file with using split_pdf_add_db function
async def upload_pdf(file: UploadFile = File(...)):
    save_path = "/Users/furkangulenc/Desktop/FastApi/uploads/" + file.filename
    with open(save_path, "wb") as f:
        f.write(await file.read()) # Take PDF file and read

    #split chunks, embed chunks, store chroma db as persistence
    ConversationalRetrievialChain.vector_store.vectorstore = (
        ConversationalRetrievialChain.split_pdf_add_db(save_path)
    )
    
    print(ConversationalRetrievialChain.vector_store.vectorstore)
    
    return {"message": "PDF uploaded successfully."}


@app.post("/question") # Take and embed question and answer from pdf  with using answer_question function
def question(question_request: QuestionRequest):
    print("Received Question:", question_request.question)

    # similarity search, ask openai, give answer
    result = ConversationalRetrievialChain.answer_question(question_request.dict())

    return {"message": "Question received successfully.", "result": result}
