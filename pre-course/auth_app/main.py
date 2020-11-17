from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '81920bd700541c2643206d1097bfdea4a781dfb7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

@app.route("/")
def hello_world():
    return render_template("index.html", n_data="n_data", name="Admin")

@app.route("/login",methods=["GET", "POST"])
def login():
    title = "WELCOME - Login to Access your Fav Movies"
    return render_template("login.html", title=title)

@app.route("/register", methods=["GET", "POST"])
def register():
    title = "WELCOME - Register to Access your Fav Movies"
    return render_template("register.html", title="title")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(debug=True)