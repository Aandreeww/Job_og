from flask import Flask, request, url_for, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
db_session.global_init("db/mars_explorer.db")


@app.route("/ans")
def index():
    ids = {}
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    for user in db_sess.query(User).all():
        ids[user.id] = f"{user.name} {user.surname}"
    return render_template("login.html", news=news, ids=ids)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1', debug=True)