from flask_mysqldb import MySQL
import yaml
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, LoginManager

app = Flask(__name__)
mysql = MySQL(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = yaml.load(open('networkanalyzer/db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['SECRET_KEY'] = 'a598a7af31fd2b71f6b60c8e102bf467'

from networkanalyzer import routes