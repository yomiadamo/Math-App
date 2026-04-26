# Math-App

A lightweight AI-powered math problem solver built with FastAPI and a locally hosted large language model (LLM) via Ollama. This project explores how LLMs can be integrated into backend API services to handle natural language math queries and return structured solutions.

---

## Purpose

Traditional math solvers rely on symbolic computation engines. This project investigates an alternative approach: routing natural language math problems through a locally running LLM (OLMo 2 1B) and serving the results via a REST API. The goal was to evaluate the feasibility of using small, locally hosted models for domain-specific reasoning tasks without relying on cloud-based APIs.

---

## Technologies Used

| Technology | Role |
|---|---|
| Python | Core language |
| FastAPI | REST API framework |
| Ollama | Local LLM inference engine |
| OLMo 2 1B (AllenAI) | Language model for math reasoning |
| Uvicorn | ASGI server |
| Requests | HTTP client for model communication |

---

## Setup & Installation

### Prerequisites
- Python 3.9+
- [Ollama](https://ollama.com) installed on your machine

### Steps

**1. Install Ollama**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**2. Pull the OLMo 2 1B model**
```bash
ollama pull hf.co/allenai/OLMo-2-0425-1B-Instruct-GGUF:Q4_K_M
```

**3. Clone the repository**
```bash
git clone https://github.com/yomi-adamo/Math-App.git
cd Math-App
```

**4. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**5. Install dependencies**
```bash
pip install fastapi uvicorn requests
```

**6. Run the server**
```bash
uvicorn main:app --reload
```

---

## Usage

Send a POST request to the `/solve` endpoint with a math problem in natural language:

```bash
curl -X POST http://127.0.0.1:8000/solve \
  -H "Content-Type: application/json" \
  -d '{"problem": "5 + 7"}'
```

The API routes the query to the locally running OLMo model and returns the model's solution.

---

## Key Features

- **Local inference** — No external API keys or cloud costs. The LLM runs entirely on your machine via Ollama.
- **FastAPI backend** — Clean, auto-documented REST interface (Swagger UI available at `/docs`).
- **Model flexibility** — Easily swap the Ollama model by updating the model name in the request payload.
- **Lightweight setup** — Minimal dependencies; runs on consumer hardware.

---

## My Contribution

This was a solo personal project. I designed and implemented the full application from scratch, including the FastAPI route structure, the Ollama integration layer, the prompt formatting logic, and the project documentation. I also evaluated multiple models during development, starting with TinyLlama before switching to OLMo 2 1B after observing improved reasoning quality on math problems.

---

## Reflection

This project gave me hands-on experience with local LLM deployment — a pattern increasingly relevant in defense and edge computing contexts where data cannot leave a secure environment. The main challenge was understanding Ollama's model format requirements and structuring prompts that produced consistent, parseable outputs from a small model. It reinforced that model selection and prompt design are just as important as the surrounding infrastructure.
