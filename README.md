# FastAPI LMS – Learning Project

This project is my personal practice repo built by following a YouTube tutorial from Faraday Academy. 
The original tutorial repo and video can be found here: YouTube Tutorial: https://youtu.be/gQTRsZpR7Gw

Original Repo: Fast API LMS [Faraday Academy](https://github.com/FaradayAcademy/fastapi-lms)

I used the tutorial as the foundation, then rebuilt and modified parts of the project while following along. 
My goal was to understand real FastAPI structure, database migrations, async patterns, and proper API design.

---

## About This Project

This project is part of my learning journey with FastAPI, PostgreSQL, SQLAlchemy, and backend development as a whole.
I followed the tutorial and extended some parts to understand:

- API structuring
- Database modeling
- Alembic migrations
- Async and sync database sessions
- Environment variable management
- Linting and formatting with Pre-commit, Black, and Flake8
- Handling real development issues (Python version conflicts, migration setup, etc.)

---

## Tech Stack

- **FastAPI**
- **Python 3.12**
- **PostgreSQL**
- **SQLAlchemy 1.4+**
- **Alembic**
- **Pydantic**
- **Poetry**
- **Black**
- **Flake8**
- **Pre-commit**

---

## Project Capabilities

This Learning Management System allows:

### Teacher Features
- CRUD operations on students
- Create courses with sections
- Add detailed content blocks to sections
- Assign courses to students
- Track student progress
- Grade content blocks and provide feedback

### Student Features
- View enrolled courses
- Explore course sections and content
- Track learning progress
- Submit content or tasks for grading

---

## Running the Project Locally

### **Requirements**
Make sure the following are installed:

- Python 
- Poetry
- PostgreSQL (running)

### **1. Clone the Repository**
```sh
git clone https://github.com/AJ-254/fast-api-lms
cd fast-api-lms
```

### **2. Create and Activate Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
source venv/Scripts/activate   # Bash
venv\Scripts\Activate.ps1      # Powershell
```

### **3. Install Dependencies**
```sh
poetry install
```

### **4. Set Up Environment Variables**
Create a .env file:
```ini
POSTGRES_USER=yourusername
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=fast_lms
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### **5. Run Database Migrations**
```sh
alembic upgrade head
```

### **6. Start the Server**
```sh
uvicorn main:app --reload
```

---

## Tech Stack

- FastAPI

- Python 3.12

- Poetry

- PostgreSQL

- SQLAlchemy

- Alembic

- Pydantic

- Black

- Flake8

- pre-commit

---

## Database Schema Overview

### **User**

- email: str

- role: enum (student, teacher)

- is_active: bool

### **Profile**

- first_name

- last_name

- bio (text)

- user_id (FK)

### **Course**

- title

- description (text)

- user_id (FK)

### **Section**

- title

- description

- course_id (FK)

### **ContentBlock**

- title

- description

- type

- url

- content

- section_id (FK)

### **StudentCourse**

- Tracks student enrollment and completion.

- student_id

- course_id

- completed (bool)

### **CompletedContentBlock**

- Tracks what each student has completed.

- student_id

- content_block_id

- url

- feedback

- grade

---

## Credits

This project is based on the FastAPI LMS tutorial by Faraday Academy on YouTube. 
I rebuilt the system for learning purposes and added my own workflow setup using 
Poetry, environment variables, linting, and pre-commit tools.


