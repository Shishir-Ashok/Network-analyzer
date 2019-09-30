from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)

mysql = MySQL(app)


db = yaml.load(open('db.yaml'))
print(db)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

print(app)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		userDetails = request.form
		fname = userDetails['fname']
		lname = userDetails['lname']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO USER(FNAME,LNAME) VALUES(%s,%s)",(fname,lname))
		mysql.connection.commit()
		cur.close()
		# return redirect('/users')
	return render_template('index.html')

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