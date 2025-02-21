from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    pass  # put HTML for homepage here, with return render_template('homepage.html') or whatever the homepage is called
