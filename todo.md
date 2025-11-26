# FastAPI Layered Architecture — TODO Document

## 🎯 Goal
Implement a clean **3-layer architecture** for a FastAPI application:

1. **Route Layer** → Exposes API endpoints  
2. **Service Layer** → Handles business logic  
3. **Database Layer** → Performs all DB interactions  

---

## 📁 Project Structure

    project/
    │
    ├── app.py # Main FastAPI application entry point
    ├── routes.py # Route layer
    ├── service.py # Business logic layer
    └── database.py # Database operations layer

yaml
Copy code

---

## 🧩 Layer Responsibilities

### 1️⃣ Route Layer (`routes.py`)
- High-level entry for client requests  
- Calls **service layer** functions  
- Returns responses to the client  
- ❌ Contains **no business logic**  
- ❌ Contains **no database calls**

**Handles:**
- `POST /employee`
- `GET /employees`

---

### 2️⃣ Service Layer (`service.py`)
- Contains **all business logic**
- Validates incoming data (optional)
- Calls **database layer** to insert or fetch data
- After fetching data:
  - Filters employees into:
    - **minors** → age `< 18`
    - **adults** → age `>= 18`
  - Returns a structured JSON object

---

### 3️⃣ Database Layer (`database.py`)
- Responsible ONLY for database operations  
- No validations  
- No business rules  

**Functions to implement:**
- `insert_employee(data)`
- `fetch_all_employees()`

---

## 📌 API Requirements

### ➤ POST `/employee`
**Insert employee details into DB:**

| Field | Type    | Required |
|-------|---------|----------|
| name  | string  | yes      |
| age   | integer | yes      |
| email | string  | yes      |

**Flow:**  
`Route → Service → Database → Service → Route`

---

### ➤ GET `/employees`
**Fetch all employee details from DB.**

Service layer must split employees into two groups:

- **male** 
- **female** 

**Expected JSON Output:**
```json
{
  "male": [
    { "name": "Rahul", "age": 16, "email": "rahul@mail.com" }
  ],
  "female": [
    { "name": "Anita", "age": 25, "email": "anita@mail.com" }
  ]
}