from flask import Flask,render_template,flash, redirect,url_for,session,logging,request

app = Flask(__name__)
app.config['SECRET_KEY'] = '81920bd700541c2643206d1097bfdea4a781dfb7'

@app.route("/")
def hello_world():
    title = "WELCOME - HomePage"
    return render_template("index.html", n_data="n_data", name="Admin", title=title)

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
    title = "WELCOME - About Page"
    return render_template("about.html", title=title)

@app.route("/services")
def services():
    title = "WELCOME - Services Page"
    return render_template("services.html", title=title)

@app.route("/services")
def services():
    title = "WELCOME - Contact Page"
    return render_template("services.html", title=title)
    
if __name__ == "__main__":
    app.run(debug=True)