#coding=utf-8
from datetime import datetime
from t4 import db
from flask import json

class tt(db.Model):
    __tablename__='tt'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    timestamp=db.Column(db.DateTime, default=datetime.utcnow, index=True)

class Messages(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    body=db.Column(db.String(200))
    timestamp=db.Column(db.DateTime, default=datetime.utcnow, index=True)
    def to_json(self):
        json_data = {
           'id':self.id,
           'name':self.name,
           'body':self.body,
           'time':self.timestamp
        }
        return json.dumps(json_data)
    def __repr__(self):
        return 'Id:%r' % self.id

class DateEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime(DATETIME)
        elif isinstance(obj,datetime.date):
            return obj.strftime(DATE)
        elif isinstance(obj,Decimal):
            return str(obj)
        else:
            return json.JSONEncoder.default(self,obj)

#from wtf import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __repr__(self):
        return '<User %r>' % self.username
