# Incident Board

A three-tier microservice web application for tracking operational incidents and their resolution status. Users can report new incidents, view active and resolved incidents, and mark incidents as resolved.

The project demonstrates migrating a multi-container application from a local **Docker Compose** environment to a production-ready **Kubernetes (k3s)** cluster with an automated **GitHub Actions CI/CD** pipeline.

## Tech Stack

- **Orchestration & Containers:** Kubernetes (`k3s`), Traefik Ingress, Docker, Docker Compose
- **CI/CD:** GitHub Actions (automated Docker build, dual-tagging with `latest` + commit SHA, and zero-downtime `kubectl` rollout)
- **Frontend:** Nginx (static file serving & reverse proxy for `/api/*`), HTML5, Vanilla JavaScript (`fetch` API)
- **Backend:** Python 3.9, Flask, `psycopg` (v3)
- **Database:** PostgreSQL 18 (PersistentVolumeClaim + schema initialization via ConfigMap)
- **Security:** Kubernetes RBAC (`ServiceAccount`, least-privilege `Role` & `RoleBinding` for CI/CD deployments), Kubernetes Secrets

## Architecture

```
User
  |
  v
Traefik Ingress (Kubernetes)
  |
  v
Frontend (Nginx + HTML/JavaScript)
  |
  | HTTP API (/api/incidents)
  v
Backend (Python + Flask)
  |
  | SQL (TCP 5432)
  v
Database (PostgreSQL + PersistentVolumeClaim)
```

## Repository Structure

```text
├── .github/workflows/
│   └── ci.yml                  # CI/CD pipeline (build, push to registry, deploy to K8s)
├── docker/
│   ├── backend/                # Flask API microservice & Dockerfile
│   ├── db/                     # SQL schema initialization
│   ├── frontend/               # Nginx reverse proxy config, UI & Dockerfile
│   └── docker-compose.yml      # Local development environment
└── k8s/
    ├── configmaps/             # Database initialization SQL ConfigMap
    ├── ingress/                # Traefik Ingress routing rules
    ├── pvc/                    # PersistentVolumeClaim for PostgreSQL storage
    ├── rbac/                   # Least-privilege ServiceAccount & Role for CD
    ├── secrets/                # Database credentials template (Base64)
    ├── backend.yml             # Backend Deployment (with Liveness/Readiness probes) & Service
    ├── db.yml                  # PostgreSQL Deployment & ClusterIP Service
    └── frontend.yml            # Frontend Deployment & ClusterIP Service
```

## Quick Start

### Local Development (Docker Compose)

```bash
cd docker
export POSTGRES_PASSWORD="your_strong_password"
docker compose up --build -d
```

The web UI will be available at `http://localhost:8080`.

### Kubernetes Deployment

```bash
kubectl apply -f k8s/configmaps/
kubectl apply -f k8s/secrets/
kubectl apply -f k8s/pvc/
kubectl apply -f k8s/rbac/
kubectl apply -f k8s/db.yml
kubectl apply -f k8s/backend.yml
kubectl apply -f k8s/frontend.yml
kubectl apply -f k8s/ingress/
```
