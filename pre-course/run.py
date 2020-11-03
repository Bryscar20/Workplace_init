from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, root_path="C:\\Users\\adladmin\\Desktop\\pYTHON_pROG\\Newfolder\\PythonNetwork\\Newfolder\\curriculum\\Folder_1\\Workplace\\Workplace_init\\pre-course\\my_root_Dir")
# app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    """
    docstring
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)