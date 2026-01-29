# 🎓 University Portal – NoSQL Microservices Project

> **Grade Achieved:** 26/25 (Full Mark + 1 Bonus) 🏆

[![View Presentation Slides](https://img.shields.io/badge/View-Presentation_Slides-orange?style=for-the-badge&logo=google-slides)](https://docs.google.com/presentation/d/10YWJVZLwyYicIv-txMq9Ungv3EtfcPNXBfHtkPSRHBw/edit?usp=sharing)

---

## 📌 Project Overview
This project is a comprehensive **University Portal** built to demonstrate the power and flexibility of **NoSQL systems**. It integrates multiple non-relational databases (MongoDB, Redis, Neo4j, InfluxDB) into a microservices architecture to handle distinct data requirements—from social networking to high-velocity activity logging.

### 🎯 Goal
The main goal of this project is to demonstrate the ability to:
* **Analyze** data requirements.
* **Select** appropriate NoSQL database types and management systems.
* **Design** data models and queries.
* **Implement** a small prototype that integrates several database systems.
* **Discuss** trade-offs in system design.

---

## 👥 Team Members
* **Mohamed**
* **Omar**
* **Zuhair**
* **Husam** (Me)

---

## 🏗️ System Architecture
The system follows a **Microservices Architecture** where each service manages its own domain and connects to a specialized database.

### 🔌 Services & Data Stores
| Service | Database | Type | Responsibility |
| :--- | :--- | :--- | :--- |
| **Auth & User Service** | **Redis** & **MongoDB** | Key-Value / Doc | Manages temporary auth tokens/sessions and user accounts. |
| **Student Information** | **MongoDB** | Document | Stores and queries student data, programs, courses, and grades. |
| **Course Activity** | **InfluxDB** | Time-Series | Records daily/weekly activities (e.g., logins, quizzes, submissions). |
| **Academic Network** | **Neo4j** | Graph | Represents relationships between students, instructors, and courses. |
| **Analytics** | **MongoDB** / **Influx** | Aggregation | Generates summaries (e.g., top courses per semester, most active students). |

---

## 📂 Project Structure
```text
UNIVERSITY-PORTAL-MAIN/
├── menus/                  # CLI/Menu interfaces for different roles
│   ├── dean.py             # Dean functionalities
│   ├── instructor.py       # Instructor functionalities
│   ├── student.py          # Student functionalities
├── services/               # Microservices logic
│   ├── auth_user_service.py
│   ├── academic_network_service.py
│   ├── analytics_service.py
│   ├── fetch_all_data.py
├── venv/                   # Virtual Environment (Ignored in Git)
├── docker-compose.yml      # Container orchestration
├── main.py                 # Application entry point
└── requirements.txt        # Python dependencies
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.9+
- Docker & Docker Compose

### Installation

Clone the repository:
```bash
git clone https://github.com/hosam221/University-Portal.git
cd University-Portal
```

Start the Database Container Cluster:
```bash
docker-compose up -d
```

Install Python Dependencies:
```bash
pip install -r requirements.txt
```

Run the Application:
```bash
python main.py
```

---

## 📋 Project Tasks Implemented

### 1. Requirement Analysis and Database Selection
- Identified main data entities (Users, Courses, Logs, Relationships).
- Justified selections: MongoDB for flexible documents, Neo4j for complex relationships, Redis for fast caching, InfluxDB for time-series logs.

### 2. System Architecture
- Designed an overall architecture showing interaction between Client Layer, API Gateway, and Microservices Layer.
- Defined data flow and connection strategies.

### 3. Data Modeling and Implementation
- Designed schemas/models for each NoSQL database.
- Loaded sample data (Seeding scripts included).
- Implemented CRUD operations and complex aggregation queries.

### 4. Integration and Demonstration
- Built a prototype interface (CLI menus) for Deans, Instructors, and Students.
- Demonstrated data retrieval combining information from multiple sources (e.g., Student Profile).

### 5. Discussion & Trade-offs
- Addressed system design trade-offs (Consistency vs. Availability).
- Implemented caching layers to optimize read performance.

**Bonus:** Demonstrated creativity in design and functionality.

---

Created for the **Non Relational Database Course Project**.
