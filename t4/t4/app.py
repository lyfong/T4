#coding=utf-8
#import MySQLdb
import platform
import click
from flask import Flask,render_template,g,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(t4)
app.config.from_object('config')
app.debug=True
from t4 import commands

db=SQLAlchemy(app)

class tt(db.Model):
    __tablename__='tt'
    id=db.Column(db.Integer,primary_key=True)

@app.route('/')
@app.route('/<param>')
def index(param='test'):
    return '<h1>Hello %s </h1>' % param

@app.route('/tt')
def get_tt():
#    t=tt.query.first()
#    return '<h1>tt.id is %d !</h1>' % t.id
    t=tt.query
    return render_template('t1.html',tt=t)

@app.route('/ttt')
def get_ttt():
    g.db=MySQLdb.connect('','root','','t3',3306)
    c=g.db.cursor()
    c.execute('select * from tt')
    msgs=list(c.fetchall())
    html=''
    l = []
    for row in msgs:
        row = '%d'%row
        l.append(row)
#        html +=  '<p>' + '%d'%row + '</p>'
    return render_template('t1.html',tt=l)
#    return html

@app.route('/sys')
def platform_msg():
    html=''
    msgs = list(platform.uname())
    for row in msgs:
        html += '<p>' + row + '</p>'
    html += '<p>操作系统名称及版本号: '  + str(platform.platform()) + '</p>'
    html += '<p>操作系统版本号: '  + str(platform.version()) + '</p>'
    html += '<p>操作系统位数: '  + str(platform.architecture()) + '</p>'
    html += '<p>计算机类型: '  + platform.machine() + '</p>'
    html += '<p>计算机网络名称: '  + platform.node() + '</p>'
    html += '<p>计算机处理器信息: '  + platform.processor() + '</p>'
    html += '<p>Python版本号: '  + str(platform.python_version()) + '</p>'
    return html

if __name__=='__main__':
    app.run('0.0.0.0')
