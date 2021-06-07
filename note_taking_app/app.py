from flask import Flask, session, redirect, url_for, escape, request,render_template,flash

app = Flask(__name__)
app.secret_key = 'harish'


@app.route('/')
def entry():
    if 'username' in session:
        username = session['username']
        return 'Welcome ' + username + '<br>' + "<b><a href = '/logout'>Logout</a></b>"
    return "<b>Please log in to access the note<a href = '/login'></b>" + " <b>Login</b></a>"


notes=[]
@app.route('/',methods=['POST'])
def index():
    n = request.form.get("note")
    notes.append(n)
    return render_template('home.html', notes=notes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    notes.clear()
    if request.method == 'POST':
        session['username'] = request.form['username']

        return render_template('home.html')

    return "<form action = '' method = 'post'> " + \
           "<p><input type = 'text' name = username></p> " + \
           "<p><input type = 'submit' value = Login></p> " + \
           "</form>"



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('entry'))

if __name__ == '__main__':
    app.run(debug=True)