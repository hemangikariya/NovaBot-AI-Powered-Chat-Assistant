# 🤖 NovaBot — AI-Powered Chat Assistant

NovaBot is a full-stack AI-powered chatbot built using **React (frontend)** and **Flask (backend)**. It can help users with information related to MCA, admissions, AI/ML career, placements, and more.

---

## 🧠 Features

- 📚 Contextual responses for MCA-related queries  
- 🔍 Keyword-based natural language understanding  
- 📝 Feedback logging system  
- 🎨 Responsive chat UI (React)  
- 🐍 Backend logic in Python with Flask  
- 🌐 CORS-enabled API for frontend-backend communication

---

## 📁 Project Structure
```bash
project-root/
├── backend/ # Flask backend
│ ├── app.py
│ ├── chatbot_logic.py
│ ├── feedback_log.json
│ ├── requirements.txt
│ └── Procfile
│
├── frontend/ # React frontend
│ ├── public/
│ ├── src/
│ ├── package.json
│ └── .env # contains REACT_APP_BACKEND_URL
│
└── README.md
```

## 🧠 Tech Stack

| Layer     | Tech Used            |
|-----------|----------------------|
| Frontend  | React.js             |
| Backend   | Python (Flask)       |
| Styling   | CSS Modules          |
| Communication | REST API + fetch |
| Logging   | JSON file logging    |

---

## 📦 How It Works

1. **User interacts** via a friendly chatbot interface.
2. Frontend sends input to backend via API (`/chat` endpoint).
3. Backend processes input using `chatbot_logic.py`.
4. Returns meaningful replies with optional options/buttons.
5. Feedback (`Yes/No`) is logged in `feedback_log.json`.

---

## 📊 Feedback Logging Format

Responses are saved in this structure:

```json
[
  {
    "topic": "placement",
    "feedback": "yes",
    "timestamp": "2025-07-03T18:30:00"
  }
]
```

---

## 👩‍💻 Author

Made by Hemangi 💻✨
👩‍💻 Connect with me on [LinkedIn](https://linkedin.com/in/hemangikariya) 

