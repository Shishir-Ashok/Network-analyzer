from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MySQL@123a@localhost/flask'
app.config['SECRET_KEY'] = 'a598a7af31fd2b71f6b60c8e102bf467'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class USER_DETAILS(db.Model):
    UID = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String(20), unique=True, nullable=False)
    EMAIL = db.Column(db.String(120), unique=True, nullable=False)
    IMAGE_FILE = db.Column(db.String(20), nullable=False, default='default.jpg')
    PASSWORD = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.USERNAME}', '{self.EMAIL}', '{self.IMAGE_FILE}')"

class VENDORS(db.Model):
	VID = db.Column(db.Integer, primary_key=True)
	NAME = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"Vendor('{self.NAME}')"

class DEVICE_ADDRESS(db.Model):
	DID = db.Column(db.Integer, primary_key=True)
	IP = db.Column(db.String(30), nullable=False)
	MAC = db.Column(db.String(30), nullable=False)
	VID = db.Column(db.Integer, db.ForeignKey(VENDORS.VID, ondelete="CASCADE", onupdate="CASCADE"))


class RECORDS(db.Model):
	RID = db.Column(db.Integer, primary_key=True)
	TIMESTAMP = db.Column(db.String(30), nullable=False)
	UID = db.Column(db.Integer, db.ForeignKey(USER_DETAILS.UID, ondelete="CASCADE", onupdate="CASCADE"))

class U_D(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	UID = db.Column(db.Integer, db.ForeignKey(USER_DETAILS.UID, ondelete="CASCADE", onupdate="CASCADE"))
	DID = db.Column(db.Integer, db.ForeignKey(DEVICE_ADDRESS.DID, ondelete="CASCADE", onupdate="CASCADE"))

class R_V(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	RID = db.Column(db.Integer, db.ForeignKey(RECORDS.RID, ondelete="CASCADE", onupdate="CASCADE"))
	VID = db.Column(db.Integer, db.ForeignKey(VENDORS.VID, ondelete="CASCADE", onupdate="CASCADE"))

if __name__ == '__main__':
	db.create_all()

# import os

# os.system('ls')