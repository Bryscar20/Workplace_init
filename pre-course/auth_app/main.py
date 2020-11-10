from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
url_api = "https://api.themoviedb.org/3/movie/550?api_key=4c20948fcb0bf4dd17dfd9e4b05423bc"
data  = requests.get(url_api)
n_Data = json.loads(data.text)

@app.route('/')
def hello_world():
    return render_template("index.html", n_data="n_data", name="Admin")

if __name__ == "__main__":
    app.run(debug=True)