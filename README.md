# 🎓 Student Authorization Management System

## 📌 Project Overview
This project was developed as part of the Advanced Programming course.

The goal is to manage student authorizations, including:
- late arrivals (entry authorization)
- temporary exits during class

The system automatically generates authorizations and sends an email notification to the professor.

---

## 🧱 Project Structure

### 📄 person.py
This file contains the `Person` class, which represents a basic person with:
- last name
- first name
- student ID

It serves as the base class for other components.

---

### 📄 student.py
This file defines the `Student` class, which inherits from `Person`.

It includes:
- field of study
- entry time
- exit time
- automatic detection of lateness

It also includes:
- `__str__` method for formatted display
- `check_late()` static method to calculate delay

---

### 📄 bit_gestion.py
This is the main program file.

It handles:
- admin authentication
- selection of authorization type (entry/exit)
- student data input
- automatic calculations (delay, duration, percentage missed)
- generation of authorization output
- email sending to professors

---

## ⚙️ How it works

1. Admin logs in using password  
2. Select authorization type  
3. Enter student information  
4. System calculates everything automatically  
5. Authorization is displayed and email is sent  

---

## ▶️ How to run the program

```bash
python bit_gestion.py
