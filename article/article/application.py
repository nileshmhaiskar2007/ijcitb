import os

from flask import Flask,render_template,request 
from .models import Article,Author,User,db 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def home():
""" home page of the site """
return render_template("home.html")



@app.route("/article")
def index():
	""" Call the form for paper data upload by author """
	return render_template("article.html")


@app.route("/author")
def author():
	""" For adding new author """
	return render_template("author.html")


@app.route("/login")
def signin():
	""" for signin to all users """
	return render_template("login.html")


@app.route("/signin_user")
def signin_user():
	""" For checking login credentials """
	pass


@app.route("/paperlist",methods=["GET","POST"])
def paperlist():
	""" Lists all titles with link to full papers """
	papers = Article.query.all()
	return render_template("paperlist.html",papers=papers)


@app.route("/paper_whole/<int:paper_id>")
def paper_whole(paper_id):
	""" Get a paper """
	paper = Article.query.get(paper_id)
	if paper is None:
		return render_template("error.html",message="No such paper")
	return render_template("paper.html",paper=paper)	


@app.route("/submit",methods=["GET","POST"])
def submit():
	""" store all form data """
	if request.method != 'POST':
		return render_template("error.html",message="Please fill the form details first")
	else:
		title = request.form.get('title')
		abstract = request.form.get('abstract')
		keywords = request.form.get('keywords')
		docfile = request.form.get('docfile')
		article = Article(title=title,abstract=abstract,keywords=keywords,docfile=docfile)
		db.session.add(article)
		db.session.commit()
	return render_template("success.html",message="article submitted")


@app.route("/save_author",methods=["GET","POST"])
def save_author():
	""" saving details of author """
	if request.method != 'POST':
		return render_template("error.html",message="Please fill the author details first")
	else:
		fullname = request.form.get('fullname')
		designation = request.form.get('designation')
		email = request.form.get('email')
		address = request.form.get('address')
		phone = request.form.get('phone')
		author = Author(name=fullname,designation=designation,email=email,address=address,phone=phone)
		db.session.add(author)
		db.session.commit()
	return render_template("success.html",message="Author registered for signin check your email") 

	
@app.route("/showall")
def showall():
	""" Show all papers data """
	articles = Article.query.all()
	return render_template("articles.html",articles=articles)




