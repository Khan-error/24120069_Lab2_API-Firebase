# 🤖 Mika Chat

Ứng dụng chatbot AI sử dụng **Streamlit** + **FastAPI** + **Groq (LLaMA 3.1)** + **Firebase**.

## ✨ Tính năng

- 💬 Chat với AI (Groq LLaMA 3.1 8B)
- 🔐 Đăng nhập bằng Email hoặc Google OAuth
- 🗄️ Lưu lịch sử chat trên Firebase Firestore

## 📁 Cấu trúc

```
chatbot-page/
├── backend/app/
│   ├── main.py              # FastAPI entry point
│   ├── core/                # Firebase config
│   ├── routers/             # auth.py, chat.py
│   ├── schemas/             # Pydantic models
│   ├── services/            # Groq AI, Firestore
│   └── dependencies/        # JWT auth
├── frontend/
│   ├── app.py               # Streamlit entry point
│   └── api_client.py        # Gọi API backend
├── .streamlit/secrets.toml  # Cấu hình Firebase & OAuth
└── requirements.txt
```

## 🛠️ Cài đặt

```bash
git clone https://github.com/Khoan-IT/chatbot-page.git
cd chatbot-page
python -m venv venv
.\venv\Scripts\Activate        # Windows
pip install -r requirements.txt
```

Cấu hình `.streamlit/secrets.toml` với Firebase Client, Admin SDK và Google OAuth credentials.

## ▶️ Chạy

> Chạy **Backend trước**, sau đó mới chạy Frontend.

**Terminal 1 — Backend:**

```powershell
.\venv\Scripts\Activate
uvicorn backend.app.main:app --reload --port 8000
```

**Terminal 2 — Frontend:**

```powershell
.\venv\Scripts\Activate
python -m streamlit run frontend/app.py
```

| Service  | URL                          |
| -------- | ---------------------------- |
| Frontend | http://localhost:8501         |
| Backend  | http://localhost:8000         |
| API Docs | http://localhost:8000/docs    |

## 🧰 Tech Stack

| Thành phần | Công nghệ                  |
| ---------- | --------------------------- |
| Frontend   | Streamlit                   |
| Backend    | FastAPI + Uvicorn           |
| AI Model   | Groq — LLaMA 3.1 8B        |
| Auth       | Firebase Auth + Google OAuth|
| Database   | Firebase Firestore          |
