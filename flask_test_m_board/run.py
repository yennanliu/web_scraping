import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
from flask import request
import pandas as pd, numpy as np 

from controller import scrap



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    message = db.Column(db.String(64)) 

    def __repr__(self):
        return '<User %r>' % self.username


class todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    message = db.Column(db.String(64)) 

    def __repr__(self):
        return '<todo %r>' % self.username


class NameForm(Form):
    name = StringField('What is your name?')
    message = TextAreaField('Please leave a message')
    submit = SubmitField('Submit')
    refresh = SubmitField('Refresh')




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    # array = User.query.all()
    # if not array:
    #     flash('Here is no message,please leave some message.')
    form = NameForm()
    
    if form.validate_on_submit():
        if request.form.get('refresh') == 'Refresh' :
            num_rows_deleted = db.session.query(User).delete()
            db.session.commit()
            return redirect(url_for('index'))
        if request.form.get('submit') == 'Submit' :
            user = User(username=form.name.data,message=form.message.data)
            db.session.add(user)       
            return redirect(url_for('index'))
    
    array = User.query.all()
    if not array:
        flash('Here is no message,please leave some message.')
    return render_template('index.html', form=form, array=array)



@app.route('/list')
def show_all():
    print (User.query.all())
    return render_template('show_all.html', User = User.query.all() )

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('success_login'))
    return render_template('login.html', error=error)


@app.route('/success_login')
def success_login():
    return "Welcome Login !"  

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  

@app.route('/scraping')
def scraping():
    data = scrap()
    print ('type = ')
    print (type(data))
    return render_template('scraping.html',data=data)
    return render_template('scraping.html',tables=data.head(1).to_html(),titles = ['SCARPING'])
    #return render_template('welcome.html')  









if __name__ == '__main__':
    app.run(debug = True)
    db.create_all()
    manager.run()