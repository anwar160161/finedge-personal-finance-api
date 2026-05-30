# FinEdge Personal Finance API

## Overview

FinEdge Personal Finance API is a backend application built using FastAPI that helps users manage personal finances by tracking income and expenses, generating summaries, setting budgets, and analyzing spending habits.

The project follows MVC architecture and includes authentication, analytics, caching, middleware, testing, and SQLite database persistence using SQLAlchemy ORM.

---

## Features

### Core Features

* User Registration
* JWT Authentication
* Add Income and Expense Transactions
* View All Transactions
* View Transaction by ID
* Update Transactions
* Delete Transactions
* Financial Summary Dashboard

### Analytics

* Filter transactions by category
* Filter transactions by month
* Monthly spending analysis

### AI-Based Suggestions

* Generates personalized saving tips based on spending patterns

### Middleware

* Request Logging Middleware
* Global Error Handling Middleware
* Transaction Validation Middleware

### Performance

* In-memory caching for summary endpoint
* Cache invalidation on transaction updates

### Database

* SQLite Database
* SQLAlchemy ORM
* Automatic table creation

### Testing

* Unit tests using Pytest
* Health endpoint test
* User API test
* Transaction API test

---

## Tech Stack

* Python 3.13
* FastAPI
* SQLAlchemy
* SQLite
* JWT (PyJWT)
* Pydantic
* Pytest
* Uvicorn

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

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
SECRET_KEY=finedge-secret-key-2026
PORT=8000
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Application:

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

### Authentication

| Method | Endpoint    |
| ------ | ----------- |
| POST   | /auth/login |

### Users

| Method | Endpoint |
| ------ | -------- |
| POST   | /users   |
| GET    | /users   |

### Transactions

| Method | Endpoint           |
| ------ | ------------------ |
| POST   | /transactions      |
| GET    | /transactions      |
| GET    | /transactions/{id} |
| PATCH  | /transactions/{id} |
| DELETE | /transactions/{id} |

### Analytics

| Method | Endpoint                              |
| ------ | ------------------------------------- |
| GET    | /transactions/analytics?category=Food |
| GET    | /transactions/analytics?month=5       |

### Summary

| Method | Endpoint |
| ------ | -------- |
| GET    | /summary |

---

## Running Tests

```bash
pytest
```

Expected Output:

```text
3 passed
```

---

## Bonus Features Implemented

### Analytics & Reporting

* Category Based Filtering
* Monthly Transaction Filtering

### AI Assistance

* Automated Saving Tips

### Advanced Middleware

* Logging Middleware
* Validation Middleware
* Error Handling Middleware

### Authentication

* JWT-Based Authentication

### Database Persistence

* SQLite Database
* SQLAlchemy ORM

### Caching

* In-Memory Cache with TTL

---

## Future Improvements

* Password Hashing using bcrypt
* PostgreSQL Support
* Role-Based Authorization
* Docker Deployment
* Alembic Database Migrations
* Refresh Tokens for JWT Authentication

---

## Author

**Anwar Shaik**

Python | FastAPI | SQLAlchemy
