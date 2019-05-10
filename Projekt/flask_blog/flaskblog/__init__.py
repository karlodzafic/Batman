from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

										
 #iz paketa flask unesi mi cijelu klasu imena Flask
app = Flask(__name__) 																		
#ovime kazemo di da klasa Flask trazi neke templates i static files nazivom _ _name_ _
#time instaciramo sve u varijablu app

app.config['SECRET_KEY']='c95ec9d7a9a336b10fbd2371f92aa879'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes