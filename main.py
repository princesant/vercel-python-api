from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

# Load the student data from the JSON file
with open("q-vercel-python.json", "r") as file:
    student_data = json.load(file)

app = FastAPI()

# Enable CORS (Allows requests from any website)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def get_marks(name: list[str] = Query([])):
    marks = [student_data.get(n, None) for n in name]
    return {"marks": marks}
