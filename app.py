from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello! This is Cloud Engineering Sample Web Applications"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
