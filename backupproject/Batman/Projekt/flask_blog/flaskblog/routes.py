from flaskblog.models import User,Post
from flaskblog import app
from flask import render_template, url_for,flash,redirect
from flaskblog.forms import RegistrationForm, LoginForm


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
@app.route("/index", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('index.html', title='Login', form=form)



@app.route("/indexregister", methods=['GET', 'POST'])
def indexregister():
	form=RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('indexregister.html',title='Register',form=form)







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