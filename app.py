from flask import Flask
from flask import render_template
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
