################################ IMPORTS ################################
# TO PUT ALL THESE INTO TXT THEN RUN THIS IN TERMINAL: pip freeze > requirements.txt
# ________________________________________________________________________________________________________________________________________________________________
# FLASK IMPORTS
from flask import Flask, render_template, session, redirect, url_for, g, request
from flask_session import Session

# ________________________________________________________________________________________________________________________________________________________________
# FORMS IMPORTS
from forms import userProfileForm, contactForm, settingsForm, loginForm, messyrLoginForm, quizForm, pollsForm, wallForm

# ________________________________________________________________________________________________________________________________________________________________
# DATABASE IMPORTS
from database import get_db, close_db
from sqlite3 import IntegrityError

# ________________________________________________________________________________________________________________________________________________________________
# PASSWORD SECURITY IMPORTS
from werkzeug.security import generate_password_hash, check_password_hash

# ________________________________________________________________________________________________________________________________________________________________
#  _____ IMPORTS
from functools import wraps

# ________________________________________________________________________________________________________________________________________________________________
# CONTACT FORM IMPORTS
import smtplib, ssl

# ________________________________________________________________________________________________________________________________________________________________
# ASSORTED UTILITY IMPORTS 
from random import randint, choice
import math
import datetime

# ________________________________________________________________________________________________________________________________________________________________
# FLASK APP INITIALISATION
app = Flask(__name__)

# ________________________________________________________________________________________________________________________________________________________________
# DATABASE TEARDOWN
app.teardown_appcontext(close_db)

# ________________________________________________________________________________________________________________________________________________________________
# COOKIES & SESSION IMPORTS
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False # True would be persistent
app.config["SESSION_TYPE"] = "filesystem"

Session(app)






@app.before_request
def load_logged_in_user():
    g.user = session.get("user_id", None)
    g.state = session.get("state", None) # Also creating a global "state" variable that signifies whether the user is a fan, artist or None

# I have two "login_required" decorators, one for if login is required for a fan and another for if login is required by an artist
def fan_login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("fan_login", next = request.url))
        return view(**kwargs)
    return wrapped_view

def artist_login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("artist_login"))
        return view(**kwargs)
    return wrapped_view









################################ SITEMAP ################################
# ________________________________________________________________________________________________________________________________________________________________
# undecided.html should probably get changed to "Downloads" and also link to the same page through the "use this skin" link

# Site Navigation                                 Profile Navigation
# |_Home (index.html)                             |_Friends (friends.html)
# |_Profile (profile.html)                        |_Flashbox (flashbox.html)
# |_Friends (friends.html)                        |_Photos (photos.html)
# |_Mail (contact.html)                           |_Widget (widget.html)
# |_Explore (explore.html)                        |_Whiteboard (whiteboard.html)
#   |__About (about.html)                         |_Solitayre (solitayre.html)
#   |__Undecided (undecided.html)                 |_Blog (blog.html)
#   |__Discography (discography.html)             |_Quiz (quiz.html) 
# |___Settings (settings.html)                    |_Polls (polls.html)
# |___help (help.html)                            |_Events (events.html)
# |___Login / Logout (login.html / logout.html)   |_Maryo (maryo.html)
# |___Search (search.html)                        |_Wall (wall.html)


################################ UNIVERSAL VARIABLES ################################
# ________________________________________________________________________________________________________________________________________________________________

# Year to apply in footer for copyright
@app.before_request
def fill_g():
    date = datetime.datetime.now()
    g.year = date.strftime("%Y")

site_nav = [
    "Home", "Profile", "Friends", "Mail", "Explore", "Settings", "Help", "Login / Logout", "Search"
]

profile_nav = [
    "Friends", "Flashbox", "Photos", "Widget", "White Board", "Solitayre", "Blog", "Quiz", "Polls", "Events", "Maryo", "Wall"
]



################################ SITE NAVIGATION ################################
# ________________________________________________________________________________________________________________________________________________________________
# HOME

@app.route("/", methods = ["GET", "POST"])
def index():
    """
    A home screen route.
    No requirement for any programming rn, as it is only calling the HTML page for the index and that is currently hard marked up.
    Eventually I would like to have this call the information to fill out the profile so that adding a new route would add a chunk without needing to edit the HTML.
    """
    try:
        return render_template("index.html", title = "Home")
    except:
        return render_template("index.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# PROFILE

@app.route("/profile", methods = ["GET", "POST"])
def profile():
    """
    Allows the user to change their username, handle, profile picture, and opt out of emails (Which we probably won't send anyway)
    """

    form = userProfileForm()

    try:
        return render_template("profile.html", title = "Profile", form = form)
    except:
        return render_template("profile.html", title = "ERROR", form = form)





# ________________________________________________________________________________________________________________________________________________________________
# FRIENDS

@app.route("/friends", methods = ["GET", "POST"])
def friends():
    """
    A place for us to show a list of our mates with profile pics and links to their music or socials.
    This won't be tethered by the top 16, but will be a list of all of our friends so can show however many we want. Maybe 4 columns still would make sense.
    Eventually I would love to expand this into Flask generated profiles with members etc that could act as a sort of wiki of Irish music,
    but that's waaaaaaaaaaaay outside of the scope of the site right now.
    """

    try:

        db = get_db()
        friendList = db.execute("""SELECT * FROM friends;""").fetchall() # Call every release in our inventory into a list of options

        # Would like to randomise friendList every page load

        return render_template("friends.html", title = "Friends", friendList = friendList)
    except:
        return render_template("friends.html", title = "ERROR", friendList = friendList)





# ________________________________________________________________________________________________________________________________________________________________
# MAIL

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    """
    
    """

    form = contactForm()

    try:
        return render_template("contact.html", title = "Home", form = form)
    except:
        return render_template("contact.html", title = "ERROR", form = form)





# ________________________________________________________________________________________________________________________________________________________________
# EXPLORE

@app.route("/explore", methods = ["GET", "POST"])
def explore():
    """
    I would like this to effectively work as a sitemap, with links to all the different pages compiled into 3 columns of cards.
    Eventually I would like to pass a list of all of the pages not in the site navigation to the explore tab on the home page and have it auto fill and expand as necessary.
    """
    try:
        return render_template("explore.html", title = "Explore")
    except:
        return render_template("explore.html", title = "ERROR")

# ____________________
# About 
@app.route("/explore/about", methods = ["GET", "POST"])
def about():
    """
    Pseudo-serious version of the profile about page. let this be for the journalists and the promoters etc.
    """
    try:
        return render_template("explore/about.html", title = "About")
    except:
        return render_template("explore/about.html", title = "ERROR")

# ____________________
# ????? 
@app.route("/explore/undecided", methods = ["GET", "POST"])
def undecided():
    try:
        return render_template("explore/undecided.html", title = "Undecided")
    except:
        return render_template("explore/undecided.html", title = "ERROR")

# ____________________
# Discography 
@app.route("/explore/discography", methods = ["GET", "POST"])
def discography():
    try:
        return render_template("explore/discography.html", title = "Discography")
    except:
        return render_template("explore/discography.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# SETTINGS

@app.route("/settings", methods = ["GET", "POST"])
def settings():
    """
    I don't have a whole pile to put in here, maybe pass in a dark mode toggle?
    """

    form = settingsForm()

    try:
        return render_template("settings.html", title = "Settings", form = form)
    except:
        return render_template("settings.html", title = "ERROR", form = form)





# ________________________________________________________________________________________________________________________________________________________________
# HELP

@app.route("/help", methods = ["GET", "POST"])
def help():
    """
    I don't have a whole pile to put in here, might be funny to have some self help articles?
    """
    try:
        return render_template("help.html", title = "Help")
    except:
        return render_template("help.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# LOGIN / LOGOUT
# Login route for Danny & JJ. After login it should show a drop down of the different things to upload. If they change the dropdown, it provides fields for the needed details. Submit and it will get  added to the DB and added to the site

@app.route("/login", methods = ["GET", "POST"])
def login():
    """
    One page but want to pass in two forms here.
    - One for "fan" login. I think this might be a GDPR breach, but I'd like people to be able to choose profile pictures and display names etc. for commenting on the wall.
    - One for myself, JJ and Danny to login. There won't be a way to "create" an account for this. I will manually add logins to the DB for these.
    """

    form = loginForm()

    try:
        return render_template("login.html", title = "Home", form = form)
    except:
        return render_template("login.html", title = "ERROR", form = form)
    
@app.route("/messyr_login", methods = ["GET", "POST"])
def messyr_login():
    """
    A function for logging into an artist account only.
    Going to have this have it's own page just for the lads convenience.
    """

    form = messyrLoginForm()

    if form.validate_on_submit():

        user_id = form.user_id.data
        password = form.password.data

        db = get_db()

        matching_users = db.execute(
            """
            SELECT * FROM artists
            WHERE user_id = ?;
            """,
            (user_id,)
        ).fetchone()

        if matching_users is None: # user id isn't in matching users, return that as an error
            form.user_id.errors.append("This user ID is not registered with us")

        elif not check_password_hash(matching_users["password"], password):
            form.password.errors.append("Password invalid")

        else: # Password & user id must match, so log them in.

            session["user_id"] = user_id
            session["state"] = "artist"
            return redirect( url_for( "home" ) )

    return render_template("messyr_login.html", form = form, title = "Artist Login | the depth")

@app.route("/logout")
def logout():
    """
    Quick route that clears the users session and logs them out of whatever profile they are logged into.
    """
    session.clear()
    return redirect (url_for( "home" ))





# ________________________________________________________________________________________________________________________________________________________________
# SEARCH

@app.route("/search", methods = ["GET", "POST"])
def search():
    """
    Page to display search results. I'm assuming there's a plugin for this but might be fun to try for yourself?
    Limit what's searchable to the wall, the blog, the about page, the discography, the events page, and the profile blurb.
    """
    try:
        return render_template("search.html", title = "Search")
    except:
        return render_template("search.html", title = "ERROR")





################################ PROFILE NAVIGATION ################################
# ________________________________________________________________________________________________________________________________________________________________
# FRIENDS - Don't need two friends routes

# @app.route("/friends", methods = ["GET", "POST"])
# def friends():
#     try:
#         return render_template("index.html", title = "Home")
#     except:
#         return render_template("index.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# FLASHBOX

@app.route("/flashbox", methods = ["GET", "POST"])
def flashbox():
    try:
        return render_template("flashbox.html", title = "Flashbox")
    except:
        return render_template("flashbox.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# PHOTOS

@app.route("/photos", methods = ["GET", "POST"])
def photos():
    try:
        return render_template("photos.html", title = "Photos")
    except:
        return render_template("photos.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# WIDGET

@app.route("/widget", methods = ["GET", "POST"])
def widget():
    try:
        return render_template("widget.html", title = "Widget")
    except:
        return render_template("widget.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# WHITEBOARD

@app.route("/whiteboard", methods = ["GET", "POST"])
def whiteboard():
    try:
        return render_template("whiteboard.html", title = "Whiteboard")
    except:
        return render_template("whiteboard.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# SOLITAYRE

@app.route("/solitayre", methods = ["GET", "POST"])
def solitayre():
    try:
        return render_template("solitayre.html", title = "Solitayre")
    except:
        return render_template("solitayre.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# BLOG

@app.route("/blog", methods = ["GET", "POST"])
def blog():
    try:
        return render_template("index.html", title = "Home")
    except:
        return render_template("index.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# QUIZ

@app.route("/quiz", methods = ["GET", "POST"])
def quiz():
    """
    
    """

    form = quizForm()

    try:
        return render_template("index.html", title = "Home", form = form)
    except:
        return render_template("index.html", title = "ERROR", form = form)





# ________________________________________________________________________________________________________________________________________________________________
# POLLS

@app.route("/polls", methods = ["GET", "POST"])
def polls():
    """
    
    """

    form = pollsForm()

    try:
        return render_template("index.html", title = "Home", form = form)
    except:
        return render_template("index.html", title = "ERROR", form = form)





# ________________________________________________________________________________________________________________________________________________________________
# EVENTS

@app.route("/events", methods = ["GET", "POST"])
def events():
    try:
        return render_template("index.html", title = "Home")
    except:
        return render_template("index.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# MARYO

@app.route("/maryo", methods = ["GET", "POST"])
def maryo():
    try:
        return render_template("index.html", title = "Home")
    except:
        return render_template("index.html", title = "ERROR")





# ________________________________________________________________________________________________________________________________________________________________
# WALL

@app.route("/wall", methods = ["GET", "POST"])
def wall():
    """
    
    """

    form = wallForm()

    try:
        return render_template("index.html", title = "Home", form = form)
    except:
        return render_template("index.html", title = "ERROR", form = form)










################################ helper functions called by other route functions ################################
# ________________________________________________________________________________________________________________________________________________________________
# ERROR











    







































    





################################ ERRORS ################################
# ________________________________________________________________________________________________________________________________________________________________

@app.errorhandler(400)
def page_not_found(error):
    """
    Bad Request

    The server cannot or will not process the request due to something that is perceived to be a client error
    """
    return render_template("errors/400.html", error_message = 400, title = "400")



# ________________________________________________________________________________________________________________________________________________________________

@app.errorhandler(401)
def page_not_found(error):
    """
    Unauthorized

    The client request has not been completed because it lacks valid authentication credentials for the requested resource
    
    """
    return render_template("errors/401.html", error_message = 401, title = "401")



# ________________________________________________________________________________________________________________________________________________________________

@app.errorhandler(403)
def page_not_found(error):
    """
    Forbidden

    The server understands the request but refuses to authorize it
    """
    return render_template("errors/403.html", error_message = 403, title = "403")



# ________________________________________________________________________________________________________________________________________________________________

@app.errorhandler(404)
def page_not_found(error):
    """
    Not Found

    The server cannot find the requested resource
    
    """
    return render_template("errors/404.html", error_message = 404, title = "404")


 
# ________________________________________________________________________________________________________________________________________________________________

@app.errorhandler(408)
def page_not_found(error):
    """
    Request Timeout

    The server would like to shut down this unused connection
    """
    return render_template("errors/408.html", error_message = 408, title = "408")



# ________________________________________________________________________________________________________________________________________________________________

@app.errorhandler(418)
def page_not_found(error):
    """
    I'm a teapot

    The server refuses to brew coffee because it is, permanently, a teapot
    """
    return render_template("errors/418.html", error_message = 418, title = "418")



# ________________________________________________________________________________________________________________________________________________________________

@app.errorhandler(500)
def page_not_found(error):
    """
    Internal Server Error

    The server encountered an unexpected condition that prevented it from fulfilling the request

    I think that renders a request for a webpage unavailable, but it might work if things are cached.
    """
    return render_template("errors/500.html", error_message = 500, title = "500")



# ________________________________________________________________________________________________________________________________________________________________

@app.errorhandler(502)
def page_not_found(error):
    """
    Bad Gateway
    
    The server, while acting as a gateway or proxy, received an invalid response from the upstream server

    I think that renders a request for a webpage unavailable, but it might work if things are cached.
    """
    return render_template("errors/502.html", error_message = 502, title = "502")


# ________________________________________________________________________________________________________________________________________________________________

@app.errorhandler(503)
def page_not_found(error):
    """
    Service Unavailable

    The server is not ready to handle the request

    I think that renders a request for a webpage unavailable, but it might work if things are cached.
    """
    return render_template("errors/503.html", error_message = 503, title = "503")



# ________________________________________________________________________________________________________________________________________________________________

@app.errorhandler(504)
def page_not_found(error):
    """
    Gateway Timeout
    
    The server, while acting as a gateway or proxy, did not get a response in time from the upstream server that it needed in order to complete the request

    I think that renders a request for a webpage unavailable, but it might work if things are cached.
    """
    return render_template("errors/504.html", error_message = 504, title = "504")