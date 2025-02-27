from flask import Flask, render_template, request
from db import db
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST" and request.form.get("recipe_name"):
        name = request.form.get("recipe_name")
        recipes = db.recipes.find({"name": name})
    else:
        recipes = db.recipes.find({})
        
    return render_template("search.html", recipes=recipes)

@app.route("/recipe/<id>")
def recipe(id):
    single_recipe = db.recipes.find_one({"_id": ObjectId(id)})
    return render_template("recipe.html", single_recipe=single_recipe)

@app.route("/home")
def home():
    recipes = db.recipes.find({})
    return render_template("home.html", recipes=recipes)


@app.route("/recipe/<id>/edit", methods=['GET', 'POST'])
def edit(id):
    name = request.form.get("recipe_name")
    description = request.form.get("recipe_description")
    steps = request.form.get("recipe_steps")
    ingredients = request.form.get("recipe_ingredients")
    single_recipe = db.recipes.find_one({"_id": ObjectId(id)})
    single_recipe.name = name
    single_recipe.description = description
    single_recipe.steps = steps
    single_recipe.ingredients = ingredients
    # render template for recipe html editing

@app.route("/login", methods=['GET', 'POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if db.recipes.find_one({"email": email, "password": password}) is not None:
        # direct to profile screen
        pass
    else:
        # return login error
        pass

@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    user = {"username": username, email: "email", password: "password"}
    db.insert_one(user)
    # return profile page

@app.route("/profile")
def profile(username):
    user_profile = db.user.find_one({"username": username})
    # would return user page html template here

app.run(debug=True)