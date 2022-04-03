# $env:FLASK_APP = "app"
# $env:FLASK_ENV = "development"
# flask run
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
# 1234 134 245 は登録済み
from ensurepip import bootstrap
from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# sqlite3で
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user  #まず、インポートする
from flask_bootstrap import Bootstrap

from datetime import datetime
import pytz
from werkzeug.security import generate_password_hash, check_password_hash
import os

# powershell で python3 (直下)
# from app import db
# db.create_all()  Post, User 作るのに2回実行する

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

login_manager = LoginManager()  # インスタンス化
login_manager.init_app(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(12))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
@login_required          # ログインしているユーザーのみアクセス
def index():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('index.html', posts=posts)



@app.route('/signup', methods=['GET', 'POST'])  # html を作ったら、@app.route でルーティングを作るという手順
def signup():
    if request.method == 'POST': # formが入力された！
        username = request.form.get('username')  #nameを取り出す
        password = request.form.get('password')

        user = User(username=username, password=generate_password_hash(password, method='SHA256'))

        db.session.add(user)  # 追加して
        db.session.commit()   # 反映する
        return redirect('/login')
    else:
        return render_template('signup.html')



@app.route('/login', methods=['GET', 'POST'])  # html を作ったら、@app.route でルーティングを作るという手順
def login():
    if request.method == 'POST':  # login form が入力されたとき
        username = request.form.get('username')  #nameを取り出す
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('/')
    else:
        return render_template('login.html')



@app.route('/logout')
@login_required          # ログインしているユーザーのみアクセス
def logout():
    logout_user()
    return redirect('/login')




@app.route('/create', methods=['GET', 'POST'])  # html を作ったら、@app.route でルーティングを作るという手順
@login_required         # ログインしているユーザーのみアクセス
def create():
    if request.method == 'POST':
        title = request.form.get('title')  #nameを取り出す
        body = request.form.get('body')
        post = Post(title=title, body=body)

        db.session.add(post)  # 追加して
        db.session.commit()   # 反映する
        return redirect('/')
    else:
        return render_template('create.html')



@app.route('/<int:id>/update', methods=['GET', 'POST'])  # html を作ったら、@app.route でルーティングを作るという手順
@login_required          # ログインしているユーザーのみアクセス
def update(id):
    post = Post.query.get(id)  # 単一でとってくる
    if request.method == 'GET':
        return render_template('update.html', post=post)

    else:
        post.title = request.form.get('title')  #nameを取り出す
        post.body = request.form.get('body')

        db.session.commit()   # 反映する
        return redirect('/')



@app.route('/<int:id>/delete', methods=['GET'])  # html を作ったら、@app.route でルーティングを作るという手順
@login_required          # ログインしているユーザーのみアクセス
def delete(id):
    post = Post.query.get(id)  # 単一でとってくる

    db.session.delete(post)
    db.session.commit()
    
    return redirect('/')
