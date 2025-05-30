
---

# 🧪 FastAPI User Generator

A lightweight FastAPI-based service that generates and manages fake user data using SQLAlchemy and Faker.

## 🚀 Core Features

* ✅ **Generate Fake Users**: Instantly create realistic user profiles using Faker.
* 📥 **Create Users**: Add new users to the SQLite database with a single API call.
* 🔍 **Get User by Email**: Fetch user details by email address.
* 📄 **List All Users**: Retrieve a complete list of all users stored in the database.

## 🛠️ Tech Stack

* ⚡ **FastAPI** — blazing fast API framework
* 🐍 **SQLAlchemy** — ORM for database interaction
* 🧪 **Faker** — generates realistic dummy data
* 🐳 **Docker** — for containerized development

## 📦 API Endpoints

* `POST /users/` → Generate and save a fake user
* `GET /users/{email}` → Retrieve user by email
* `GET /users/all` → List all users

## 📂 Database

* Uses **SQLite** as a lightweight, file-based DB (`users.db`).

---
