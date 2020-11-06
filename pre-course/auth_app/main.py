from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", posts=posts, name="Admin")

@app.route('/profile')
def profile():
    return render_template("profile.html", name="User")

if __name__ == "__main__":
    app.run(debug=True)