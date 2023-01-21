from flask import Flask, render_template, url_for

app = Flask(__name__)

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


@app.route('/contact')
def contacts():
    print(url_for('contacts'))
    return render_template('contacts.html', title='Контакты', menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


if __name__ == '__main__':
    app.run(debug=True)
