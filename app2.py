from flask import Flask,render_template,send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    message = "ㅇㅅㅇ"
    return render_template("index.html", message=message)

@app.route("/<path:name>")
def page(name):
    return send_from_directory("templates", name)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)