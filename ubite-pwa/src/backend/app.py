from flask import Flask, render_template, redirect, url_for, request
from flask_jwt_extended import JWTManager
from authentication import registerUser, loginUser

app = Flask(__name__, template_folder='../../templates')

# Secret key to encode JWT
app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)

# Dummy user storage (you can use a database in production)
users = {}
food_submission = {}

def component_submit(request, form_element, redirect_path, html_path):
    if request.method == "POST":
        user_input = request.form[form_element]
        food_submission[form_element] = user_input
        return redirect(url_for(redirect_path, location = redirect_path))

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
    return component_submit(request, "restaurant", "get-food-data", "index.html")

@app.route("/food-names", methods = ["GET", "POST"], endpoint = "food-names")
def food_submit():
    return component_submit(request, "food", "add-to-tracker", "index.html")

@app.route("/add-to-tracker", methods = ["POST"])
def add_and_redirect():
    restaurant = food_submission["restaurant"]
    food = food_submission["food"]
    result = {}
    
    # query database for food nutrition facts
    
    calories = 1
    fat = 1
    cholesterol = 1
    sodium = 1
    carb = 1
    protein = 1
    halal = True
    
    result["restaurant"] = restaurant
    result["food"] = food
    result["calories"] = calories
    result["fat"] = fat
    result["cholesterol"] = cholesterol
    result["sodium"] = sodium
    result["carb"] = carb
    result["protein"] = protein
    result["halal"] = halal
    
    # add to tracker
    
    
    return addtoTracker(result) # adds and redirects to tracker page
    

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
