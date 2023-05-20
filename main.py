from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # get form data
    data = request.get_json()
        
        # Print the received data
    print(data)
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,debug=True)
