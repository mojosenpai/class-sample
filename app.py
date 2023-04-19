from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello!'

@app.route('/about-me')
def about():
    return 'some text about the company'

app.run()