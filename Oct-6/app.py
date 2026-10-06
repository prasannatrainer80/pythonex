from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# JWT configuration
app.config["JWT_SECRET_KEY"] = "my-super-secret-key"
jwt = JWTManager(app)


# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="jwt_demo"
    )


# --------------------------------------------------
# REGISTER
# --------------------------------------------------
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({
            "message": "All fields are required"
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    # Check existing user
    cursor.execute(
        "SELECT id FROM users WHERE username=%s OR email=%s",
        (username, email)
    )

    if cursor.fetchone():
        cursor.close()
        connection.close()

        return jsonify({
            "message": "Username or email already exists"
        }), 409

    # Hash password
    hashed_password = generate_password_hash(password)

    cursor.execute(
        """
        INSERT INTO users(username, password, email)
        VALUES(%s, %s, %s)
        """,
        (username, hashed_password, email)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "User registered successfully"
    }), 201


# --------------------------------------------------
# LOGIN
# --------------------------------------------------
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE username=%s",
        (username,)
    )

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if not user:
        return jsonify({
            "message": "Invalid username or password"
        }), 401

    # Verify password
    if not check_password_hash(user["password"], password):
        return jsonify({
            "message": "Invalid username or password"
        }), 401

    # Create JWT token
    access_token = create_access_token(
        identity=str(user["id"])
    )

    return jsonify({
        "message": "Login successful",
        "access_token": access_token
    })


# --------------------------------------------------
# PROTECTED PROFILE
# --------------------------------------------------
@app.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = get_jwt_identity()

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, username, email FROM users WHERE id=%s",
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    return jsonify(user)


# --------------------------------------------------
# PROTECTED HOME
# --------------------------------------------------
@app.route("/home", methods=["GET"])
@jwt_required()
def home():

    user_id = get_jwt_identity()

    return jsonify({
        "message": "Welcome to protected API",
        "user_id": user_id
    })


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)