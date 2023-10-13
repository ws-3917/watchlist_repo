from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	str = '<h1>哈啦呜</h1> <img src="https://www.zsucai.com/files/2014/0724/140612199224757/zsucai140612245525iy100.jpg"><br>文件列表<br>Kind_Sheet.xlsx<br>Result.jpg'
	return str
