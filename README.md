# Library Management System API

This is a Flask-based Library Management System API that allows CRUD operations for books and members. It also includes features like search functionality, pagination, and token-based authentication.

---

## Features

- **Books API**: Perform CRUD operations on books, search by title or author, and use pagination.
- **Members API**: Perform CRUD operations on members.
- **Authentication**: Token-based authentication for secure API access.

---

## Prerequisites

1. **Python 3.7+**: Ensure Python is installed on your system.
2. **Pip**: Python package manager.

---

## Setup Instructions

1. Clone the Repository:
   ```bash
   git clone https://github.com/abhigyanpatek/library-management.git
   cd library-management
   ```

2. Create a Virtual Environment:
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/macOS
   env\Scripts\activate    # For Windows
   ```

3. Install Dependencies:
   ```bash
   pip install Flask
   ```

4. Run the Application:
   ```bash
   python app.py
   ```

5. Access the API:
   Open your browser or use a tool like Postman to access the API at `http://127.0.0.1:5000`.

---

## API Endpoints

### Books API

#### **1. Get All Books**
- **URL**: `/books`
- **Method**: `GET`
- **Query Parameters**:
  - `title` (optional): Filter by book title.
  - `author` (optional): Filter by author name.
  - `page` (optional): Pagination page number (default: 1).
  - `limit` (optional): Number of items per page (default: 10).
- **Example**:
  ```bash
  curl -X GET "http://127.0.0.1:5000/books?title=search_title&author=search_author&page=1&limit=10"
  ```

#### **2. Add a Book**
- **URL**: `/books`
- **Method**: `POST`
- **Headers**:
  - `Authorization`: Bearer token (e.g., `Bearer SECRET_TOKEN`).
  - `Content-Type`: `application/json`
- **Body**:
  ```json
  {
    "title": "Book Title",
    "author": "Author Name",
    "published_year": 2024
  }
  ```
- **Example**:
  ```bash
  curl -X POST http://127.0.0.1:5000/books \
  -H "Authorization: Bearer SECRET_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Book Title", "author": "Author Name", "published_year": 2024}'
  ```

#### **3. Update a Book**
- **URL**: `/books/<book_id>`
- **Method**: `PUT`
- **Headers**:
  - `Authorization`: Bearer token.
  - `Content-Type`: `application/json`
- **Body**:
  ```json
  {
    "title": "Updated Title",
    "author": "Updated Author",
    "published_year": 2023
  }
  ```
- **Example**:
  ```bash
  curl -X PUT http://127.0.0.1:5000/books/1 \
  -H "Authorization: Bearer SECRET_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title", "author": "Updated Author", "published_year": 2023}'
  ```

#### **4. Delete a Book**
- **URL**: `/books/<book_id>`
- **Method**: `DELETE`
- **Headers**:
  - `Authorization`: Bearer token.
- **Example**:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/books/1 \
  -H "Authorization: Bearer SECRET_TOKEN"
  ```

### Members API

#### **1. Get All Members**
- **URL**: `/members`
- **Method**: `GET`
- **Example**:
  ```bash
  curl -X GET http://127.0.0.1:5000/members
  ```

#### **2. Add a Member**
- **URL**: `/members`
- **Method**: `POST`
- **Headers**:
  - `Authorization`: Bearer token.
  - `Content-Type`: `application/json`
- **Body**:
  ```json
  {
    "name": "Member Name",
    "email": "member@example.com"
  }
  ```
- **Example**:
  ```bash
  curl -X POST http://127.0.0.1:5000/members \
  -H "Authorization: Bearer SECRET_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Member Name", "email": "member@example.com"}'
  ```

#### **3. Update a Member**
- **URL**: `/members/<member_id>`
- **Method**: `PUT`
- **Headers**:
  - `Authorization`: Bearer token.
  - `Content-Type`: `application/json`
- **Body**:
  ```json
  {
    "name": "Updated Member Name",
    "email": "updated@example.com"
  }
  ```
- **Example**:
  ```bash
  curl -X PUT http://127.0.0.1:5000/members/1 \
  -H "Authorization: Bearer SECRET_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Member Name", "email": "updated@example.com"}'
  ```

#### **4. Delete a Member**
- **URL**: `/members/<member_id>`
- **Method**: `DELETE`
- **Headers**:
  - `Authorization`: Bearer token.
- **Example**:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/members/1 \
  -H "Authorization: Bearer SECRET_TOKEN"
  ```

---

## Notes

1. Replace `<book_id>` and `<member_id>` with the actual IDs.
2. Use `Bearer SECRET_TOKEN` as the token in headers.
3. Ensure to install Python and Flask before running the project.

---

## Limitations

1. This API uses an in-memory data store, meaning data is lost when the server restarts.
2. Authentication is hardcoded and should be replaced with a more secure mechanism in production.
3. The debug mode should only be used in development.

--
