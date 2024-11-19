from flask import Flask, request, jsonify
import sqlite3
import bcrypt

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Create a users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Helper function to register a user
def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return {"message": f"User '{username}' registered successfully!"}, 201
    except sqlite3.IntegrityError:
        return {"message": "Username already exists. Please choose a different username."}, 400
    finally:
        conn.close()

# Helper function to verify a user
def verify_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result is None:
        return False

    # `result[0]` is already in bytes, so no need to encode
    stored_hash = result[0] if isinstance(result[0], bytes) else result[0].encode()
    return bcrypt.checkpw(password.encode(), stored_hash)



# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    response, status = register_user(username, password)
    return jsonify(response), status

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    if verify_user(username, password):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid username or password."}), 401


if __name__ == '__main__':
    init_db()  # Ensure the database is initialized
    app.run(debug=True, port=5000)
