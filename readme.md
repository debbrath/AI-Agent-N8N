Project structure:


📂 Project Structure (Initial Setup)
ai-agent-n8n/
│
├── frontend/        # Lovable frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/         # FastAPI backend (will add later)
│   └── main.py
│
└── README.md


Run:

pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000




