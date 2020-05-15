# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class RequestForm(FlaskForm):
    method = StringField("请求方式")
    url = StringField("url")
    header = StringField("请求头")
    params = StringField("参数")
    body = StringField("请求体")
    request = SubmitField("发送")
