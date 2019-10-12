from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from networkanalyzer import app
from networkanalyzer.model import USER_DETAILS


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    def validate_username (self,USERNAME):
        user = USER_DETAILS.query.filter_by(USERNAME=USERNAME.data).first()
        if user:
            raise ValidationError('Username is already taken')

    def validate_email (self,EMAIL):
        user = USER_DETAILS.query.filter_by(EMAIL=EMAIL.data).first()
        if user:
            raise ValidationError('Email ID is already taken')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')