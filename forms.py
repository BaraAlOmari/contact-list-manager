from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import re

def validate_name(form, field):
    if field.data and not re.fullmatch(r"[A-Za-z\s'-]+", field.data):  
        raise ValidationError('Name must contain only letters, spaces, hyphens, and apostrophes!')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[validate_name])
    phone = StringField('Phone', validators=[DataRequired(message='Phone number is required!')])
    email = StringField('Email', validators=[Email(message='Invalid email address!')])
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 