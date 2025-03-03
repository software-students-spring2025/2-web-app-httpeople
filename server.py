from flask import Flask, render_template, request, redirect, session
from db import db
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST" and request.form.get("recipe_name"):
        name = request.form.get("recipe_name")
        recipes = db.recipes.find({"name": name})
    else:
        recipes = db.recipes.find({})
        
    return render_template("search.html", recipes=recipes)

@app.route("/save/<item_id>", methods=["GET"])
def save(item_id):
    if not session.get("user_id"):
        return redirect(f"/recipe/{item_id}")
    single_recipe = db.recipes.find_one({"_id": ObjectId(item_id)})

    # Create saved_by if not exist
    if not single_recipe.get("saved_by"):
        single_recipe["saved_by"] = []

    if ObjectId(session.get("user_id")) not in single_recipe["saved_by"]:
        single_recipe["saved_by"].append(ObjectId(session.get("user_id")))
        db.recipes.update_one( {
            { "_id": ObjectId(item_id) }, # match criteria
            {
                "$set":{
                    "saved_by": single_recipe["saved_by"],
                }
            }
        })
    return redirect(f"/recipe/{item_id}")

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
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        steps = request.form.get("steps").split("\r\n")
        ingredients = request.form.get("ingredients").split("\r\n")
        single_recipe = db.recipes.find_one({"_id": ObjectId(id)})
        recipes = db.recipes
        new_values = {"$set": {'name': name, 'description': description, 'steps': steps, 'ingredients': ingredients}}
        recipes.update_one(single_recipe, new_values)
        return redirect(f"/recipe/{str(single_recipe["_id"])}")
    # render template for recipe html editing
    return render_template("recipeedit.html", id=id)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if db.users.find_one({"username": username, "password": password}) is not None:
            user = db.users.find_one({"username": username, "password": password}) 
            session['user_id'] = str(user["_id"])
            print(session['user_id'])
            return redirect("/home")
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
        user = db.users.insert_one(user)
        session["user_id"] = str(user.inserted_id)
        return redirect("/home")
    # return profile page
    return render_template("signup.html")

@app.route("/profilepage")
def profile():

    # would return user page html template here
    return render_template("profilepage.html")

app.run(debug=True)