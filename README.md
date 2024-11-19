# Login Verification Microservice

This microservice handles user authentication by verifying a username and password. It allows registering new users with securely hashed passwords and validating user credentials during login. The microservice communicates via JSON requests and responses.

---

## Communication Contract
- A. This microservice is for Joo Wang Lee.
- B. THis microservice is finished.
- C. N/A
- D. The code is available in a public github repo and can be ran locally.
- E. They can message me on discord if any issues come up.
- F. Preferably as soon as they can so I can fix any issues. I will be out of town from the 27th to the 31st, but I will have my laptop with me, responses just might take a little longer.
- G. I just hope I explained it well enough and left enough comments.
  
### Base URL
`http://127.0.0.1:5000`

---

### Endpoints

#### **1. `/register` (POST)**
Used to register a new user with a username and password.

##### **Request Format**
- **Method:** `POST`
- **URL:** `/register`
- **Content-Type:** `application/json`
- **Request Body:**
  ```json
  {
      "username": "admin",
      "password": "password123"
  }
  ```
### Response Format
- **On success:**
```json
  {
      "message": "User 'admin' registered successfully!"
  }
```
- **On failure (e.g., duplicate username):**
```json
  {
      "message": "Username already exists. Please choose a different username."
  }
```

#### **2. `/login` (POST)**
Used to verify user credentials and return a success message if the username and password are valid.

##### **Request Format**
- **Method:** `POST`
- **URL:** `/login`
- **Content-Type:** `application/json`
- **Request Body:**
  ```json
  {
      "username": "admin",
      "password": "password123"
  }
  ```
### Response Format
- **On success:**
```json
  {
      "message": "Login successful!",
      "session_token": "abc123xyz456"
  }
```
- **On failure (e.g., duplicate username):**
```json
  {
      "message": "Invalid username or password."
  }
```

---

## How to Programmatically Interact with the Microservice

### Requesting Data
Example for registering a user using Python:
```python
import requests

url = "http://127.0.0.1:5000/register"
data = {
    "username": "admin",
    "password": "password123"
}

response = requests.post(url, json=data)
print(response.json())
```
Example for logging in a user using Python:
```python
import requests

url = "http://127.0.0.1:5000/login"
data = {
    "username": "admin",
    "password": "password123"
}

response = requests.post(url, json=data)
print(response.json())
```

### Receiving Data
When calling the endpoints, the responses are returned as JSON objects. Below is an example of handling the response programmatically:
```python
response = requests.post(url, json=data)

# Ensure the request was successful
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.json())
```

---
## UML Sequence Diagram


---

### Setup Instructions
1. Clone the repository:
git clone 

2. Install dependencies:
pip install flask bcrypt

3. Run the microservice:
python login_service.py

4. Test the microservice with example requests.

Dependencies
- Python 3.x
- Flask
- bcrypt
- SQLite
