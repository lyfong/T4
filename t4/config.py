import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='mysql+pymysql://:3306/t3?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS=False
CSRF_ENABLED=True
SECRET_KEY='ONE TWO THREE'
