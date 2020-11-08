from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

with open("sources.json") as data:
    datas = json.load(data)

@app.route('/')
def hello_world():
    return render_template("index.html", datas="datas",name="Admin")

@app.route('/profile')
def profile():
    return render_template("profile.html", name="User")

if __name__ == "__main__":
    app.run(debug=True)