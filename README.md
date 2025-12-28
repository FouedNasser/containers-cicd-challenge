# 🧩 FastAPI Auth with PostgreSQL & CI/CD

This project implements a containerized FastAPI application with PostgreSQL integration, secure authentication, and a complete CI/CD pipeline.

---

## 🚀 Getting Started

### 1. Prerequisites
- Docker & Docker Compose
- Python 3.10+ (optional, for local development outside Docker)

### 2. Run with Docker (Recommended)
This command builds the optimized multi-stage image and orchestrates the FastAPI app and PostgreSQL database.
```bash
docker-compose -f docker/docker-compose.yml up --build
```
- **API Base URL:** `http://localhost:8000`
- **Interactive API Docs (Swagger):** `http://localhost:8000/docs`
- **Health Check:** `http://localhost:8000/`

### 3. Local Development & Testing
To run tests or the application locally:
```bash
# Install dependencies
pip install -r app/requirements.txt

# Run unit tests (uses in-memory SQLite)
pytest app/tests/test_app.py

# Run application locally
uvicorn app.main:app --reload
```

### 4. Environment Variables
The following variables can be configured via an `.env` file or exported in your shell:
- `POSTGRES_USER`: Database username (default: `postgres`)
- `POSTGRES_PASSWORD`: Database password (default: `postgres`)
- `POSTGRES_DB`: Database name (default: `fastapi_db`)
- `SECRET_KEY`: JWT signing key (default: `placeholder_secret_key`)

---

## 📂 Project Structure

```
.
├── app/
│   ├── main.py            # FastAPI Application & Routes
│   ├── auth.py            # JWT & Hashing Utilities
│   ├── database.py        # SQLAlchemy Connection
│   ├── models.py          # Database Models
│   ├── schemas.py         # Pydantic Validation
│   ├── config.py          # Environment Configuration
│   └── tests/
│       └── test_app.py    # Pytest Suite
├── docker/
│   ├── Dockerfile         # Multi-stage optimized build
│   └── docker-compose.yml # Service orchestration
└── .github/workflows/
    └── ci.yml             # GitHub Actions Pipeline
```
