from flask_sqlalchemy import SQLAlchemy 


db = SQLAlchemy()


class Author(db.Model):
	""" For creating paper authors """

	__tablename__ = "author"
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String,nullable=False)
	designation = db.Column(db.String,nullable=False)
	email = db.Column(db.String,nullable=False)
	address = db.Column(db.String,nullable=False)
	phone = db.Column(db.Integer,nullable=False)
	articles = db.relationship("Article",backref="article",lazy=True)


class Article(db.Model):
	""" For creating article papers """ 

	__tablename__ = "article"

	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String,nullable=False)
	abstract = db.Column(db.String,nullable=False)
	keywords = db.Column(db.String,nullable=False)
	docfile = db.Column(db.String,nullable=False)
	author_id = db.Column(db.Integer,db.ForeignKey("author.id"),nullable=False)



class User(db.Model):
	""" for creating all users """
	
	__tablename__ = "user"
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String,unique=True,nullable=False)
	password = db.Column(db.String(128))




	
	