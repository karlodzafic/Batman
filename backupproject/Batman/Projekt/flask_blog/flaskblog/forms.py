from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField 
#ovo nam pomaze da u formi ce sadrazavati neka polja tipa string,ili password,etc...
from wtforms.validators import DataRequired, Length, Email, EqualTo 
#sluzi da potrazi nekakve podatke pod obaveznim i nekim kritetrijama
#sad cemo ovdje pisati neke nase klase sta ce nam sadrzavati koja forma
#u klasi RegistrationForm ce sadrzavati sve od FlaskForm (nasljedivanje)

class RegistrationForm(FlaskForm):
	username=StringField('Username',
							validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',
						validators=[DataRequired(),Email()])
	password=PasswordField('Password',
						validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password',
						validators=[DataRequired(),EqualTo('password')])

	submit=SubmitField('Sign Up')


class LoginForm(FlaskForm):
	
	email=StringField('Email',
						validators=[DataRequired(),Email()])
	password=PasswordField('Password',
						validators=[DataRequired()])
	remember=BooleanField('Remeber me')
	submit=SubmitField('Login')