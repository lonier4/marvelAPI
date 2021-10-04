from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SubmitField, PasswordField
from wtforms import validators
from wtforms.validators import DataRequired, Email, EqualTo

class newMarvelForm(FlaskForm):
    character_name = StringField('Character Name', validators=[DataRequired()])
    super_power = StringField('Superpower')
    comics_appeared_in = StringField('Comics')
    hero_or_villain = StringField('Superhero or Villain') 
    description = StringField('Description')
    submit_button = SubmitField()

class signInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

class signUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired() ] )
    email = StringField('Email', validators=[DataRequired(), Email() ] )
    password = PasswordField('Password', validators=[DataRequired() ] )
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password') ] )
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit_button = SubmitField()

class updateUser(FlaskForm):
    newusername = StringField('New Username')
    newpassword = StringField('New Password')
    confirm_newpassword = StringField('Confirm New Password', validators=[EqualTo('newpassword')])
    oldpassword = StringField('Current Password', validators=[DataRequired()])
    submit_button = SubmitField()