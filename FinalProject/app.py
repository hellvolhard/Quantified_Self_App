from flask import Flask, redirect
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finaldatabase.sqlite3"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class User(db.Model):
    __tablename__ = 'User_Credentials'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String,  nullable=False)
    fname = db.Column(db.String,  nullable=False)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login_form.html")

    if request.method=="POST":
        users = User.query.all()

        username = request.form["u"]
        password = request.form["p"]

        for user in users:
            if username == user.username and password == user.password:
                print("Logged in successfully")
                break
        return redirect("/")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method=="GET":
        return render_template("signup_form.html")


if __name__ == '__main__':
  # Run the Flask app
  app.run(debug=True)
