# SHL AI Assessment Recommendation Chatbot

## Overview

The SHL AI Assessment Recommendation Chatbot is an intelligent recommendation system that helps recruiters identify suitable SHL assessments based on job requirements. The chatbot uses Google's Gemini Large Language Model (LLM) together with the SHL Product Catalog to understand recruiter queries, ask clarification questions, and recommend relevant assessments.

The application is developed using FastAPI and deployed on Render.

---

## Features

- AI-powered conversational chatbot using Google Gemini
- SHL assessment recommendation based on recruiter requirements
- Clarification questions for incomplete user input
- Intelligent recommendation ranking
- Comparison support for SHL assessments
- REST API using FastAPI
- Live deployment on Render

---

## Technology Stack

- Python 3.14
- FastAPI
- Google Gemini API (google-genai)
- Uvicorn
- JSON
- Git & GitHub
- Render

---

## Project Structure

```
SHL-AI-Assessment-Recommender/
│
├── app/
│   ├── catalog/
│   ├── chatbot/
│   ├── conversation/
│   ├── llm/
│   ├── models/
│   ├── recommender/
│   └── main.py
│
├── data/
│   └── shl_product_catalog.json
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/manojkumar2306/SHL-AI-Assessment-Recommender.git
```

Move into the project directory

```bash
cd SHL-AI-Assessment-Recommender
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
python -m uvicorn app.main:app --reload
```

---

## API Endpoints

### Home

```
GET /
```

### Health Check

```
GET /health
```

### Chat

```
POST /chat
```

Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I need a Python assessment for a Software Engineer."
    }
  ]
}
```

---

## Live Demo

Render Deployment

https://shl-ai-assessment-recommender-5mvy.onrender.com

Swagger API Documentation

https://shl-ai-assessment-recommender-5mvy.onrender.com/docs

---

## GitHub Repository

https://github.com/manojkumar2306/SHL-AI-Assessment-Recommender

---

## Future Improvements

- Semantic search using embeddings
- Multi-turn conversation memory
- Streamlit or React frontend
- Better ranking using vector similarity
- Authentication and user sessions

---

## Author

Manoj Kumar M

Bachelor of Engineering (Electronics and Communication Engineering)
