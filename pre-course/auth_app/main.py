from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.nasa.gov/planetary/apod?api_key=I5zlMkrXLLvEXm3MFi0F7kZN00sVSTnnVIt0AqIz"

data = requests.get(url)
new_datas = data.json()
datas = {new_datas}

@app.route('/')
def hello_world():
    return render_template("index.html", datas="datas",name="Admin")

@app.route('/profile')
def profile():
    return render_template("profile.html", name="User")

if __name__ == "__main__":
    app.run(debug=True)