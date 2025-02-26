from flask import Flask, render_template
from db import db

app = Flask(__name__)


@app.route('/')
def homepage():
    pass  # put HTML for homepage here, with return render_template('homepage.html') or whatever the homepage is called

@app.route("/search")
def search():
    recipes = db.recipes.find({})
    print(recipes)
    print(recipes[0]["name"])
    return render_template("search.html", recipes=recipes)

app.run(debug=True)