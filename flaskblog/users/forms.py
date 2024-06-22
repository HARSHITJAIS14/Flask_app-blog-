from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError,Email
from email_validator import validate_email, EmailNotValidError
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from flaskblog.models import User
from flask_login import current_user



class RegistrationForm(FlaskForm):
    username=StringField('Username',
                        validators=[DataRequired(),Length(min=2,max=20)]) 

    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist..')
    def validate_email(self, email):
        try:
            validate_email(email.data)
        except EmailNotValidError as e:
            raise ValidationError(str(e))
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already linked to another user")
class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username=StringField('Username',
                        validators=[DataRequired(),Length(min=2,max=20)]) 

    email=StringField('Email',validators=[DataRequired(),Email()])
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')
    def validate_username(self,username):
        if username.data!=current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exist..')
    def validate_email(self, email):
        try:
            validate_email(email.data)
        except EmailNotValidError as e:
            raise ValidationError(str(e))
        if email.data!=current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email already linked to another user")
class RequestResetForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    submit=SubmitField('Request Password Reset')
    def validate_email(self, email):
        try:
            validate_email(email.data)
        except EmailNotValidError as e:
            raise ValidationError(str(e))
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account with this email.You must register first.")
        
class ResetPassword(FlaskForm):
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Reset Password')