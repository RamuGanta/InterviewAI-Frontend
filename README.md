# InterviewAI Frontend

Interactive web interface for the **InterviewAI** mock interview platform. Built with **Streamlit**, this app connects to the [InterviewAI Backend](https://github.com/RamuGanta/InterviewAI-Backend) to deliver AI-powered interview practice with real-time feedback.

**Live App:** [interviewai-fastapi-ramu.streamlit.app](https://interviewai-fastapi-ramu.streamlit.app)
**Backend Repo:** [InterviewAI-Backend](https://github.com/RamuGanta/InterviewAI-Backend)

---

## How It Works

```
User fills profile form
        │
        ▼
Streamlit sends POST /start_interview to FastAPI backend
        │
        ▼
Backend generates AI interview question (OpenAI GPT-4)
        │
        ▼
User answers in chat → follow-up questions → feedback & scoring
```

### Interview Flow

1. **Setup** — Enter your name, experience, skills, desired position, and target company
2. **Interview** — Chat with the AI interviewer who asks role-specific questions and follow-ups
3. **Feedback** — Receive a performance score (1–10) with detailed strengths and improvement areas

---

## Features

- Personalized interview questions based on your profile, skills, and experience level
- Support for multiple roles: Data Scientist, Data Engineer, ML Engineer, BI Analyst, Financial Analyst
- Target company selection: Amazon, Meta, LinkedIn, Spotify, and more
- Real-time chat interface with streaming AI responses
- End-of-interview feedback with scoring and actionable suggestions

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| UI Framework | Streamlit |
| Backend Communication | REST API (requests) |
| Deployment | Streamlit Community Cloud |
| Backend | FastAPI ([separate repo](https://github.com/RamuGanta/InterviewAI-Backend)) |

---

## Project Structure

```
InterviewAI-Frontend/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── .gitignore
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- The [InterviewAI Backend](https://github.com/RamuGanta/InterviewAI-Backend) running locally or deployed

### Local Setup

1. **Clone the repo:**

```bash
git clone https://github.com/RamuGanta/InterviewAI-Frontend.git
cd InterviewAI-Frontend
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure backend URL:**

In `app.py`, update the API base URL to point to your backend:

```python
# For local development:
API_BASE_URL = "http://localhost:8000"

# For production (already configured):
API_BASE_URL = "https://interviewai-backend-z8rg.onrender.com"
```

4. **Run the app:**

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Deployment

Deployed on **Streamlit Community Cloud** with the following configuration:

| Setting | Value |
|---------|-------|
| Repository | `RamuGanta/InterviewAI-Frontend` |
| Branch | `main` |
| Main file | `app.py` |

The frontend contains no secrets or API keys — all sensitive operations are handled by the backend.

---

## System Architecture

This is the frontend half of a two-repo architecture:

```
┌──────────────────────┐       REST API        ┌──────────────────────┐
│                      │ ───────────────────►   │                      │
│  Streamlit Frontend  │                        │   FastAPI Backend    │
│  (this repo)         │ ◄───────────────────   │   (separate repo)   │
│                      │     JSON responses     │                      │
│  Streamlit Cloud     │                        │   Render (Docker)    │
└──────────────────────┘                        └──────────┬───────────┘
                                                           │
                                                     OpenAI GPT-4
```

**Why two repos?** Separating frontend and backend allows independent deployment, scaling, and technology choices. The backend can be swapped or upgraded without touching the UI, and vice versa.

---

## Related

- **Backend:** [InterviewAI-Backend](https://github.com/RamuGanta/InterviewAI-Backend) — FastAPI service with OpenAI integration and session management
- **Earlier Prototype:** [Interview-and-Feedback-tool](https://github.com/RamuGanta/Interview-and-Feedback-tool) — Single-file version combining UI and AI logic in one Streamlit app

---

## Author

**Ramu Ganta** — [LinkedIn](https://www.linkedin.com/in/ramgan333729/) · [GitHub](https://github.com/RamuGanta)
