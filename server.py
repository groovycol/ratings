"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

# from model import connect_to_db, db
from model import User, Rating, Movie, connect_to_db, db

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route('/sign_in')
def sign_in():
    """Send user to sign in page"""

    return render_template("sign_in.html")

@app.route('/user_validation', methods=["POST"])
def user_validation():
    """Validate user login, add new users to dbase"""
    email = request.form.get("email")
    password = request.form.get("password")

    User.query.filter_by(email="email").one()
    # Find out if they are in the DB with query...
    #  User.query.filter('email').
    # if user not in db
    #     add user to db       
    # else
    #     cool

    # return render_template("welcome.html")

    return render_template("homepage.html")



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
