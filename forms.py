from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, EqualTo



#______________________________________________________________________________________________________________________________
class userProfileForm(FlaskForm):
    """
    Allows a user to change various details about how they comment on the page
    """
    displayName = StringField(
        "Display Name:",
        validators = [
            InputRequired()
        ]
    )
    username = StringField(
        "Username:",
        validators = [
            InputRequired()
        ]
    )
    email = StringField(
        "Email address:",
        validators = [
            InputRequired()
        ]
    )
    pfp = TextAreaField(
        "Profile picture:",
        validators = [
            InputRequired()
        ]
    )
    submit = SubmitField(
        "Update profile"
    )






#______________________________________________________________________________________________________________________________
class contactForm(FlaskForm):
    """
    Flask Form for the email contact form.
    App.py handles the message being sent via SMTP.
    """
    name = StringField(
        "Name:",
        validators = [
            InputRequired()
        ]
    )
    subject = StringField(
        "Subject:",
        validators = [
            InputRequired()
        ]
    )
    email = StringField(
        "Email address:",
        validators = [
            InputRequired()
        ]
    )
    message = TextAreaField(
        "Message:",
        validators = [
            InputRequired()
        ],
        default = "Put your message here"
    )

    submit = SubmitField()


#______________________________________________________________________________________________________________________________
class settingsForm(FlaskForm):
    """
    Flask Form for the email contact form.
    App.py handles the message being sent via SMTP.
    """
    name = StringField(
        "Name:",
        validators = [
            InputRequired()
        ]
    )
    subject = StringField(
        "Subject:",
        validators = [
            InputRequired()
        ]
    )
    email = StringField(
        "Email address:",
        validators = [
            InputRequired()
        ]
    )
    message = TextAreaField(
        "Message:",
        validators = [
            InputRequired()
        ],
        default = "Put your message here"
    )

    submit = SubmitField()


#______________________________________________________________________________________________________________________________
class loginForm(FlaskForm):
    """
    Flask Form for the email contact form.
    App.py handles the message being sent via SMTP.
    """
    userID = StringField(
        "user ID:",
        validators = [
            InputRequired()
        ]
    )
    password = PasswordField(
        "Password:",
        validators = [
            InputRequired()
        ]
    )
    submit = SubmitField(
        "Login"
    )

class registrationForm(FlaskForm):

    userID = StringField(
        "User id:",
        validators = [
            InputRequired()
        ]
    )
    password = PasswordField(
        "Password:",
        validators = [
            InputRequired()
        ]
    )
    password2 = PasswordField(
        "Confirm Password:",
        validators = [
            InputRequired(),
            EqualTo("password")
        ]
    )
    submit = SubmitField(
        "Create account"
    )


#______________________________________________________________________________________________________________________________

class messyrLoginForm(FlaskForm):
    """
    Login form for access to content submission.
    Mainly for Danny, JJ, and Donagh.
    There isn't an equivalent registration system.
    Accounts manually added to database.
    """
    messyrName = StringField(
        "Messyr Name:",
        validators = [
            InputRequired()
        ]
    )
    password = PasswordField(
        "Password:",
        validators = [
            InputRequired()
        ]
    )
    submit = SubmitField(
        "Messyr Login"
    )

class addEvent(FlaskForm):
    submit = SubmitField(
        "Add Event"
    )


#______________________________________________________________________________________________________________________________
class quizForm(FlaskForm):
    """
    Flask Form for the email contact form.
    App.py handles the message being sent via SMTP.
    """
    name = StringField(
        "Name:",
        validators = [
            InputRequired()
        ]
    )
    subject = StringField(
        "Subject:",
        validators = [
            InputRequired()
        ]
    )
    email = StringField(
        "Email address:",
        validators = [
            InputRequired()
        ]
    )
    message = TextAreaField(
        "Message:",
        validators = [
            InputRequired()
        ],
        default = "Put your message here"
    )

    submit = SubmitField()


#______________________________________________________________________________________________________________________________
class pollsForm(FlaskForm):
    """
    Flask Form for the email contact form.
    App.py handles the message being sent via SMTP.
    """
    name = StringField(
        "Name:",
        validators = [
            InputRequired()
        ]
    )
    subject = StringField(
        "Subject:",
        validators = [
            InputRequired()
        ]
    )
    email = StringField(
        "Email address:",
        validators = [
            InputRequired()
        ]
    )
    message = TextAreaField(
        "Message:",
        validators = [
            InputRequired()
        ],
        default = "Put your message here"
    )

    submit = SubmitField()



#______________________________________________________________________________________________________________________________

class wallForm(FlaskForm):
    """
    Flask Form for the email contact form.

    Display name, user name, and time of post is also taken but is hidden and does not need a form field.
    """
    message = TextAreaField(
        "Write On their wall:",
        validators = [
            InputRequired()
        ]
    )
    submit = SubmitField(
        "Post To Wall"
    )



#______________________________________________________________________________________________________________________________
class ContactForm(FlaskForm):
    """
    Flask Form for the email contact form.
    App.py handles the message being sent via SMTP.
    """
    name = StringField(
        "Name:",
        validators = [
            InputRequired()
        ]
    )
    subject = StringField(
        "Subject:",
        validators = [
            InputRequired()
        ]
    )
    email = StringField(
        "Email address:",
        validators = [
            InputRequired()
        ]
    )
    message = TextAreaField(
        "Message:",
        validators = [
            InputRequired()
        ],
        default = "Put your message here"
    )

    submit = SubmitField()