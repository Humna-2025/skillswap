<div align="center">

# 🔄 SkillSwap

### Peer-to-Peer Skill Bartering Platform for University Students

<p align="center">
  <b>Learn. Teach. Exchange. Grow.</b>
</p>

<p align="center">
  A web-based platform that allows students to exchange skills using a<br>
  <b>credit-based bartering system instead of money.</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST%20API-black?logo=flask)
![MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-green?logo=mongodb\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript\&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-orange?logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-blue?logo=css3\&logoColor=white)
![PyMongo](https://img.shields.io/badge/PyMongo-Driver-green)
![bcrypt](https://img.shields.io/badge/bcrypt-Password%20Hashing-red)

</p>

<p align="center">

<a href="https://github.com/Humna-2025">
<img src="https://img.shields.io/badge/GitHub-Humna--2025-181717?logo=github">
</a>

</p>

</div>

---

# 📌 Table of Contents

* [📖 Project Overview](#-project-overview)
* [🎯 Problem Statement](#-problem-statement)
* [💡 Solution](#-solution)
* [✨ Key Features](#-key-features)
* [🔄 How SkillSwap Works](#-how-skillswap-works)
* [💳 Credit Bartering System](#-credit-bartering-system)
* [🏗️ System Architecture](#️-system-architecture)
* [🛠️ Technology Stack](#️-technology-stack)
* [🗄️ Database Design](#️-database-design)
* [🔌 REST API](#-rest-api)
* [📂 Project Structure](#-project-structure)
* [🎨 User Interface](#-user-interface)
* [🔐 Authentication & Security](#-authentication--security)
* [⚙️ Installation](#️-installation)
* [▶️ How to Run](#️-how-to-run)
* [🧪 Testing](#-testing)
* [📊 Example Workflow](#-example-workflow)
* [🚀 Future Enhancements](#-future-enhancements)
* [📚 Learning Outcomes](#-learning-outcomes)
* [👩‍💻 Project Information](#-project-information)
* [📄 License](#-license)

---

# 📖 Project Overview

**SkillSwap** is a web-based peer-to-peer skill bartering platform designed specifically for university students.

The platform allows students to **teach skills to other students and earn Skill Credits**, which they can later spend to learn skills from their peers.

Instead of paying money for tutoring, users participate in a structured skill exchange ecosystem.

### Example

A student who knows **Python** can teach another student and earn Skill Credits.

The earned credits can then be used to learn:

* Graphic Design
* Photoshop
* Public Speaking
* Mathematics
* Video Editing
* Languages
* UI/UX Design
* Programming

The project demonstrates a complete full-stack web application using:

**Frontend → Flask REST API → MongoDB**

---

# 🎯 Problem Statement

University students possess valuable skills but often lack an organized platform where they can exchange those skills without financial transactions.

Existing solutions have several limitations:

* Paid tutoring can be expensive.
* Social media groups are unstructured.
* Students may struggle to find peers with specific skills.
* There is no proper credit-based exchange mechanism.
* Skill exchange history is difficult to track.
* There is limited accountability through ratings and transaction records.

### Problem

Students need a structured platform where they can:

> **Teach what they know, earn credits, and use those credits to learn something new.**

---

# 💡 Solution

SkillSwap introduces a **credit-based skill bartering system**.

Users can:

1. Create an account.
2. Create a skill profile.
3. Add skills they can teach.
4. Add skills they want to learn.
5. Search for other students.
6. Send skill swap requests.
7. Accept or decline requests.
8. Complete a learning session.
9. Transfer Skill Credits.
10. Rate other students.
11. View transaction history.
12. Monitor notifications.
13. Compete on the leaderboard.

No direct monetary transaction is required.

---

# ✨ Key Features

| #  | Feature                | Description                                          |
| -- | ---------------------- | ---------------------------------------------------- |
| 1  | 👤 User Authentication | Registration and login system                        |
| 2  | 🧑‍💻 Skill Profiles   | Users can list skills they teach and want to learn   |
| 3  | 🔍 Search & Filter     | Find students based on their skills                  |
| 4  | 🔄 Swap Requests       | Send, accept, decline and complete skill exchanges   |
| 5  | 💳 Credit System       | Teaching earns credits and learning consumes credits |
| 6  | 📜 Transaction History | Records all credit transfers                         |
| 7  | ⭐ Rating System        | Users can rate each other after completed swaps      |
| 8  | 🏆 Leaderboard         | Displays top users based on credits and ratings      |
| 9  | 🔔 Notifications       | Displays swap-related notifications                  |
| 10 | 📱 Responsive UI       | Works across desktop and smaller screens             |
| 11 | 📊 Dashboard           | Displays user information, credits and activities    |
| 12 | 🎨 Glassmorphism UI    | Modern dashboard interface                           |
| 13 | 📂 Collapsible Sidebar | Easy navigation between dashboard sections           |
| 14 | 🔌 REST API            | Backend functionality exposed through API endpoints  |

---

# 🔄 How SkillSwap Works

```text
                    ┌─────────────────────┐
                    │     Student        │
                    │     Registers      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Create Profile    │
                    │                     │
                    │ Skills I Teach      │
                    │ Skills I Want       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Search Students   │
                    │     by Skill        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Send Swap Request  │
                    └──────────┬──────────┘
                               │
                       ┌───────┴────────┐
                       ▼                ▼
                  ┌─────────┐      ┌─────────┐
                  │ Accept  │      │ Decline │
                  └────┬────┘      └─────────┘
                       │
                       ▼
                ┌───────────────┐
                │ Complete Swap │
                └───────┬───────┘
                        │
                ┌───────┴────────┐
                ▼                ▼
        Teacher receives     Learner pays
            credits             credits
                │                │
                └───────┬────────┘
                        ▼
                  ┌───────────┐
                  │   Rating  │
                  └───────────┘
```

---

# 💳 Credit Bartering System

SkillSwap does not use direct monetary payments.

Instead, it uses **Skill Credits**.

### Initial Credits

Every new user starts with:

```text
10 Skill Credits
```

### Teaching

When a user teaches another student:

```text
Teacher → receives Credits
Learner  → pays Credits
```

### Example

Suppose Alice teaches Python to Bob for 5 credits.

```text
Before:

Alice = 15 credits
Bob   = 10 credits

After:

Alice = 20 credits
Bob   = 5 credits
```

The transaction is recorded in the database.

### Important Rule

Credits can only be earned through teaching.

```text
No credit purchasing
No monetary payment
No direct money exchange
```

---

# 🏗️ System Architecture

SkillSwap follows a three-layer web application architecture.

```text
┌─────────────────────────────────────────┐
│              FRONTEND                   │
│                                         │
│ HTML5 + CSS3 + JavaScript               │
│ Fetch API / AJAX                        │
└──────────────────┬──────────────────────┘
                   │
                   │ HTTP Requests
                   ▼
┌─────────────────────────────────────────┐
│              BACKEND                    │
│                                         │
│ Python 3.10                             │
│ Flask Framework                         │
│ REST API                                │
│ Authentication                          │
│ Business Logic                          │
└──────────────────┬──────────────────────┘
                   │
                   │ PyMongo
                   ▼
┌─────────────────────────────────────────┐
│              DATABASE                   │
│                                         │
│ MongoDB                                 │
│ skillswap_db                            │
│                                         │
│ users                                   │
│ swap_requests                           │
│ transactions                            │
│ ratings                                 │
└─────────────────────────────────────────┘
```

---

# 🛠️ Technology Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API
* AJAX
* Responsive Design
* Glassmorphism UI

## Backend

* Python 3.10
* Flask
* Flask-CORS
* REST API
* PyMongo
* bcrypt

## Database

* MongoDB
* MongoDB Compass
* Local MongoDB Server
* Database: `skillswap_db`

## Development Tools

* Visual Studio Code
* MongoDB Compass
* Postman / cURL
* Git
* GitHub

---

# 🗄️ Database Design

Database name:

```text
skillswap_db
```

The application uses four main MongoDB collections.

## 1. users

Stores student profile information.

Example fields:

```text
user_id
name
email
credits
skills_offer
skills_want
rating_avg
```

---

## 2. swap_requests

Stores skill exchange requests.

Example fields:

```text
request_id
requester_id
receiver_id
skill_offered
skill_requested
credits_proposed
status
created_at
```

Possible request statuses:

```text
pending
accepted
declined
completed
```

---

## 3. transactions

Stores credit transfer history.

Example fields:

```text
transaction_id
teacher_id
learner_id
credits_exchanged
swap_request_id
created_at
```

---

## 4. ratings

Stores reviews submitted after completed swaps.

Example fields:

```text
rating_id
reviewer_id
reviewed_id
rating
comment
created_at
```

Rating range:

```text
1 to 5 stars
```

---

# 🔌 REST API

The Flask backend provides REST API endpoints for application functionality.

| Method | Endpoint                          | Purpose                            |
| ------ | --------------------------------- | ---------------------------------- |
| POST   | `/api/register`                   | Create a new user                  |
| POST   | `/api/login`                      | Authenticate user                  |
| GET    | `/api/users`                      | Get all users                      |
| GET    | `/api/users/<id>`                 | Get specific user                  |
| PUT    | `/api/users/<id>`                 | Update user profile                |
| GET    | `/api/search?skill=python`        | Search users by skill              |
| POST   | `/api/swap-request`               | Create swap request                |
| GET    | `/api/swap-requests/<user_id>`    | Get user's requests                |
| PUT    | `/api/swap-request/<id>/accept`   | Accept request                     |
| PUT    | `/api/swap-request/<id>/decline`  | Decline request                    |
| PUT    | `/api/swap-request/<id>/complete` | Complete swap and transfer credits |
| GET    | `/api/transactions/<user_id>`     | Get transaction history            |
| POST   | `/api/rating`                     | Submit rating                      |
| GET    | `/api/leaderboard`                | Get top users                      |
| GET    | `/api/notifications/<user_id>`    | Get notifications                  |

---

# 📂 Project Structure

Recommended project structure:

```text
SkillSwap/
│
├── app.py
├── requirements.txt
├── README.md
│
├── frontend/
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   │
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── backend/
│   ├── routes/
│   ├── models/
│   └── utils/
│
├── database/
│   └── sample_data.json
│
└── screenshots/
    ├── login.png
    ├── dashboard.png
    ├── profile.png
    ├── search.png
    ├── requests.png
    ├── transactions.png
    └── leaderboard.png
```

> Adjust this structure to match your actual folders. Do not create README folders that do not exist in your repository.

---

# 🎨 User Interface

The application provides a modern responsive interface.

### Main UI Components

* Login page
* Registration page
* Student dashboard
* Profile management
* Skill search
* Swap request interface
* Credit balance
* Transaction history
* Rating interface
* Leaderboard
* Notifications
* Collapsible navigation sidebar

### UI Design

The interface uses:

* Responsive layout
* Glassmorphism-inspired cards
* Dashboard components
* Interactive buttons
* Search and filtering
* Dynamic content updates
* Mobile-friendly layout

---

# 🔐 Authentication & Security

SkillSwap implements session-based authentication.

### Security features include:

* User registration
* Login authentication
* Session management
* Password hashing using `bcrypt`
* Protected user-specific operations
* Backend validation

Passwords should never be stored as plain text in a production deployment.

---

# ⚙️ Installation

## Step 1: Install Python

Install Python 3.8 or newer.

Verify:

```bash
python --version
```

Recommended:

```text
Python 3.10+
```

---

## Step 2: Install MongoDB

Install MongoDB Community Edition.

Start the MongoDB service on Windows:

```bash
net start MongoDB
```

Default MongoDB connection:

```text
mongodb://localhost:27017
```

---

## Step 3: Install MongoDB Compass

Open MongoDB Compass and connect to:

```text
mongodb://localhost:27017
```

Create:

```text
Database: skillswap_db
```

Collections:

```text
users
swap_requests
transactions
ratings
```

---

# 🐍 Step 4: Create Virtual Environment

Open the project folder in VS Code.

Run:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

---

# 📦 Step 5: Install Dependencies

Run:

```bash
pip install flask flask-cors pymongo bcrypt
```

Or, if `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

## Step 1: Start MongoDB

```bash
net start MongoDB
```

---

## Step 2: Verify MongoDB

Open MongoDB Compass.

Connect to:

```text
mongodb://localhost:27017
```

Verify:

```text
skillswap_db
```

exists.

---

## Step 3: Start Flask Backend

From the project directory:

```bash
python app.py
```

The Flask server should run on:

```text
http://localhost:5000
```

---

## Step 4: Start Frontend

Open the frontend using VS Code Live Server or your configured frontend method.

For example:

```text
index.html
```

The frontend communicates with the Flask REST API.

---

# 🧪 Testing

The project can be tested through:

* Browser
* Postman
* cURL
* MongoDB Compass

### Functional Testing

Test the following workflow:

```text
Register
   ↓
Login
   ↓
Create Profile
   ↓
Add Skills
   ↓
Search Students
   ↓
Send Swap Request
   ↓
Accept Request
   ↓
Complete Swap
   ↓
Transfer Credits
   ↓
Create Transaction
   ↓
Submit Rating
   ↓
Update Leaderboard
```

---

# 🧪 API Testing Example

### Register User

```http
POST /api/register
```

Example request:

```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "password": "your-password",
  "skills_offer": ["Python", "Java"],
  "skills_want": ["UI/UX Design"]
}
```

---

### Login

```http
POST /api/login
```

Example:

```json
{
  "email": "alice@example.com",
  "password": "your-password"
}
```

---

### Search by Skill

```http
GET /api/search?skill=python
```

---

### Send Swap Request

```http
POST /api/swap-request
```

Example:

```json
{
  "requester_id": "USER_ID",
  "receiver_id": "USER_ID",
  "skill_offered": "Python",
  "skill_requested": "Photoshop",
  "credits_proposed": 5
}
```

---

# 📊 Example User Workflow

Suppose:

```text
Alice teaches Python
Bob wants to learn Python
```

Alice creates a skill profile:

```text
Skills I Teach:
Python
Java
```

Bob searches:

```text
Python
```

Bob finds Alice and sends a swap request.

Alice accepts the request.

After the session:

```text
Alice: +5 credits
Bob:   -5 credits
```

The system then:

```text
1. Updates credit balances
2. Creates transaction record
3. Marks swap as completed
4. Allows rating
5. Updates leaderboard
6. Creates notification
```

---

# 🔔 Notification System

The application provides notifications for important events such as:

* New swap request
* Swap request accepted
* Swap request declined
* Swap completed
* Credit transfer
* Rating activity

Notifications are retrieved through:

```http
GET /api/notifications/<user_id>
```

---

# 🏆 Leaderboard

SkillSwap includes a leaderboard that displays top-performing users.

Ranking can consider:

* Skill Credits
* User ratings
* Completed swaps

Example:

```text
🏆 SkillSwap Leaderboard

1. Alice       120 Credits ⭐ 4.9
2. David       105 Credits ⭐ 4.8
3. Carol        95 Credits ⭐ 4.7
4. Emma         82 Credits ⭐ 4.6
5. Bob           75 Credits ⭐ 4.5
```

---

# 📸 Screenshots

Add screenshots of your actual application here.

Recommended screenshots:

### Login

```text
screenshots/login.png
```

### Dashboard

```text
screenshots/dashboard.png
```

### Skill Search

```text
screenshots/search.png
```

### Swap Requests

```text
screenshots/requests.png
```

### Transaction History

```text
screenshots/transactions.png
```

### Leaderboard

```text
screenshots/leaderboard.png
```

Example Markdown:

```markdown
## 📸 Screenshots

### Login
![Login](screenshots/login.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Skill Search
![Search](screenshots/search.png)

### Swap Requests
![Requests](screenshots/requests.png)

### Transaction History
![Transactions](screenshots/transactions.png)

### Leaderboard
![Leaderboard](screenshots/leaderboard.png)
```

---

# 🔮 Future Enhancements

The current version provides the core SkillSwap functionality. Future versions can include:

### 🔥 Real-Time Features

* Firebase integration
* WebSocket notifications
* Live chat
* Real-time dashboard updates

### 🎥 Online Learning

* Video call integration
* Online teaching sessions
* Screen sharing
* Session scheduling

### 📧 Account Management

* Email verification
* Password reset
* Email notifications
* Two-factor authentication

### 🏅 Gamification

* Skill verification badges
* Achievement system
* Learning streaks
* XP system
* Monthly leaderboard rewards

### 📱 Mobile Application

A mobile version can be developed using:

```text
React Native
```

### 👥 Group Learning

Future versions can support:

* Group skill sessions
* Multiple learners
* Multiple instructors
* Group challenges

---

# 🧠 Learning Outcomes

This project provided practical experience in:

### Backend Development

* Python
* Flask
* REST API development
* HTTP methods
* API routing
* Backend validation

### Database Development

* MongoDB
* NoSQL data modeling
* Collections
* CRUD operations
* PyMongo
* Transaction records

### Frontend Development

* HTML5
* CSS3
* JavaScript
* Fetch API
* AJAX
* Responsive UI

### Software Engineering

* Full-stack application architecture
* Authentication
* API integration
* Database integration
* Error handling
* Project structure
* Testing
* Git and GitHub

---

# 📈 Project Highlights

```text
15+ REST API Endpoints
4 MongoDB Collections
10+ Major Features
Credit-Based Bartering System
Session-Based Authentication
Password Hashing
Responsive Dashboard
Search & Filtering
Swap Management
Transaction Tracking
Rating System
Leaderboard
Notifications
```

---

# 🚀 Project Status

```text
Status: Completed Core Implementation
```

The current version demonstrates the complete core workflow of a student skill bartering platform using:

```text
HTML
CSS
JavaScript
        ↓
Flask REST API
        ↓
PyMongo
        ↓
MongoDB
```

---

# 👩‍💻 Project Information

### Project

**SkillSwap: Peer-to-Peer Skill Bartering Platform**

### Type

Full-Stack Web Application

### Developed Using

```text
Python
Flask
MongoDB
PyMongo
HTML5
CSS3
JavaScript
bcrypt
Fetch API
```

### Academic Context

University Software / Database / Full-Stack Development Project

### Developer

**Humna Nawaz**



# 📄 License

This project was developed for educational and academic purposes.

You may use the project for learning and reference with appropriate attribution.

---

<div align="center">

### 🔄 SkillSwap

**Teach a Skill. Earn Credits. Learn Something New.**

⭐ If you find this project useful, consider giving it a star!

</div>
