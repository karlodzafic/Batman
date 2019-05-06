from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy	
from datetime import datetime											
 #iz paketa flask unesi mi cijelu klasu imena Flask
app = Flask(__name__) 																		
#ovime kazemo di da klasa Flask trazi neke templates i static files nazivom _ _name_ _
#time instaciramo sve u varijablu app

app.config['SECRET_KEY']='c95ec9d7a9a336b10fbd2371f92aa879'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)


class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),unique=True,nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
	password=db.Column(db.String(60),nullable=False)
	posts=db.relationship('Post',backref='author',lazy=True)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(100),nullable=False)
	date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	content=db.Column(db.Text,nullable=False)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

	def __repr__(self):
		return f"Post('{self.title}','{self.date_posted}')"

posts=[
	{
		'author':'Karlo Dzafic',
		'title':'Blog Post 1',
		'content':'First post content',
		'date_posted':'May 5,2019'
	
	},

	{
		'author':'Pero Peric',
		'title':'Blog Post 2',
		'content':'Second post content',
		'date_posted':'May 6,2019'
	
	}

]


@app.route("/")
@app.route("/home") #route smatrajte kao neki ruter koji vam pomaze oko pronalzenja patha na internetu te ovisno o tome sta se nalazi na tom linku ce biti prikazano
def home():
    return render_template('home.html',posts=posts,title='Home') #ova funkcija nam pomaze da kad dode na stranicu /home da nam prikaze sta nam se nalazi sve u dadoteci home.html
    												#sve sto smo pisali u dicitonary gore smo sada proslijedili u funkicju render_template tako da kad otvorimo home page jos ce nam biti postovi

@app.route("/about") #route smatrajte kao neki ruter koji vam pomaze oko pronalzenja patha na internetu te ovisno o tome sta se nalazi na tom linku ce biti prikazano
def about():
    return render_template('about.html',title='About')


@app.route("/register",methods=['GET','POST']) 
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html',title='Register',form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__': #pomaze da sa python imefile.py pozovem i runum server 
	app.run(debug=True)