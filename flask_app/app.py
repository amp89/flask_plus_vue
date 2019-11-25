from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello():
    return render_template('index.html')

app.run(host='127.0.0.1', port=8181, debug=False)


