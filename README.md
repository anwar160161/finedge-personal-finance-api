# FinEdge Personal Finance API

Version: 2.0.0

A modern Personal Finance Management API built with FastAPI, SQLAlchemy, and SQLite. The application enables users to manage income and expenses, generate financial summaries, analyze spending patterns, and receive AI-powered saving recommendations.

---

## Overview

FinEdge Personal Finance API is a backend application designed to help users efficiently manage their personal finances by tracking transactions, monitoring spending habits, and generating financial insights.

The project follows the MVC (Model-View-Controller) architecture and incorporates authentication, analytics, caching, middleware, testing, and database persistence using SQLAlchemy ORM.

---

## Features

### Core Features

* User Registration
* Get User Details
* Delete User
* JWT Authentication
* Add Income and Expense Transactions
* View All Transactions
* View Transaction by ID
* Update Transactions
* Delete Transactions
* Financial Summary Dashboard

### Analytics & Reporting

* Filter transactions by category
* Filter transactions by month
* Monthly spending analysis

### AI-Based Suggestions

* Personalized saving tips based on spending patterns

### Middleware

* Request Logging Middleware
* Global Error Handling Middleware
* Transaction Validation Middleware

### Performance

* In-Memory Caching with TTL
* Cache Invalidation on Transaction Updates

### Database

* SQLite Database
* SQLAlchemy ORM
* Automatic Table Creation

### Testing

* Unit Tests using Pytest
* Health Endpoint Test
* User API Test
* Transaction API Test

---

## Tech Stack

* Python 3.13
* FastAPI
* SQLAlchemy
* SQLite
* PyJWT
* Pydantic
* Pytest
* Uvicorn

---

## Architecture

The application follows the MVC (Model-View-Controller) architecture pattern:

* **Models** – SQLAlchemy ORM database models
* **Schemas** – Pydantic request and response validation
* **Routes** – API endpoint definitions
* **Controllers** – Request handling layer
* **Services** – Business logic layer
* **Middleware** – Logging, validation, and exception handling
* **Database** – SQLite with SQLAlchemy ORM

This architecture improves maintainability, scalability, and separation of concerns.

---

## Project Structure

```text
finedge-personal-finance-api/
│
├── app/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── database.py
│   ├── dependencies.py
│   └── main.py
│
├── tests/
│   ├── test_health.py
│   ├── test_users.py
│   └── test_transactions.py
│
├── .env
├── finedge.db
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <your-github-repository-url>
cd finedge-personal-finance-api
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=finedge-secret-key-2026
PORT=8000
```

---

## Running the Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health

| Method | Endpoint |
| ------ | -------- |
| GET    | /health  |

---

### Authentication

| Method | Endpoint    |
| ------ | ----------- |
| POST   | /auth/login |

---

### Users

| Method | Endpoint         |
| ------ | ---------------- |
| POST   | /users           |
| GET    | /users           |
| GET    | /users/{user_id} |
| DELETE | /users/{user_id} |

---

### Transactions

| Method | Endpoint           |
| ------ | ------------------ |
| POST   | /transactions      |
| GET    | /transactions      |
| GET    | /transactions/{id} |
| PATCH  | /transactions/{id} |
| DELETE | /transactions/{id} |

---

### Analytics

| Method | Endpoint                              |
| ------ | ------------------------------------- |
| GET    | /transactions/analytics?category=Food |
| GET    | /transactions/analytics?month=5       |

---

### Summary

| Method | Endpoint |
| ------ | -------- |
| GET    | /summary |

---

## Running Tests

Execute:

```bash
pytest
```

Current Status:

```text
3 Passed Tests
0 Failed Tests
```

---

## Bonus Features Implemented

### Analytics & Reporting

* Category-Based Filtering
* Monthly Transaction Filtering

### AI Assistance

* Automated Saving Recommendations

### Authentication

* JWT-Based Authentication

### Database Persistence

* SQLite Database
* SQLAlchemy ORM

### Advanced Middleware

* Request Logging Middleware
* Transaction Validation Middleware
* Global Exception Handling Middleware

### Performance Optimization

* In-Memory Cache Service
* TTL-Based Cache Expiry

---

## Future Improvements

* Password Hashing using bcrypt
* PostgreSQL Support
* Docker Deployment
* Alembic Database Migrations
* Refresh Tokens for JWT Authentication
* Role-Based Authorization
* User Budget Management
* Export Reports to PDF/CSV

---

## Author

**Anwar Shaik**

Python | FastAPI | SQLAlchemy

GitHub: https://github.com/anwar160161