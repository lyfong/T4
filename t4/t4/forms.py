from flask_wtf import Form
from wtforms import StringField,TextField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length
#from flask_wtf.recaptcha import RecaptchaField

from werkzeug import secure_filename
from flask_wtf.file import FileField

class BaseLogin(Form):
    name = StringField('username', validators=[DataRequired(message=u'用户名不能为空'),Length(10,20,message=u'长度位于10~20之间')],render_kw={'placeholder':u'输入用户名'})
    password = StringField('password', validators=[DataRequired()],render_kw={'placeholder':u'输入用户密码'})
    remember_me = BooleanField('remember_me', default=False)
#    recaptcha = RecaptchaField()
    submit = SubmitField(
        label="登录",
        render_kw={"class": "btn btn-lg btn-success btn-block"}
    )
        
class UploadForm(Form):
    file = FileField()
