# API from Scratch with Flask and MongoDB

This project demonstrates how to create a RESTful API from scratch using Python, Flask, and MongoDB. The API includes CRUD operations and serves as a guide for building your own backend services.

---

## What is an API?
An **API (Application Programming Interface)** allows software applications to communicate with each other. In the context of web development, a **RESTful API** enables clients (like web browsers, mobile apps, or other systems) to perform operations on a server using HTTP methods such as:
- `GET`: Retrieve data.
- `POST`: Create new data.
- `PUT`: Update existing data.
- `DELETE`: Remove data.

For example, when you use a weather app, it fetches data from a server using an API.

---

## What is Flask?
Flask is a lightweight and easy-to-use web framework for Python. It allows developers to quickly build web applications and APIs without the overhead of more complex frameworks. Flask is often used for its simplicity, flexibility, and ability to scale small projects or microservices into production-ready solutions.

Key features of Flask:
- Minimal and modular design.
- Supports extensions for additional functionality (e.g., authentication, database integration).
- Easy to learn and widely supported by a large community.

---

## Features of This API
- **Create**: Add new users to the database.
- **Read**: Retrieve all users or a specific user by ID.
- **Update**: Modify an existing user's details.
- **Delete**: Remove a user from the database.

---

## Requirements
- Python 3.7+
- Flask
- Flask-PyMongo
- MongoDB (local or cloud-based, e.g., MongoDB Atlas)

---

## Setup Guide

### 1. Install MongoDB
- For local use, download MongoDB Community Edition from [MongoDB Download Center](https://www.mongodb.com/try/download/community).
- Alternatively, set up a cloud database using [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

### 2. Clone or Download the Repository
Download the code or clone the repository.

### 3. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate  # Windows
```

### 4. Install Dependencies
```bash
pip install flask flask-pymongo
```

### 5. Update MongoDB Connection
Edit the `app.py` file and replace the MongoDB URI:
```python
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"  # Update with your MongoDB URI
```
For MongoDB Atlas, use a URI like:
```python
"mongodb+srv://<username>:<password>@cluster.mongodb.net/mydatabase"
```

---

## Running the API
1. Activate the virtual environment:
   ```bash
   source venv/bin/activate # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
2. Start the Flask app:
   ```bash
   python app.py
   ```
3. The API will be accessible at `http://127.0.0.1:5000`.

---

## API Endpoints

### 1. **GET /users**
Retrieve a list of all users.
- **Response**: JSON array of users.

### 2. **GET /users/<id>**
Retrieve details of a specific user by their ID.
- **Response**:
  - `200 OK`: User data.
  - `404 Not Found`: User not found.

### 3. **POST /users**
Create a new user.
- **Request Body** (JSON):
  ```json
  {
      "name": "John Doe",
      "email": "john@example.com"
  }
  ```
- **Response**:
  - `201 Created`: New user data.
  - `400 Bad Request`: Missing name or email.

### 4. **PUT /users/<id>**
Update an existing user's details.
- **Request Body** (JSON):
  ```json
  {
      "name": "Jane Doe",
      "email": "jane@example.com"
  }
  ```
- **Response**:
  - `200 OK`: Updated user data.
  - `404 Not Found`: User not found.

### 5. **DELETE /users/<id>**
Delete a user by their ID.
- **Response**:
  - `200 OK`: Confirmation message.
  - `404 Not Found`: User not found.

---

## Testing the API
You can test the API using:
1. **cURL**:
   ```bash
   curl http://127.0.0.1:5000/users
   ```
2. **Postman**: Import the endpoints and send requests.
3. **Browser**: Open `http://127.0.0.1:5000/users` to view the data.

---

## Next Steps
- Add **pagination** for large datasets.
- Implement **authentication** (e.g., JWT).
- Add API **documentation** using Swagger.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it for your own projects!
