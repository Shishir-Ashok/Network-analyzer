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
	# image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	PASSWORD = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.USERNAME}', '{self.EMAIL}')"

	def get_id(self):
		return (self.UID)
