from flask import Flask, url_for, request, render_template, Markup, flash, redirect


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in !')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    # return "Hello World!"
    # return request.method
    # return url_for('static', filename='style.css')
    return render_template('hello.html', name=Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>')

@app.route("/user/<username>")
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print(url_for('hello', name="lily"))
    print(url_for('show_post', post_id=12))

if __name__ == "__main__":
    app.run(debug=True) 