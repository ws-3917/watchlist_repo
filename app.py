from flask import Flask, url_for
from markupsafe import escape
app = Flask(__name__)
@app.route("/")
@app.route("/index")
def hello():
	str = 'hello'
	return str

@app.route("/user/<newname>")
def displayname(newname):
	return f"unanthorized visit! {escape(newname)}"

@app.route("/test")
def test_for():
	print(url_for("hello"))
	print(url_for("displayname", newname="ws"))

	print(url_for("test_for"))
	print(url_for("test_for", num=2, ws='8d8', we = 33))

#	print(url_for("error"))

	return 'ok'