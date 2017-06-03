from flask import Flask, render_template, session, request, url_for, redirect
from apps.database import db_session
from apps.models import PMEB

app = Flask(__name__)
app.secret_key =b'JSz\xf8\x1cR\xdd\x04\xbf>\x15d\x02\x8c\x08\xc0*\x8f?d\x89:\x0b\x87'

def pmebList():   
    pmeb = list()
    for p in PMEB.query.all():
        s = str(p).split(", ")
        try:
            pmeb.append(s)
        except:
            pass
    return pmeb

def confirmLogin():
    try:
        if session["pw"] == "hongrae":
            return True
        else:
            return False
    except:
        return False

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/")
def index():
    return render_template("index.html", login=confirmLogin())

@app.route("/login", methods=['GET', 'POST'])
def login():
    if confirmLogin() == True:
        return redirect(url_for("index"))
    if request.method == 'POST':
        pw = request.form["pw"]
        if pw == "hongrae":
            session["pw"] = "hongrae"
            return redirect(url_for("index"))
        else:
            return render_template("login.html", login=confirmLogin(), message="Please try again")
    return render_template("login.html", login=confirmLogin(), message="")

@app.route("/logout")
def logout():
    session.pop("pw", None)
    return redirect(url_for("index"))

@app.route("/pmeb", methods=["GET", "POST"])
def pmeb():
    if confirmLogin() == False:
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':        
            date = request.form["date"]
            content = request.form["content"]
            money = request.form["money"]

            p = PMEB(str(date), str(content), int(money))

            db_session.add(p)
            db_session.commit()
                        
            return redirect(url_for("pmeb"))
        return render_template("pmeb.html", pmeb=pmebList())
