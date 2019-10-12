from flask_login import LoginManager
from flask import Flask
from sqlalchemy import create_engine
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bcrypt = Bcrypt(app)


engine = create_engine("mysql+pymysql://root:MySQL@123a@localhost/test1?host=localhost?port=3306")
conn = engine.connect()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MySQL@123a@localhost/flask'
app.config['SECRET_KEY'] = 'a598a7af31fd2b71f6b60c8e102bf467'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'




from networkanalyzer import routes