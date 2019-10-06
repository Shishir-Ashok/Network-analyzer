from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import yaml
from forms import LoginForm,RegistrationForm


app = Flask(__name__)

mysql = MySQL(app)


db = yaml.load(open('db.yaml'))

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['SECRET_KEY'] = 'a598a7af31fd2b71f6b60c8e102bf467'



@app.route('/sign-up', methods=['GET','POST'])
def register():
	# if request.method == 'POST':
	form = RegistrationForm()

	if form.validate_on_submit():
		userDetails = request.form
		username = userDetails['username']
		email = userDetails['email']
		password = userDetails['password']
		cur = mysql.connection.cursor()
		test = cur.execute("INSERT INTO USER_DETAILS(USERNAME,EMAIL,PASSWORD) VALUES(%s,%s,%s)",(username,email,password))
		mysql.connection.commit()
		cur.close()
		flash(f'Account created for {form.username.data}!', 'success')
		return render_template('layout.html')
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
	# if request.method == 'POST':
	form = LoginForm()

	if form.validate_on_submit():
		userDetails = request.form
		email = userDetails['email']
		password = userDetails['password']
		email = userDetails['email']
		password = userDetails['password']
		cur = mysql.connection.cursor()
		test = cur.execute("SELECT EMAIL,PASSWORD FROM USER_DETAILS WHERE EMAIL=%s AND PASSWORD=%s",(email,password))
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
	resultValue = cur.execute("SELECT * FROM USER")

	if resultValue > 0:
		print("resultValue = {}".format(resultValue))
		userDetails = cur.fetchall()
		print(userDetails)
		return render_template('details.html',userDetails=userDetails)
	else:
		return '<h1>Empty</h1>'


if __name__ == '__main__':
	app.run(debug=True)