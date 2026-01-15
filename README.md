# Secure FastAPI JWT API

A modern **FastAPI application** demonstrating **secure API development** and **DevSecOps best practices**.  

This project is fully **Dockerized**, uses **JWT authentication**, and includes an automated **CI/CD pipeline** with **security scanning**.

---

## Features

- FastAPI API with **JWT authentication**  
- Dockerized with **Python 3.9-slim**  
- Runs as a **non-root user** inside container  
- Dependencies pinned for **reproducibility**  
- CI/CD pipeline with:
  - **Trivy** container vulnerability scanning  
  - **Semgrep** Python code scanning  
- Ready for production demo & portfolio showcase  

---

## Endpoints

- `GET /` → Public endpoint  
- `POST /token` → Generate JWT token for a user  
- `GET /private` → Private endpoint, requires valid JWT  

Example token request:

```bash
curl -X POST "http://localhost:8000/token" -H "Content-Type: application/json" -d '{"user":"Divya"}'
