from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}

@app.get("/api")
def api_root():
    return {"message": "API endpoint works!"}

class Problem(BaseModel):
    question: str

@app.post("/solve")
def solve_math(problem: Problem):
    payload = {
        "model": "hf.co/allenai/OLMo-2-0425-1B-Instruct-GGUF:Q4_K_M",
        "prompt": f"Solve this math problem step-by-step:\n{problem.question}"
    }

    response = requests.post("http://localhost:11434/api/generate",json=payload,stream=True)

    full_output = ""

    for line in response.iter_lines():
        if line:
            obj = json.loads(line.decode("utf-8"))
            full_output += obj.get("response","")

    return {"answer": full_output}