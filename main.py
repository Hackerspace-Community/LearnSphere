from flask import Flask, redirect, render_template,request, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from gpt import query
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # get form data
    if request.method == 'POST':
        data = request.get_json()
        result = query(data)
        print("Result",result)
        return jsonify(data = {
            'result': result
        })
        
@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # get form data
        data = request.get_json()
        print(data)
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get form data
        data = request.get_json()
        print(data)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,debug=True)
