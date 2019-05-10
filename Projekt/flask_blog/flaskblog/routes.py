import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm,PostForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.urls import url_parse

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


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('UImain')
            # import pdb; pdb.set_trace()
            if not next_page or url_parse(next_page).netloc !='':
                next_page=url_for('UImain')
            
            return redirect(next_page)
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('index.html', title='Login', form=form)


@app.route("/indexregister", methods=['GET', 'POST'])
def indexregister():

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('index'))
    return render_template('indexregister.html', title='Register', form=form)



@app.route("/UImain")
def UImain():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('UImain.html',posts=posts)




@app.route("/home",methods=['GET', 'POST'])
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts) #ova funkcija nam pomaze da kad dode na stranicu /home da nam prikaze sta nam se nalazi sve u dadoteci home.html
    												#sve sto smo pisali u dicitonary gore smo sada proslijedili u funkicju render_template tako da kad otvorimo home page jos ce nam biti postovi

@app.route("/about") #route smatrajte kao neki ruter koji vam pomaze oko pronalzenja patha na internetu te ovisno o tome sta se nalazi na tom linku ce biti prikazano
def about():
    return render_template('about.html',title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)




@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))







def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (250, 250)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)



@app.route("/profil", methods=['GET', 'POST'])
@login_required
def profil():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profil'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('profil_korisnika.html', title='Account',
                           image_file=image_file, form=form)

@app.route("/pregled")
def pregled():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('Pregled_izleta.html', posts=posts)





def save_post_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/post_pics', picture_fn) #OVDJE PRAVIM PATH ZA SPREMANJE SLIKA IZLETA
    output_size = (250,250) #odredjujem velicinu slike koja je uploadana
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/samiizlet/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_samiizlet(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_post_picture(form.picture.data)
        post.title =form.title.data
        post.content=form.content.data 
         #ovdje ubacivat dodatne stavke za izlete
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('samiizlet', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('noviizlet.html', title='Update Post',
                           form=form, legend='Update Post')



@app.route("/samiizlet/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_samiizlet(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('pregled'))




@app.route("/noviizlet", methods=['GET', 'POST'])
def noviizlet():
    form = PostForm()
    if form.validate_on_submit():
        picture_file = save_post_picture(form.picture.data)
        post = Post(title=form.title.data, content=form.content.data, author=current_user, picture_post=picture_file) #ovdje ubacivat dodatne stavke za izlete
        db.session.add(post)
        db.session.commit() #dodaje izlete u database
        flash('Vas izlet je uspjesno kreiran', 'success')
        return redirect(url_for('UImain'))
    return render_template('noviizlet.html', title='Novi izlet', form=form, legend='Novi izlet')

@app.route("/samiizlet/<int:post_id>")
def samiizlet(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('samiizlet.html', title=post.title, post=post)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        picture_file = save_post_picture(form.picture.data)
        post = Post(title=form.title.data, content=form.content.data, author=current_user, picture_post=picture_file) #ovdje ubacivat dodatne stavke za izlete
        db.session.add(post)
        db.session.commit() #dodaje izlete u database
        flash('Vas izlet je uspjesno kreiran', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')




@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)



@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        picture_file = save_post_picture(form.picture.data)
        post = Post(title=form.title.data, content=form.content.data, author=current_user, picture_post=picture_file)
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)



@app.route("/korisnikizlet/<string:username>")
def korisnikizlet(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=6)
    return render_template('korisnik_izleti.html', posts=posts, user=user)