from flask import Flask, render_template

app = Flask(__name__)

import json
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=I5zlMkrXLLvEXm3MFi0F7kZN00sVSTnnVIt0AqIz"


data = requests.get(url)
# print(data.text, end='\n')
datas = data.text

@app.route('/')
def hello_world():
    return render_template("index.html", datas="datas",name="Admin")

@app.route('/profile')
def profile():
    return render_template("profile.html", name="User")

if __name__ == "__main__":
    app.run(debug=True)