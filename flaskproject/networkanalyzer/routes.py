from flask import render_template, request, redirect, url_for, flash, request
from networkanalyzer.forms import LoginForm,RegistrationForm
from networkanalyzer import db,app,bcrypt
from networkanalyzer.model import USER_DETAILS, CIDR_, DEVICE_ADDRESS
from flask_login import login_user, LoginManager, logout_user, current_user, login_required
from wtforms.validators import DataRequired, Length, Email, EqualTo
from networkanalyzer.getIPinfo import getIP
from networkanalyzer.parse import macIP
# import networkanalyzer.getIPinfo
import os



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
	return render_template('home.html')


@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	print("Login form = ", form)
	if form.validate_on_submit():
		user = USER_DETAILS.query.filter_by(EMAIL=form.email.data).first()
		if user and bcrypt.check_password_hash(user.PASSWORD, form.password.data):
			login_user(user, remember=form.remember.data)
			flash('You have been logged in!', 'success')
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful! Email ID and / or Password is incorrect.', 'danger')
			return redirect('/login')
	return render_template('login.html',title='Login',form=form)


@app.route('/account')
@login_required
def account():
	image_file = url_for('static', filename='profile_pictures/' + current_user.IMAGE_FILE)
	return render_template('account.html',title='Account', image_file=image_file)
	# return '<h1>{{ current_user.username }}</h1>'

@app.route('/scan')
@login_required
def scan():
	os.system('cd networkanalyzer/;sh script.sh')
	i=1;
	IP, MAC = macIP(fileName="networkanalyzer/output.txt",getip_filename="networkanalyzer/IPinfo.txt")
	# info = DEVICE_ADDRESS(IP=mac_IP.IPaddress.data, MAC=macIP.macSplit.data, VID=i)
	# db.session.add(info)
	# db.session.commit()
	# mask = CIDR_.query.filter_by(HEX=get_IP.subnetMask.data).first()
	x = len(IP)
	for i in range (x):
		print("MAC : ",MAC[i],"IP : ", IP[i])
		info = DEVICE_ADDRESS(IP=IP[i], MAC=MAC[i], VID=i+1)
		db.session.add(info)
	db.session.commit()
	# for i in mac_IP:
	# 	a =1
	# 	print(i[a])
	# print(mask)
	return render_template('table.html', title='Scan Result',IP=IP,MAC=MAC,x=x)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))
