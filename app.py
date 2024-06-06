from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

users = {
    'Oleh Yuzva': '123456',
    'Markiyan Patsai': '654321',
    'Legenda': 'Legenda'
}


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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            flash(f"Вітаю {username}! Ви успішно авторизувались!")

            return redirect(url_for('user', username=username))

    return render_template('login.html')


@app.route('/logout')
def logout():
    username = session.pop('username', None)
    if username:
        flash(f"Вітаю {username} Ви успішно покинули нас :( ")

    return redirect(url_for('home'))


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
