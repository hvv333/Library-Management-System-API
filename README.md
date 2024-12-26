# Library Management System API

A Flask-based REST API for managing a library system, developed for the **"Better Software"** company as an assessment. The API enables CRUD operations for books and members and includes features like search functionality, pagination, and token-based authentication for secure access.

## Overview

This project is a Flask-based API for a Library Management System. It supports:
- CRUD operations for books and members.
- Search functionality for books by title or author.
- Pagination for efficient data handling.
- Token-based authentication for secure access.

---

## A) How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/hvv333/Library-Management-System-API.git
   cd Library-Management-System-API

2. Install Python (if not already installed).

3. Run the application:
   ```bash
   python app.py


---

## B) Design Choices

- Framework : Flask was chosen for its simplicity and lightweight nature.
- Authentication : Token-based authentication ensures secure access to the API.
- Pagination : Added for efficient handling of large data sets.

---

## C) Assumptions and Limitations
- Tokens : The token is hardcoded as secrettoken. This should be replaced with a dynamic authentication mechanism in a production environment.
- Data Storage : In-memory storage (lists for books and members) is used for simplicity. A database should be used for scalability in a real-world application.



