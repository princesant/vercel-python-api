from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load student marks
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = Query([])):
    marks = [data.get(n, None) for n in name]
    return {"marks": marks}
