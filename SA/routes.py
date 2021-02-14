from flask import flash, request, redirect, url_for, render_template
#from SA.utils import dictionary, save_image, predict
from SA.forms import LoginForm
from SA.twitter_collector import twitter
from SA import app
#from flask_login import login_user, current_user, logout_user

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'sentiment@tcs.com' and form.password.data == 'tcs@1234':
			flash("Welcome to Sentiment Analysis Dashboard", 'success')
			graph = twitter()
			return render_template('graph.html', title='Dashboard', graph=graph)
			redirect(url_for('upload'))
		else:
			flash("Wrong Credentials", 'danger')
	return render_template('login.html', form=form, title='Login')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	return render_template('graph.html', title='Dashboard')