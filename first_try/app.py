from flask import Flask, render_template, redirect, session, request, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "adolf_"
app.permanent_session_lifetime = timedelta(days=1)


@app.route('/second', methods=["POST", "GET"])
def second():
    if request.method == "POST":
        user = request.form["nm"]
        pas_ = request.form["pas_"]
        session["user"] = user
        session["password"] = pas_
        session["login"] = True
        
        return redirect(url_for("firth"))
    else:
        return render_template('second.html')   


def is_login():
    if session["login"] == True:
        return True
    else:
        return False

def account_exist(name, pas):
    if session["user"] == name and session["password"] == pas:
        True
    else:
        False


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/2')
def third():
    if is_login():
        return render_template('index.html')
    else:
        return redirect(url_for("second"))

@app.route('/main')
def firth():
    if is_login():
        return render_template('main.html')
    else:
        return redirect(url_for("second"))


if __name__ == "__main__":
    app.run(debug=True)