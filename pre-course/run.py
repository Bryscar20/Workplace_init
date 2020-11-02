from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    """
    docstring
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)