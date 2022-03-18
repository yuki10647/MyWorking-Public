# $env:FLASK_APP = "hello"
# flask run
# cd で直前まで入る
# debug は on のほうが良い
# flask.cli.NoAppException はなんか治った
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
from flask import Flask
from flask import render_template

app = Flask(__name__)

bullets = [
    '箇条書き1', 
    '箇条書き2',
    '箇条書き3',
    '箇条書き4',
]

@app.route("/")
def hello():
    return render_template('hello.html', bullets=bullets)

#@app.route("/japan/<city>")
#def hello(city):
#    return render_template('hello.html', city=city)
# templatesのhello.htmlを引っ張ってくる

