from flask import render_template, request, redirect, url_for, flash
from networkanalyzer.forms import LoginForm,RegistrationForm
from networkanalyzer import mysql,app
from networkanalyzer import bcrypt
from flask_login import login_user, current_user, LoginManager
from wtforms.validators import DataRequired, Length, Email, EqualTo


@app.route('/sign-up', methods=['GET','POST'])
def register():

	if current_user.is_authenticated:
		return redirect(url_for('home'))
	cur = mysql.connection.cursor()
	emaildetails = cur.execute("SELECT EMAIL FROM USER_DETAILS")
	usernamedetails = cur.execute("SELECT USERNAME FROM USER_DETAILS")
	if emaildetails > 0:
		print("resultValue = {}".format(emaildetails))
		email_all = cur.fetchall()
	if usernamedetails > 0:
		print("resultValue = {}".format(usernamedetails))
		username_all = cur.fetchall()
	form = RegistrationForm(FlaskForm,username_all,email_all)
	cur.close()
	if form.validate_on_submit():
		userDetails = request.form
		username = userDetails['username']
		email = userDetails['email']
		password = userDetails['password']
		hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
		cur = mysql.connection.cursor()
		test = cur.execute("INSERT INTO USER_DETAILS(USERNAME,EMAIL,PASSWORD) VALUES(%s,%s,%s)",(username,email,hashed_password))
		mysql.connection.commit()
		cur.close()
		flash(f'Account created successfully! You can now Log In.', 'success')
		return redirect(url_for('login'))
	return render_template('register.html',title='Register',form=form)
# @app.route('/', methods=['GET','POST'])
# def index():							
# 	if request.method == 'POST':
# 		userDetails = request.form
# 		fname = userDetails['fname']
# 		lname = userDetails['lname']
# 		fname = fname.strip()
# 		lname = lname.strip()
# 		print("fname :",fname,"|","Lname :",lname,"|")
# 		if fname != '' and lname != '':
# 			cur = mysql.connection.cursor()
# 			cur.execute("INSERT INTO USER(FNAME,LNAME) VALUES(%s,%s)",(fname,lname))
# 			mysql.connection.commit()
# 			cur.close()
# 		else:
# 			return '<h1>EMPTY</h1>'
# 		#return redirect('/users')
# 	return render_template('tindex.html')
@app.route('/')
def home():
	return render_template('layout.html')


@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()

	if form.validate_on_submit():
		userDetails = request.form
		email = userDetails['email']
		password = userDetails['password']
		email = userDetails['email']
		password = userDetails['password']
		hashPassword_check = bcrypt.generate_password_hash(password).decode('utf-8')
		cur = mysql.connection.cursor()
		test = cur.execute("SELECT EMAIL,PASSWORD FROM USER_DETAILS WHERE EMAIL=%s and PASSWORD=%s",(email,password))
		mysql.connection.commit()
		cur.close()
		if (test == 1):
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful! Email ID or Password or both is incorrect.', 'danger')
		return redirect('/login')
	return render_template('login.html',title='Login',form=form)

@app.route('/users')
def users():

	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM USER_DETAILS")

	if resultValue > 0:
		print("resultValue = {}".format(resultValue))
		userDetails = cur.fetchall()
		print(userDetails)
		return render_template('details.html',userDetails=userDetails)
	else:
		return '<h1>Empty</h1>'