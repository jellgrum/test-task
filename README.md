# Test Task

## Architecture

Two-container application orchestrated with Docker Compose:

- **Backend** — lightweight Python HTTP server serving `/` and `/health` endpoints.
- **Nginx** — reverse proxy that forwards external requests to the backend.

```
Client → Nginx (:80) → Backend (:${BACKEND_PORT})
```

Both services communicate over a shared Docker bridge network.

## Tech Stack

| Component        | Technology              |
|------------------|-------------------------|
| Backend          | Python 3.12 (stdlib)    |
| Reverse Proxy    | Nginx 1.28 (Alpine)     |
| Containerization | Docker + Docker Compose |
| CI               | GitHub Actions          |

## Launch

1. **Create `.env` file** in the project root:
  ```env
  # Example values
  DOMAIN_NAME=localhost
  BACKEND_PORT=8080
  ```

2. **Build and start** the services:
  ```sh
  docker compose up -d --build
  ```

3. **Verify** the containers are running:
  ```sh
  docker compose ps
  ```

## Check Functionality

```sh
curl http://localhost/
# Expected: Hello from Effective Mobile!

curl http://localhost/health
# Expected: OK
```

## CI Checks

Two GitHub Actions pipelines run on every push/pull request to any branch and are also available for manual launch.

**Linting** ([`.github/workflows/linting.yml`](.github/workflows/linting.yml)):

| Job                | Tool           | Target               |
|--------------------|----------------|----------------------|
| Python linting     | Ruff           | `backend/`           |
| Nginx linting      | Gixy           | `nginx/nginx.conf`   |
| Dockerfile linting | Hadolint       | `backend/Dockerfile` |
| Dockerfile linting | Hadolint       | `nginx/Dockerfile`   |
| Compose validation | Docker Compose | `docker-compose.yml` |

**Security** ([`.github/workflows/security.yml`](.github/workflows/security.yml)):

| Job         | Tool  | Target                  |
|-------------|-------|-------------------------|
| Image scan  | Trivy | `backend` (built image) |
| Image scan  | Trivy | `nginx:1.28.3-alpine`   |
| Config scan | Trivy | `docker-compose.yml`    |

All Trivy scans report **CRITICAL** and **HIGH** severity vulnerabilities and fail the pipeline if any are found.
