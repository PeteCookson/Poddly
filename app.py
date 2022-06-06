import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_podcasts")
def get_podcasts():
    podcasts = mongo.db.podcasts.find()
    return render_template("podcasts.html", podcasts=podcasts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        # check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("get_podcasts"))


@app.route("/add_podcast", methods=["GET", "POST"])
def add_podcast():
    if request.method == "POST":
        podcast = {
            "category_name": request.form.get("category_name"),
            "podcast_name": request.form.get("podcast_name"),
            "podcast_description": request.form.get("podcast_description"),
            "channel": request.form.get("channel"),
            "streaming_service": request.form.get("streaming_service"),
            "added_by": session["user"],
           # "date_added":
            "cover": request.form.get("cover")
        }
        mongo.db.podcasts.insert_one(podcast)
       # mongo.db.addCurrentDate.insert_one()
        flash("Podcast successfully added to the PODDLY Directory")
        return redirect(url_for("get_podcasts"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    channels = mongo.db.channels.find().sort("channel", 1)
    services = mongo.db.service.find().sort("streaming_service")
    return render_template("add_podcast.html", categories=categories, 
    channels=channels, services=services)


@app.route("/edit_podcast/<podcast_id>", methods=["GET", "POST"])
def edit_podcast(podcast_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "podcast_name": request.form.get("podcast_name"),
            "podcast_description": request.form.get("podcast_description"),
            "channel": request.form.get("channel"),
            "streaming_service": request.form.get("streaming_service"),
            "added_by": session["user"],
            "cover": request.form.get("cover")
        }
        mongo.db.podcasts.update_one({"_id": ObjectId(podcast_id)}, {"$set": submit })
        flash("Podcast Successfully Updated")
        return redirect(url_for("get_podcasts"))

    podcast = mongo.db.podcasts.find_one({"_id": ObjectId(podcast_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    channels = mongo.db.channels.find().sort("channel", 1)
    services = mongo.db.service.find().sort("streaming_service")
    return render_template("edit_podcast.html", podcast=podcast, categories=categories, 
    channels=channels, services=services)


@app.route("/delete_podcast/<podcast_id>")
def delete_podcast(podcast_id):
    mongo.db.podcasts.delete_one({"_id": ObjectId(podcast_id)})
    flash("Podcast successfully deleted from the PODDLY Directory")
    return redirect(url_for("get_podcasts"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)         # Change to false on deployment
 