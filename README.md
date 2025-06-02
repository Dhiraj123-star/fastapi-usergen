
---

# 🧪 FastAPI User Generator

A lightweight 💡 FastAPI-based service that generates and manages fake user data using SQLAlchemy and Faker.

## 🚀 Core Features

* ✅ **Generate Fake Users** — Instantly create realistic user profiles using Faker.
* 📥 **Create Users** — Add new users to the SQLite database with a single API call.
* 🔍 **Get User by Email** — Fetch user details by email address.
* 📄 **List All Users** — Retrieve a complete list of all users stored in the database.
* ✏️ **Edit User** — Update user details by email.
* ❌ **Delete User** — Remove user records by email.
* ❤️ **Health Check** — Simple `/health` endpoint to verify service status.

## 🛠️ Tech Stack

* ⚡ **FastAPI** — blazing fast API framework
* 🐍 **SQLAlchemy** — ORM for database interaction
* 🧪 **Faker** — generates realistic dummy data
* 🐳 **Docker** — for containerized development
* 🌐 **Nginx** — reverse proxy with HTTPS and load balancing
* 🔐 **SSL** — self-signed certs for HTTPS support (local testing)
* 🔁 **GitHub Actions** — automated CI/CD pipeline to Docker Hub

## 📦 API Endpoints

* `POST /users/` → 🆕 Generate and save a fake user
* `GET /users/{email}` → 🔍 Retrieve user by email
* `GET /users/all` → 📄 List all users
* `PUT /users/{email}` → ✏️ Update user details by email
* `DELETE /users/{email}` → ❌ Delete user by email
* `GET /health` → ❤️ Health check endpoint

## 📂 Database

* Uses **SQLite** 🗃️ as a lightweight, file-based DB (`users.db`).

## ⚙️ Production-Like Setup

* 🧱 **Multiple FastAPI instances** (on ports 8000, 8001, 8002) to simulate horizontal scaling.
* 🔁 **Nginx load balancer** configured with round-robin strategy.
* 🔐 **HTTPS** enabled using **self-signed SSL certificates** (via `/certs`).
* 🐳 Fully containerized using **Docker Compose**.

## 🚀 CI/CD with Docker Hub

* Automatic build and push of Docker image on every push to `main` using **GitHub Actions**.
* Docker image available at: [`dhiraj918106/fastapi-usergen`](https://hub.docker.com/r/dhiraj918106/fastapi-usergen)

---

