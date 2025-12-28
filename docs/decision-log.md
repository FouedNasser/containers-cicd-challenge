# Decision Log - Containers & CI/CD Challenge

## Project Architecture & Tooling

### 1. Framework: FastAPI (0.109.0)
- **Decision:** Used the latest stable version of FastAPI with Pydantic V2.
- **Reason:** Pydantic V2 offers significant performance improvements and is the current industry standard. It ensures the solution is "job-ready" for modern environments.

### 2. Database: PostgreSQL (15-alpine)
- **Decision:** Used PostgreSQL for production-grade persistence and SQLite for unit testing.
- **Reason:** Postgres is the industry standard for relational data. SQLite was chosen for tests because it allows for fast, isolated, and in-memory test execution without requiring a live database server, ensuring the CI pipeline is fast and reliable.

### 3. Containerization: Multi-stage Dockerfile
- **Decision:** Implemented a two-stage build process.
- **Reason:** 
    - **Stage 1 (Builder):** Installs build tools (`gcc`, `libpq-dev`) to compile `psycopg2`.
    - **Stage 2 (Final):** Only contains the compiled "wheels" and the runtime libraries.
    - **Result:** A significantly smaller and more secure image by excluding unnecessary build-time dependencies.

### 4. Configuration: Pydantic-Settings
- **Decision:** Used `pydantic-settings` to manage environment variables.
- **Reason:** It provides automatic validation (e.g., ensuring ports are integers) and easily handles `.env` files, keeping secrets out of the codebase as required by the challenge.

### 5. Authentication: JWT & Bcrypt
- **Decision:** Implemented JSON Web Tokens (JWT) for stateless authentication and Bcrypt for secure password hashing.
- **Reason:** Securely stores user credentials and allows for scalable, token-based authentication.

### 6. CI/CD: GitHub Actions
- **Decision:** Configured a pipeline that runs tests, builds the image, and verifies container startup.
- **Reason:** Automates the "Quality Gate," ensuring that no broken code is merged into the main branch.
