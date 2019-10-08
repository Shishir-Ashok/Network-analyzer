from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from networkanalyzer import app,engine
from sqlalchemy import create_engine


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    # print(username_all)
    # print(email_all)
    def validate_username (self,username):
        # engine = create_engine("mysql+pymysql://root:MySQL@123a@localhost/test1?host=localhost?port=3306")
        conn = engine.connect()
        username_validate = conn.execute("SELECT USERNAME FROM USER_DETAILS WHERE USERNAME LIKE BINARY %s",(username.data)).fetchall()
        conn.close()
        print("Username : ", username_validate)
        if len(username_validate) != 0:
            raise ValidationError('Username is already taken')

    def validate_email (self,email):
        # engine = create_engine("mysql+pymysql://root:MySQL@123a@localhost/test1?host=localhost?port=3306")
        conn = engine.connect()
        email_validate = conn.execute("SELECT EMAIL FROM USER_DETAILS WHERE USERNAME LIKE BINARY %s",(email.data)).fetchall()
        conn.close()
        print("Email : ", email_validate)
        if len(email_validate) != 0:
            raise ValidationError('     Email ID is already taken')
    

    # cur = mysql.connection.cursor()
    # details = cur.fetchall()
    # print(details)
    # def validate_email (self,email):
    
    #     cur = mysql.connection.cursor()
    #     check = cur.execute("SELECT EMAIL FROM USER_DETAILS WHERE EMAIL LIKE BINARY '%s",(email))
    #     cur.close()
    #     if check:
    #         raise ValidationError('Email ID is already taken')
    # check = cur.execute("SELECT EMAIL FROM USER_DETAILS WHERE EMAIL LIKE BINARY '%s",(email))
    # print(check)
    # cur.close()



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')