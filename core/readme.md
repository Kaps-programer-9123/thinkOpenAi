# 🧠 thinkOpenAI – Modular Django GenAI & RAG Framework

**thinkOpenAI** is a modular Django-based application designed to power GenAI and Retrieval-Augmented Generation (RAG) pipelines. Each Django app in this project handles a specific function—from text chunking to middleware and logging—working together to expose a complete set of REST APIs for external integrations.

> Built for scale, ready for Docker, CI/CD-enabled, and deployable to Amazon EKS.

---

## 🧩 Project Structure

This Django monorepo is organized into modular apps, each serving a unique purpose:

| Folder        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `chunking/`   | Handles text chunking and intelligent splitting for token-optimized input. |
| `core/`       | The central Django app, contains main settings, URLs, and logic.           |
| `logs/`       | Captures application logs, errors, and audit trails.                       |
| `middleware/` | Custom middleware for request/response processing, logging, etc.           |
| `db.sqlite3`  | Local development SQLite database.                                          |
| `manage.py`   | Django's project management command-line tool.                             |

Each app defines its own `urls.py` and exposes REST APIs that can be consumed externally for orchestration with GenAI tools, agents, or UIs.

---

## 🚀 Getting Started (Locally)

### 🛠️ Requirements

- Python 3.12+
- pip / virtualenv
- Docker (optional for containerized setup)

### ▶️ Run Locally (Dev Mode)

```bash
# Set up virtual environment
python -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Run the Django development server
cd core
python manage.py runserver
```
### 🧪 Run Tests
```bash
cd core
pytest
```

### 🐳 Docker Support
This project includes a Dockerfile to containerize the entire Django app.
```bash
docker build -t thinkopenai-app .
```

### ▶️ Run Container
```bash
docker run -d -p 8000:8000 --name thinkopenai-container thinkopenai-app
```

### 🛑 Stop & Remove Container
```bash
docker stop thinkopenai-container && docker rm thinkopenai-container
```