# Secure Authentication Portal

# Student Details
 Student Name                 : B RANJITH KUMAR
 
 Student ID                	  : SGT-26E-2412
 
 Domain                    	  : Backend Developer
 
 Project Title                : SoftGrowTech Student Management REST API

This is a complete professional backend development project built for the **SoftGrowTech Internship Task 2**. The project demonstrates a secure, modern, and responsive User Authentication System using Flask and SQLite.

---

# 🚀 Project Overview

The **Secure Authentication Portal** is a full-stack web application designed to handle secure user authentication and authorization functionalities including:

- User Registration
- User Login
- User Logout
- Session Management
- Password Encryption
- Protected Dashboard Access

The application features a premium dark-themed responsive UI built using Bootstrap 5 and modern frontend technologies.

---

# ✨ Features

✅ User Registration  
✅ Secure User Login  
✅ User Logout  
✅ Password Hashing using Bcrypt  
✅ Flask-Login Session Management  
✅ Protected Routes  
✅ Responsive Dashboard  
✅ Strong Password Validation  
✅ Duplicate Account Prevention  
✅ Error Handling & Flash Messages  
✅ Professional Dark UI  

---

# 🛠️ Technologies Used

## Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Bcrypt

## Database
- SQLite

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Tools
- Git
- GitHub
- VS Code

---

# ⚙️ Project Structure

```text
SoftGrowTech_Auth_System/
│
├── app.py
├── requirements.txt
├── README.md
├── config.py
│
├── models/
│   └── user_model.py
│
├── routes/
│   └── auth_routes.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── main.js
│
├── screenshots/
│
└── database/
    └── users.db
```

---

# 🔐 Authentication Flow

## Registration Flow
1. User enters username, email, and password
2. Backend validates form data
3. Password is encrypted using Bcrypt
4. User details stored securely in SQLite database

## Login Flow
1. User enters email and password
2. Backend verifies credentials
3. Flask-Login creates secure session
4. User redirected to protected dashboard

## Protected Routes
- Dashboard accessible only after authentication
- Unauthorized users redirected to login page

---

# 📸 Project Screenshots

## 🏠 Home Page

Modern landing page for the Secure Authentication Portal.

<img width="1917" height="909" alt="Screenshot 2026-05-11 200101" src="https://github.com/user-attachments/assets/a942f3f9-86f3-46d5-ac02-1733ad5721c0" />

---

## 📝 Registration Page

Secure signup form with validation and password security requirements.

<img width="1908" height="897" alt="Screenshot 2026-05-11 200121" src="https://github.com/user-attachments/assets/7755f2ad-3493-4e2d-9a79-d449bec14b31" />


---

## ⚠️ Form Validation

Strong password validation and error handling system.

<img width="1917" height="914" alt="Screenshot 2026-05-11 200211" src="https://github.com/user-attachments/assets/a57afa4b-4c7a-44a2-bcb5-eda29dd659c4" />


---

## ✅ Successful Registration

Successful account creation with validation checks.

<img width="1918" height="906" alt="Screenshot 2026-05-11 200401" src="https://github.com/user-attachments/assets/c0eb0eba-2a2f-47b9-b492-4c4c108258c6" />


---

## 🔐 Login Page

Secure login page for user authentication.

<img width="1919" height="907" alt="Screenshot 2026-05-11 200432" src="https://github.com/user-attachments/assets/edd6489e-0ba1-4a02-9b52-41752ac8a2e8" />


---

## 📊 Protected Dashboard

Authenticated users can access secure dashboard.

<img width="1919" height="912" alt="Screenshot 2026-05-11 200450" src="https://github.com/user-attachments/assets/0776ee45-86f7-40ec-9e3b-866c7ddeb8ab" />


---

## 🚪 Logout System

Secure logout functionality with session termination.

<img width="1898" height="901" alt="Screenshot 2026-05-11 200533" src="https://github.com/user-attachments/assets/79c837f1-3713-48fe-af94-feea9c9b080a" />


---

# 🔄 Authentication Features

| Feature | Description |
|----------|-------------|
| User Registration | Create secure accounts |
| User Login | Authenticate existing users |
| Password Hashing | Encrypt passwords using Bcrypt |
| Session Management | Flask-Login based authentication |
| Protected Routes | Restrict unauthorized access |
| Logout System | End active user sessions securely |


# 💻 Installation & Setup Guide

## Step 1 — Clone or Download Project

Download the project and open it in VS Code.

```bash
git clone https://github.com/ranjithkumar077/Secure-Authentication-Portal.git
```
---

## Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 3 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

# Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 5 — Run Flask Application

```bash
python app.py
```

---

# Step 6 — Open Browser

```text
http://127.0.0.1:5000
```

---

# 📦 requirements.txt

```txt
Flask
Flask_SQLAlchemy
Flask_Login
Flask_Bcrypt
```

---

# 🔐 Routes Implemented

| Method | Route | Description |
|--------|--------|-------------|
| GET | / | Home page |
| GET | /login | Login page |
| POST | /login | User login |
| GET | /register | Registration page |
| POST | /register | Create account |
| GET | /dashboard | Protected dashboard |
| GET | /logout | Logout user |

---

# 🎯 Internship Task Objectives Completed

✅ User Authentication System  
✅ Secure Login & Signup  
✅ Password Encryption  
✅ Session Handling  
✅ Protected Dashboard  
✅ Flask Backend Development  
✅ Database Integration  
✅ Responsive Frontend Design  

---

# 📸 Future Improvements

- JWT Authentication
- Email Verification
- Password Reset System
- Two-Factor Authentication
- OAuth Login
- Cloud Deployment

---

# 👨‍💻 Developed By

<div align="center">

# B Ranjith Kumar

Backend Developer Intern  
SoftGrowTech

</div>
