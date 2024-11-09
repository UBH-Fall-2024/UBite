from flask import Flask
from flask_jwt_extended import JWTManager
from authentication import registerUser, loginUser

app = Flask(__name__)

# Secret key to encode JWT
app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)

# Dummy user storage (you can use a database in production)
users = {}

@app.home("/", methods = ["GET"])
def home():
    pass

@app.home("/locations", methods = ["GET"])
def home():
    pass

@app.home("/restaurant-names", methods = ["GET"])
def home():
    pass

@app.home("/get-food-data", methods = ["GET"])
def home():
    pass

@app.home("/add-to-tracker", methods = ["POST"])
def home():
    pass

# Registration endpoint
@app.route("/register", methods=["POST"])
def register():
    return registerUser()

# Login endpoint
@app.route("/login", methods=["POST"])
def login():
    return loginUser()

if __name__ == "__main_@_":
    app.run(debug=True)
