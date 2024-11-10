from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from dbLookup import retrieve_user

app = Flask(__name__)

# Secret key to encode JWT
app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)

# Dummy user storage (you can use a database in production)
users = {}

def registerUser():
    data = request.get_json()
    if data["email"] in users:
        return jsonify({"message": "Email already registered"}), 400

    hashed_password = generate_password_hash(data["password"])
    users[data["email"]] = hashed_password
    return jsonify({"message": "User registered successfully"}), 201

def loginUser():
    data = request.get_json()
    user = users.get(data["email"])
    
    if user and check_password_hash(user, data["password"]):
        access_token = create_access_token(identity=data["email"])
        calorie_count = retrieve_user(user["email"])
        return jsonify({"message": " Log in successful!", "access_token": access_token, "calories": calorie_count})
    
    return jsonify({"message": "Invalid credentials"}), 401
