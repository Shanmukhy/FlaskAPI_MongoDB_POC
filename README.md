# User Management REST API using Flask & MongoDB

This is a simple RESTful API for managing user data using Flask (Python) and MongoDB. The API allows you to perform basic CRUD (Create, Read, Update, Delete) operations.

## 🔧 Tech Stack

- **Backend:** Flask (Python)
- **Database:** MongoDB
- **Driver:** PyMongo

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.7+
- MongoDB (running locally on default port `27017`)
- `pip` (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Shanmukhy/FlaskAPI_MongoDB_POC.git
   cd FlaskAPI_MongoDB_POC

2. **Install dependencies**

   ```bash
   pip install flask pymongo
   ```

3. **Run the Flask app**

   ```bash
   python app.py
   ```

   The server will start at: `http://127.0.0.1:5000`

---

## 📦 API Endpoints

### 1. Home Route

* **GET** `/`
* **Description:** Check if API is running
* **Response:**

  ```json
  "API is working"
  ```

---

### 2. Add User

* **POST** `/add_user`
* **Body:**

  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }
  ```
* **Response:**

  ```json
  {
    "message": "User added",
    "id": "mongodb_generated_id"
  }
  ```

---

### 3. Get All Users

* **GET** `/users`
* **Response:**

  ```json
  [
    {
      "_id": "user_id",
      "name": "John Doe",
      "email": "john@example.com",
      "age": 30
    },
    ...
  ]
  ```

---

### 4. Get Single User

* **GET** `/user/<user_id>`

* **Response (Success):**

  ```json
  {
    "_id": "user_id",
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }
  ```

* **Response (Not Found):**

  ```json
  {
    "error": "User not found"
  }
  ```

---

### 5. Update User

* **PUT** `/update_user/<user_id>`
* **Body:** Partial or full user data to update

  ```json
  {
    "email": "new_email@example.com"
  }
  ```
* **Response:**

  ```json
  {
    "message": "User updated successfully"
  }
  ```

---

### 6. Delete User

* **DELETE** `/delete_user/<user_id>`

* **Response (Success):**

  ```json
  {
    "message": "User deleted"
  }
  ```

* **Response (Not Found):**

  ```json
  {
    "message": "User not found"
  }
  ```

---

## 🗃️ Database Structure

* **Database:** `user_db`
* **Collection:** `users`
* **Sample Document:**

  ```json
  {
    "_id": ObjectId("..."),
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }
  ```

---

## 📌 Notes

* This API is meant for local development and testing.
* Ensure MongoDB is running locally or update the MongoDB connection URI accordingly.

---
````
