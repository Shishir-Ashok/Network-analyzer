from flask_login import LoginManager
from flask import Flask
from sqlalchemy import create_engine
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

engine = create_engine("mysql+pymysql://root:MySQL@123a@localhost/test1?host=localhost?port=3306")
conn = engine.connect()

# db = yaml.load(open('networkanalyzer/db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']
app.config['SECRET_KEY'] = 'a598a7af31fd2b71f6b60c8e102bf467'

from networkanalyzer import routes