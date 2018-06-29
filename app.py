from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_user():
    user = {'name': 'Arno'}
    return render_template("hello-user.html", title='Home', user=user)


if __name__ == '__main__':
    app.run(debug=True)
