from flask_login import LoginManager, UserMixin
from flask import Flask
from networkanalyzer import db,app,login_manager
from flask_sqlalchemy import SQLAlchemy



@login_manager.user_loader
def load_user(user_UID):
	return USER_DETAILS.query.get(int(user_UID))


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
		return f"Vendor('{self.NAME}','{self.VID}')"

	def get_id(self):
		return (self.VID)

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
	INFO = db.Column(db.String(60), nullable=False)
	UID = db.Column(db.Integer, db.ForeignKey(USER_DETAILS.UID, ondelete="CASCADE", onupdate="CASCADE"))

	def __repr__(self):
		return f"RECORDS('{self.TIMESTAMP}')"

class U_D(db.Model, UserMixin):
	ID = db.Column(db.Integer, primary_key=True)
	UID = db.Column(db.Integer, db.ForeignKey(USER_DETAILS.UID, ondelete="CASCADE", onupdate="CASCADE"))
	DID = db.Column(db.Integer, db.ForeignKey(DEVICE_ADDRESS.DID, ondelete="CASCADE", onupdate="CASCADE"))


class CIDR_(db.Model, UserMixin):
	ID = db.Column(db.Integer, primary_key=True)
	CIDR1 = db.Column(db.String(4), nullable=False)
	DOTTED = db.Column(db.String(100), nullable=False)
	HEX = db.Column(db.String(12), nullable=False)
	INVERSE = db.Column(db.String(30), nullable=False)
	BINARYNETMASK = db.Column(db.String(100), nullable=False)
	CLASSFULL = db.Column(db.String(20), nullable=False)
	USABLE = db.Column(db.String(20), nullable=False)


	def __repr__(self):
		return f'({self.CIDR1})'