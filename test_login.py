import requests

BASE_URL = "http://127.0.0.1:5000"

def register_user(username, password):
    print("\n--- Register User ---")
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/register", json=data)
    print("Response:", response.json())

def login_user(username, password):
    print("\n--- Login User ---")
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/login", json=data)
    print("Response:", response.json())

if __name__ == "__main__":
    # Register a user
    register_user("admin", "password123")

    # Test login with correct credentials
    login_user("admin", "password123")

    # Test login with incorrect credentials
    login_user("admin", "wrongpassword")

    # Test login with non-existent user
    login_user("nonexistent", "password123")
