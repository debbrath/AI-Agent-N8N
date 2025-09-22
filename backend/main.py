
import uuid
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path



# Define input model
class ArticleRequest(BaseModel):
    email: str
    article_url: str

app = FastAPI()


# Allow frontend (lovable app) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to frontend folder
FRONTEND_DIR = Path(__file__).parent.parent / "frontend"

print("Frontend directory resolved to:", FRONTEND_DIR.resolve())

# Serve /index.html
@app.get("/", response_class=FileResponse)
def serve_index():
    return FRONTEND_DIR / "index.html"

# Serve other static files (CSS, JS)
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# Replace with your n8n webhook URL
N8N_WEBHOOK_URL = "https://ddnath2001.app.n8n.cloud/webhook-test/6f5bca51-eb77-4830-8d61-f69e3226d04d"

@app.post("/submit")
def submit_article(data: ArticleRequest):
    print("Received data:", data.dict())
    session_id = str(uuid.uuid4())
    payload = {
        "email": data.email,
        "article_url": data.article_url,
        "session_id": session_id
    }

    try:
        response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=10)
        print("n8n status:", response.status_code)
        print("n8n response:", response.text)
        response.raise_for_status()
    except Exception as e:
        return {"status": "error", "message": f"Failed to reach n8n: {e}"}

    return {"status": "success", "message": "Data forwarded to n8n", "session_id": session_id}