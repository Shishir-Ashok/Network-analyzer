from flask import render_template, request, redirect, url_for, flash
from networkanalyzer.forms import LoginForm,RegistrationForm
from networkanalyzer import engine,app
from networkanalyzer import bcrypt
from flask_login import login_user, LoginManager, logout_user, current_user
from wtforms.validators import DataRequired, Length, Email, EqualTo


loginKey = 0
@app.route('/sign-up', methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		userDetails = request.form
		username = userDetails['username']
		email = userDetails['email']
		password = userDetails['password']
		hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
		conn = engine.connect()
		test = conn.execute("INSERT INTO USER_DETAILS(USERNAME,EMAIL,PASSWORD) VALUES(%s,%s,%s)",(username,email,hashed_password))
		conn.close()
		flash(f'Account created successfully! You can now Log In.', 'success')
		return redirect(url_for('login'))
	return render_template('register.html',title='Register',form=form)


@app.route('/')
def home():
	return render_template('layout.html')


@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		userDetails = request.form
		email = userDetails['email']
		password = userDetails['password']
		conn = engine.connect()
		test = conn.execute("SELECT EMAIL,PASSWORD FROM USER_DETAILS WHERE EMAIL=%s",(email)).fetchall()
		conn.close()
		if (len(test) != 0):
			if bcrypt.check_password_hash(test[0][1],password):
				flash('You have been logged in!', 'success')
				return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful! Email ID or Password or both is incorrect.', 'danger')
			return redirect('/login')
	return render_template('login.html',title='Login',form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))
