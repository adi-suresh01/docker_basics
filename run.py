from flask import Flask
from _datetime import datetime

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to my webpage"


@app.route('/time')
def visit_time():
    current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return "Current time: {}".format(current_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
