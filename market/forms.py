from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length, EqualTo, DataRequired, Email, ValidationError
from market.models import user

class RegisterForm(FlaskForm):
    
    def validate_username(self, username_to_check):
        User = user.query.filter_by(username=username_to_check.data).first()
        if User:
            raise ValidationError('Username already exists! Please try a different name')
    
    def validate_email_address(self, email_address_to_check):
        User = user.query.filter_by(username=email_address_to_check.data).first()
        if User:
            raise ValidationError('email address already exists! Please try a different email address')
        
    
    
    
    username = StringField(label='User Name : ', validators=[length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address : ', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password : ', validators=[length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account : ')
    
    
class LoginForm(FlaskForm):
    username = StringField(label='User Name : ', validators=[DataRequired()])
    password = PasswordField(label='Password : ', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')
    