from flask import Flask, render_template, request
from db import db
from bson.objectid import ObjectId

app = Flask(__name__)


@app.route('/')
def homepage():
    pass  # put HTML for homepage here, with return render_template('homepage.html') or whatever the homepage is called

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


app.run(debug=True)