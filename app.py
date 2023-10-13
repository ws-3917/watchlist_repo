from flask import Flask, url_for, render_template
from markupsafe import escape
app = Flask(__name__)
name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
@app.route("/")
def index():
    return render_template("index.html", name=name, movies=movies)
# @app.route("/index")
# def hello():
# 	str = 'hello'
# 	return str

# @app.route("/user/<newname>")
# def displayname(newname):
# 	return f"unanthorized visit! {escape(newname)}"

# @app.route("/test")
# def test_for():
# 	print(url_for("hello"))
# 	print(url_for("displayname", newname="ws"))

# 	print(url_for("test_for"))
# 	print(url_for("test_for", num=2, ws='8d8', we = 33))

# #	print(url_for("error"))

# 	return 'ok'