from flask import Flask
from flask_sqlalchemy import SQLAlchemy

apps = Flask(__name__)
apps.config.from_object('config')
db = SQLAlchemy(apps)


import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(apps)
lm.login_view = 'login'
oid = OpenID(apps, os.path.join(basedir, 'tmp'))
