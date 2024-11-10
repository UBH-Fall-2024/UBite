from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_jwt_extended import JWTManager
from authentication import registerUser, loginUser
import sqlite3

app = Flask(__name__, template_folder='../templates')

# Secret key to encode JWT
app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)

# Dummy user storage (you can use a database in production)
users = {}
food_submission = {}

def component_submit(request, json_key, redirect_path, html_path):
    if request.method == "POST":
        data = request.get_json()
        if json_key in data:
            user_input = data[json_key]
            food_submission[json_key] = user_input
            return redirect(url_for(redirect_path, location = redirect_path))
        else:
            return jsonify({"error": "Missing key in JSON data"}), 400

    return render_template(html_path)

def addToDb():
    # do stuff
    return redirect(url_for("tracker", location = "tracker"))


def addtoTracker(food_data):
    pass

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")

@app.route("/profile", methods = ["GET"])
def t():
    pass # return profile page with info such as today's calories, and lifetime calories

@app.route("/qr-add", methods = ["GET"])
def z():
    pass


@app.route("/log-food", methods = ["GET"])
def log_redirect():
    return redirect(url_for("locations"))

@app.route("/locations", methods=["GET", "POST"], endpoint="locations")
def location_submit():
    return component_submit(request, "location", "restaurant-names", "index.html")

@app.route("/restaurant-names", methods = ["GET", "POST"], endpoint = "restaurant-names")
def restaurant_submit():
    print("at restaurants")
    return component_submit(request, "restaurant", "food-names", "index.html")

@app.route("/food-names", methods = ["GET"], endpoint = "food-names")
def food_submit():
    print("at foods")

    return render_template("index.html")

@app.route("/add-to-tracker", methods=["POST"])
def add_and_redirect():
    data = request.get_json()
    print("Received Data:", data)
    print("at adding")
    print("Food submission:", food_submission)
    
    food_submission["restaurant"] = "Champa"
    restaurant = food_submission["restaurant"]
    food = data["food"]
    
    result = {
        "restaurant": restaurant,
        "food": food["name"],
        "calories": food["calories"],
        "fat": food["fat"],
        "cholesterol": food["cholesterol"],
        "sodium": food["sodium"],
        "carb": food["carb"],
        "protein": food["protein"],
        "halal": food["halal"]  # Ensure halal is stored as 0 or 1
    }

    # Connect to the SQLite database
    conn = sqlite3.connect('calorie_tracker.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS food_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        restaurant TEXT,
                        food TEXT,
                        calories INTEGER,
                        fat INTEGER,
                        cholesterol INTEGER,
                        sodium INTEGER,
                        carb INTEGER,
                        protein INTEGER,
                        halal BOOLEAN,
                        date TEXT DEFAULT CURRENT_DATE)''')

    try:
        # Insert a new entry without checking for duplicates
        cursor.execute('''INSERT INTO food_logs (user_id, restaurant, food, calories, fat, cholesterol, sodium, carb, protein, halal)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (1, result["restaurant"], result["food"], result["calories"], result["fat"], result["cholesterol"],
                        result["sodium"], result["carb"], result["protein"], result["halal"]))
        print("Inserted new entry for food:", result["food"])

        # Commit the transaction
        conn.commit()

    except Exception as e:
        print("Error during database operation:", e)
        conn.rollback()

    # Fetch the updated user history
    cursor.execute('''SELECT id, restaurant, food, calories, fat, cholesterol, sodium, carb, protein, halal, date 
                      FROM food_logs 
                      WHERE user_id = ? 
                      ORDER BY date DESC''', (1,))
    
    food_history = cursor.fetchall()

    # Format the history data
    history_data = [
        {
            "id": entry[0],
            "restaurant": entry[1],
            "food": entry[2],
            "calories": entry[3],
            "fat": entry[4],
            "cholesterol": entry[5],
            "sodium": entry[6],
            "carb": entry[7],
            "protein": entry[8],
            "halal": entry[9],
            "date": entry[10]
        }
        for entry in food_history
    ]

    # Calculate total accumulated calories for the user
    cursor.execute("""SELECT SUM(calories) FROM food_logs WHERE user_id = ?""", (1,))
    total_calories = cursor.fetchone()[0] or 0

    # Close the database connection
    conn.close()

    # Return the updated history and total calories as a JSON response
    return {
        "status": "success",
        "history": history_data,
        "total_calories": total_calories
    }



@app.route("/tracker", methods = ["GET"])
def getTracker():
    
    # get profile info from database or something?
    
    return("index.html")
    
    

# Registration endpoint
@app.route("/register", methods=["POST"])
def register():
    return registerUser()

# Login endpoint
@app.route("/login", methods=["POST"])
def login():
    return loginUser()

if __name__ == "__main__":
    app.run(debug=True)
