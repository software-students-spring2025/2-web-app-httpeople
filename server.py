from flask import Flask, render_template, request, redirect
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

@app.route("/")
def root():
    return redirect("/home")


@app.route("/recipe/<id>/edit", methods=['GET', 'POST'])
def edit(id):
    name = request.form.get("recipe_name")
    description = request.form.get("recipe_description")
    steps = request.form.get("recipe_steps")
    ingredients = request.form.get("recipe_ingredients")
    single_recipe = db.recipes.find_one({"_id": ObjectId(id)})
    recipes = db.httpeople
    new_values = {"$set": {'name': name, 'description': description, 'steps': steps, 'ingredients': ingredients}}
    recipes.update_one(single_recipe, new_values)
    # render template for recipe html editing
    return render_template("recipe.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if db.recipes.find_one({"email": email, "password": password}) is not None:
            # direct to profile screen
            pass
        else:
            # return login error
            pass
    return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        user = {"username": username, "email": email , "password": password}
        db.users.insert_one(user)
        return redirect("/home")
    # return profile page
    return render_template("signup.html")

@app.route("/profilepage")
def profile():

    # would return user page html template here
    return render_template("profilepage.html")

app.run(debug=True)