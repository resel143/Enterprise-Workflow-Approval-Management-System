# Enterprise Workflow & Approval Management System – Frontend

This repository contains the **frontend application** for the Enterprise Workflow & Approval Management System, built using **Angular**.

The frontend is responsible for:
- Role-based dashboards
- Workflow builder UI
- Request creation & tracking
- Approval inbox & actions
- Notifications & audit log views
- SLA monitoring and visual indicators

---

## 🏗️ Tech Stack

- **Framework:** Angular
- **Language:** TypeScript
- **UI Library:** Angular Material / Tailwind CSS
- **State Management:** RxJS
- **Authentication:** JWT-based authentication
- **API Communication:** REST APIs
- **Build Tool:** Angular CLI

---

## 📦 Project Structure

frontend/
│── src/
│ ├── app/
│ │ ├── core/ # Services, guards, interceptors
│ │ ├── shared/ # Reusable components, pipes
│ │ ├── auth/ # Login & authentication
│ │ ├── dashboard/ # Role-based dashboards
│ │ ├── workflows/ # Workflow builder module
│ │ ├── requests/ # Request creation & tracking
│ │ ├── approvals/ # Approval inbox & actions
│ │ ├── notifications/ # Notifications UI
│ │ └── auditlogs/ # Audit log viewer
│ └── environments/
│ ├── environment.ts
│ └── environment.prod.ts

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites

- Node.js (v16+ recommended)
- npm or yarn
- Angular CLI

npm install -g @angular/cli

2️⃣ Install Dependencies
cd frontend
npm install

3️⃣ Environment Configuration

Edit src/environments/environment.ts:

export const environment = {
  production: false,
  apiBaseUrl: 'http://127.0.0.1:8000/api'
};

## 🚀 Running the Application
ng serve


Frontend will be available at:

http://localhost:4200/

---

## 🔐 Authentication & Authorization

JWT token stored securely in browser storage

HTTP interceptor attaches token to API requests

Route guards protect private routes

Role-based navigation and UI rendering

---

## 📊 Core Features

Role-based dashboards (Admin, Manager, Employee)

Dynamic workflow builder interface

Request submission with validation

Approval inbox with approve/reject actions

SLA countdown timers

Notification panel with read/unread state

Audit log viewer with filters

---

## ⚡ Performance & UX

Lazy-loaded Angular modules

Global loaders & error handling

Optimized API calls using RxJS

Responsive and accessible UI design

---

## 🧪 Running Tests
ng test

📦 Production Build
ng build --prod


Build artifacts will be generated in the dist/ directory.

---

## 📌 Best Practices Followed

Modular architecture

Separation of concerns

Reusable shared components

Centralized API services

Strong typing with TypeScript

Clean UX for enterprise workflows

## 🧑‍💻 Author

Enterprise Workflow & Approval Management System
Frontend developed using Angular
