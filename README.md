# Library-Management-System-API
A Flask-based REST API for managing a library system, developed for the "Better Software" company as an assessment. The API enables CRUD operations for books and members and includes features like search functionality, pagination, and token-based authentication for secure access.

Overview
This project is a Flask-based API for a Library Management System. It supports CRUD operations for books and members, search functionality for books by title or author, pagination, and token-based authentication.

How to Run the Project
Clone the repository:

git clone <https://github.com/hvv333/Library-Management-System-API/tree/main>
cd Library-Management-System-API>
Install Python (if not installed) and run the application:
python app.py
Access the API at http://127.0.0.1:5000.

Design Choices
Framework: Flask was chosen for its simplicity and lightweight nature.
Authentication: Token-based authentication ensures secure access to the API.
Pagination: Added for efficient handling of large data sets.

Assumptions and Limitations
Tokens: The token is hardcoded (secrettoken). This should be replaced with a dynamic authentication mechanism in production.
Data Storage: In-memory storage (books and members lists) is used for simplicity. Use a database for scalability.
