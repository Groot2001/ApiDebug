# coding=utf-8

from flask import Flask,redirect,render_template
from form import RequestForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "123456"

@app.route('/', methods=["GET","POST"])
def index():
    form = RequestForm()
    if form.validate_on_submit():
        print(form.method.data)
        return render_template('index.html',form = form, sent = "已发送")
    return render_template('index.html', form = form)

@app.route('/success', methods=["GET"])
def success():
    return "请求发送成功！"

if __name__=="__main__":
    app.run(debug=True)