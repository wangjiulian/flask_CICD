from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello')
def hello():  # put application's code here
    return 'Hello World!'

def test_hello():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
