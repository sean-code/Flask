from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/magic')
def magic():
    return '<ul><li>David Blaine</li><li>Houdini</li><li>Shin lim</li></ul>'