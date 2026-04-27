from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Sucessfull run!"

@app.route('/hello')
def hello():
    return "Hello, DevOps!"

@app.route('/home')
def home():
    return "Hello, home!"

@app.route('/ktm')
def ktm():
    return "Hello, Welcome to kathmandu!"

@app.route('/pipeline')
def pipeline():
    return "Pipeline Triggred sucessfully"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)