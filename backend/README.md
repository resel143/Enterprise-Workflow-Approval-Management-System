# Enterprise Workflow & Approval Management System – Backend

This repository contains the **backend service** for the Enterprise Workflow & Approval Management System, built using **Django** and **Django REST Framework**.

The backend is responsible for:
- Authentication & authorization
- Organization and user management
- Workflow definition & execution
- Approval lifecycle handling
- Audit logging
- Notifications & SLA escalation

---

## 🏗️ Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (Access & Refresh Tokens)
- **Async Processing:** Celery + Redis
- **Real-time:** Django Channels (WebSockets)
- **Caching:** Redis
- **Documentation:** Swagger / OpenAPI
- **Testing:** Pytest / Django Test Framework

---

## 📦 Project Structure

backend/
│── accounts/ # Authentication & user management
│── organizations/ # Organization & department management
│── workflows/ # Workflow definitions & steps
│── requests/ # Request lifecycle handling
│── approvals/ # Approval engine & actions
│── notifications/ # Email & in-app notifications
│── auditlogs/ # System-wide audit logging
│── core/ # Shared utilities & base classes
│── config/ # Django project settings
│── manage.py


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
git clone <repository-url>
cd backend

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

Create a .env file:

DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/workflow_db
REDIS_URL=redis://127.0.0.1:6379
JWT_SECRET_KEY=your_jwt_secret

### 🗄️ Database Setup
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

---

###  🚀 Running the Server
python manage.py runserver


Server will be available at:

http://127.0.0.1:8000/

---

###  🔐 Authentication Flow

Login returns JWT access & refresh tokens

Tokens required for protected APIs

Role-based access control enforced at API level

---

###  🔁 Async Tasks (Celery)

Start Redis:

redis-server


Start Celery worker:

celery -A config worker -l info
---

###  📑 API Documentation

Swagger UI:

http://127.0.0.1:8000/api/docs/

---

###  🧪 Running Tests
python manage.py test
---

###  🔒 Security Features

Role-Based Access Control (RBAC)

Input validation & sanitization

Rate limiting

Soft deletes

Audit trail for all critical actions
---

###  📌 Key Features

Dynamic workflow builder

Multi-step approval engine

Parallel & conditional approvals

SLA tracking & escalation

Full audit logging

Real-time notifications
--- 
### 🧑‍💻 Author
By Reshul
Enterprise Workflow & Approval Management System
Backend developed using Django & DRF
