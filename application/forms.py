from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import *

