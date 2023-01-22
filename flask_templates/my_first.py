import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

DATABASE = '/tmp/fiks.db'
DEBUG = True
SECRET_KEY = 'dfc3d370a23c8c6fc6129c4fae226867ca8c4134'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'fiks.db')))


def connect_db():
    van = sqlite3.connect(app.config['DATABASE'])
    van.row_factory = sqlite3.Row
    return van


def create_db():
    db = connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [
    {"name": "Начальная страница", "url": "index"},
    {"name": "Меню приложения", "url": "about"},
    {"name": "Контакты", "url": "contact"},
]


@app.route('/index')
@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Начальная страница', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='Меню приложения', menu=menu)


@app.route('/contact', methods=['POST', 'GET'])
def contacts():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено успешно!', category='success')
        else:
            flash('Ошибка отправки', category='error')
    return render_template("contacts.html", title="Контакты", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


if __name__ == '__main__':
    app.run(debug=True)
