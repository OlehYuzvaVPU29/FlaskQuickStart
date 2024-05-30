from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/bye")
def bye_world():
    return render_template('bye_html')


@app.route("/hello/<username>")
def hello_user(username):
    return render_template('hello_user.html', username=username)


@app.route("/users")
def user_list():
    users_list = [
        'Oleh Yuzva',
        'Markiyan Patsai',
        'Legenda'
    ]

    return render_template(
        'user_list.html',
        users_list=users_list
    )


@app.route("/users/string:username>")
def user(username):
    return render_template(
        'user.html',
        username=username,
    )


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=range(1, 11))


@app.route("/posts/<post_id>")
def show_post(post_id):
    return render_template('show_post.html', post_id=post_id)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/about')
def about():
    return render_template('about.html')
