from flask import Flask,render_template,url_for,request

app = Flask("__name__")

@app.route('/')
def home():
    return "Hello World"


if "__name__"=="__main":
    app.run(debug=True)