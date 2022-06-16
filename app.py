import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_paginate import Pagination, get_page_args
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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
    podcasts = list(mongo.db.podcasts.find())
    return render_template("podcasts.html", podcasts=podcasts)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    podcasts = list(mongo.db.podcasts.find({"$text": {"$search": query}}))
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
                flash("You have succesfully logged in as {}".format(
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
        return redirect(url_for("get_podcasts"))

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
            "added_on": datetime.now().strftime("%d %b, %Y"),
            "cover": request.form.get("cover")
        }
        mongo.db.podcasts.insert_one(podcast)
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


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("dashboard.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))
    return render_template("add_category.html")


@app.route("/add_channel", methods=["GET", "POST"])
def add_channel():
    if request.method == "POST":
        channel = {
            "channel": request.form.get("channel")
        }
        mongo.db.channels.insert_one(channel)
        flash("New Channel Added")
        return redirect(url_for("get_categories"))
    return render_template("dashboard.html")
    
@app.route("/add_service", methods=["GET", "POST"])
def add_service():
    if request.method == "POST":
        service = {
            "streaming_service": request.form.get("streaming_service")
        }
        mongo.db.service.insert_one(service)
        flash("New Streaming Service Added")
        return redirect(url_for("get_categories"))
    return render_template("dashboard.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one(
            {"_id": ObjectId(category_id)},{"$set": submit})
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


@app.route("/get_channels")
def get_channels(channel_id):
    channels = mongo.db.channels.find_one({"id": ObjectId(channel_id)})
    return render_template("get_categories", channels=channels)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)