from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators


class ContactForm(FlaskForm):
    name = StringField('Name:', [validators.Required("Please enter your name.")])
    email = StringField('E-mail:', [validators.Required("Please enter a valid email address."), validators.Email("Please enter your email address.")])
    subject = StringField('Subject:', [validators.Required("Please enter a subject.")])
    message = TextAreaField('Comment:', [validators.Required("Please enter a message.")])
    submit = SubmitField('Submit')