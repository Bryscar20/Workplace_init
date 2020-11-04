from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, root_path="C:\\Users\\adladmin\\Desktop\\pYTHON_pROG\\Newfolder\\PythonNetwork\\Newfolder\\curriculum\\Folder_1\\Workplace\\Workplace_init\\pre-course\\my_root_Dir")

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def login():
    return render_template("login.html")

@app.route("/register", methods=['GET','POST'])
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)