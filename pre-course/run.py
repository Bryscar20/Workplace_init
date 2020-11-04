from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__, root_path="C:\\Users\\adladmin\\Desktop\\pYTHON_pROG\\Newfolder\\PythonNetwork\\Newfolder\\curriculum\\Folder_1\\Workplace\\Workplace_init\\pre-course\\my_root_Dir")
app.secret_key = 'somesecretkeythatonlyishouldknow'

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='test1@123.com', password='test123'))
users.append(User(id=2, username='test2', password='test234'))
users.append(User(id=3, username='test3', password='test345'))

# Homepage
@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")
# Profile page
@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
    
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return render_template("profile.html")
    return render_template("index.html")

@app.route("/profile", methods=['GET','POST'])
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)