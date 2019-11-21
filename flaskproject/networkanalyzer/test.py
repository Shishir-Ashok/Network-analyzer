from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MySQL@123a@localhost/flask'
app.config['SECRET_KEY'] = 'a598a7af31fd2b71f6b60c8e102bf467'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class USER_DETAILS(db.Model, UserMixin):
	UID = db.Column(db.Integer, primary_key=True)
	USERNAME = db.Column(db.String(30), unique=True, nullable=False)
	EMAIL = db.Column(db.String(30), unique=True, nullable=False)
	IMAGE_FILE = db.Column(db.String(20), nullable=False, default='default.png')
	PASSWORD = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.USERNAME}', '{self.EMAIL}')"

	def get_id(self):
		return (self.UID)

class VENDORS(db.Model, UserMixin):
	VID = db.Column(db.Integer, primary_key=True)
	MACSEARCH = db.Column(db.String(20), nullable=False)
	NAME = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"Vendor('{self.NAME}')"

class DEVICE_ADDRESS(db.Model, UserMixin):
	DID = db.Column(db.Integer, primary_key=True)
	IP = db.Column(db.String(30), nullable=False)
	MAC = db.Column(db.String(30), nullable=False)
	VID = db.Column(db.Integer, db.ForeignKey(VENDORS.VID, ondelete="CASCADE", onupdate="CASCADE"))

	def __repr__(self):
		return f"DEVICE_ADDRESS('{self.IP}', '{self.MAC}')"


class RECORDS(db.Model, UserMixin):
	RID = db.Column(db.Integer, primary_key=True)
	TIMESTAMP = db.Column(db.String(30), nullable=False)
	UID = db.Column(db.Integer, db.ForeignKey(USER_DETAILS.UID, ondelete="CASCADE", onupdate="CASCADE"))

	def __repr__(self):
		return f"RECORDS('{self.TIMESTAMP}')"

class U_D(db.Model, UserMixin):
	ID = db.Column(db.Integer, primary_key=True)
	UID = db.Column(db.Integer, db.ForeignKey(USER_DETAILS.UID, ondelete="CASCADE", onupdate="CASCADE"))
	DID = db.Column(db.Integer, db.ForeignKey(DEVICE_ADDRESS.DID, ondelete="CASCADE", onupdate="CASCADE"))

if __name__ == '__main__':
	db.create_all()

# import os

# os.system('ls')