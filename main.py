from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Simple API server")
# need to allow cross-origin requests (but limit just to localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="http://localhost.*",
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "message": "Hello world!"}

class AdditionModel(BaseModel):
    num1: float
    num2: float

@app.post("/add/")
def add_numbers(numbers: AdditionModel):
    num1 = numbers.num1
    num2 = numbers.num2
    return {"status": "ok", "result": num1 + num2}
