from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/hello/<name>')
def helo(name=None):
    return render_template('hello.html', name=name)

