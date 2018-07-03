from flask import Flask
from flask import render_template, flash, redirect
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
import models


@app.route('/')
def hello_user():
    user = {'name': 'Arno'}
    posts = [
        {
            'author': {'name': 'Ar'},
            'body': 'This is test!'
        },
        {
            'author': {'name': 'no'},
            'body': 'No!'
        }
    ]
    return render_template("hello-user.html", title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])


if __name__ == '__main__':
    app.run(debug=True)
