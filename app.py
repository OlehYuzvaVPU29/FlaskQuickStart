from flask import Flask, render_template, request, redirect, url_for, session, flash
from sqlalchemy.testing.schema import mapped_column

from forms.login_form import LoginForm
from forms.registration_form import RegistrationForm

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users_database.db"
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]


with app.app_context():
    db.create_all()

users = {
    'Oleh Yuzva': '123456',
    'Markiyan Patsai': '654321',
    'Legenda': 'Legenda'
}

app.secret_key = 'supersecretkey'


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/bye")
def bye_world():
    return render_template('bye.html')


@app.route("/hello/<username>")
def hello_user(username):
    return render_template(
        'hello_user.html',
        username=username
    )


@app.route("/users")
def user_list():
    users_list = list(users.keys())

    return render_template(
        'user_list.html',
        users_list=users_list
    )


@app.route("/users/<string:username>")
def user(username):
    if 'username' in session and session['username'] == username:
        return render_template(
            'user.html',
            username=username
        )
    else:
        return redirect(url_for('login'))


@app.route("/posts")
def posts():
    return render_template(
        'posts.html',
        posts=range(1, 11)
    )


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    return render_template(
        'show_post.html',
        post_id=post_id
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            flash(f"Вітаю {username}! Ви успішно авторизувались!")

            return redirect(url_for('user', username=username))

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    username = session.pop('username', None)
    if username:
        flash(f"Вітаю {username} Ви успішно покинули нас :( ")

    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():

        username = request.form['username']
        password = request.form['password']

        new_user = User(
            username=username,
            password=password,
        )
        db.session.add(new_user)
        db.session.commit()

        if username not in users:
            users[username] = password
            session['username'] = username
            flash(f"Вітаю {username}! Ви успішно зареєструвались!")
            return redirect(url_for('user', username=username))
        else:
            flash(f"Користувач з іменем {username} вже існує. Будь ласка, виберіть інше ім'я.")

    return render_template('register.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)

