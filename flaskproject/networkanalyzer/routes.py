from flask import render_template, request, redirect, url_for, flash
from networkanalyzer.forms import LoginForm,RegistrationForm
from networkanalyzer import db,app,bcrypt
from networkanalyzer.model import USER_DETAILS
from flask_login import login_user, LoginManager, logout_user, current_user
from wtforms.validators import DataRequired, Length, Email, EqualTo


loginKey = 0
@app.route('/sign-up', methods=['GET','POST'])
def register():
	print("Hello\n")
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	else:
		print("Is authenticated not working\n")
	form = RegistrationForm()
	if form.validate_on_submit():
		userDetails = request.form
		username = userDetails['username']
		email = userDetails['email']
		password = userDetails['password']
		hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
		user = USER_DETAILS(USERNAME=form.username.data, EMAIL=form.email.data, PASSWORD=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created successfully! You can now Log In.', 'success')
		return redirect(url_for('login'))
	return render_template('register.html',title='Register',form=form)


@app.route('/')
def home():
	return render_template('layout.html')


@app.route('/login', methods=['GET','POST'])
def login():
	print("Hello\n")
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	else:
		print("Is authenticated not working\n")
	form = LoginForm()
	loggedin = 0

	if form.validate_on_submit():
		user = USER_DETAILS.query.filter_by(EMAIL=form.email.data).first()
		if user and bcrypt.check_password_hash(user.PASSWORD, form.password.data):
			login_user(user, remember=form.remember.data)
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful! Email ID and / or Password is incorrect.', 'danger')
			return redirect('/login')
	return render_template('login.html',title='Login',form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))
