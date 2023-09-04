from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/apple')
def page():
    return 'Hello, 사과!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)    