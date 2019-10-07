from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import yaml



app = Flask(__name__)

mysql = MySQL(app)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

@app.route('/')
def res():
	cur = mysql.connection.cursor()
	details = cur.fetchall()
	print(details)


if __name__ == '__main__':
	app.run(debug=True)