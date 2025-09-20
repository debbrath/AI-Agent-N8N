Project structure:

ai-agent-n8n/
├─ frontend/
│  └─ index.html
├─ backend/
│  └─ app.py
├─ n8n-workflow/
│  └─ workflow.json
├─ requirements.txt


PS F:\Python\AI-Agent-N8N> cd F:\Python\AI-Agent-N8N\backend
(venv) PS F:\Python\AI-Agent-N8N\backend> python main.py




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


