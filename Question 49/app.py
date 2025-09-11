from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this in production
bcrypt = Bcrypt(app)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["flask_auth_db"]
users = db["users"]

# ---------- Routes ----------

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("home"))
    return redirect(url_for("signin"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        existing_user = users.find_one({"username": username})
        if existing_user:
            flash("Username already exists!", "danger")
            return redirect(url_for("signup"))

        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
        users.insert_one({"username": username, "password": hashed_pw})
        flash("Signup successful! Please login.", "success")
        return redirect(url_for("signin"))

    return render_template("signup.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users.find_one({"username": username})
        if user and bcrypt.check_password_hash(user["password"], password):
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials!", "danger")

    return render_template("signin.html")

@app.route("/home")
def home():
    if "username" in session:
        return render_template("home.html", username=session["username"])
    return redirect(url_for("signin"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out successfully!", "info")
    return redirect(url_for("signin"))

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
