#coding=utf-8
import MySQLdb
import platform
import pymysql
from flask_sqlalchemy import SQLAlchemy
from t4 import app,db
from t4.models import Messages
from t4.forms import BaseLogin
from flask import url_for,render_template,g,jsonify,json,flash,redirect

@app.route('/')
@app.route('/<param>')
def index(param='test'):
    return '<h1>Hello %s </h1>' % param



@app.route('/baselogin',methods=('POST','GET'))
def baselogin():
    form=BaseLogin()
    #判断是否是验证提交
    if form.validate_on_submit():
        #跳转
        flash(form.name.data+'|'+form.password.data,'ok')
        return redirect(url_for('success'))
    else:
        #渲染
        return render_template('baselogin2.html',form=form)
 
@app.route('/success')
def success():
    return render_template('success.html',m='Success')
