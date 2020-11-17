from flask import Flask,render_template,url_for,request

posts =[
    {
        'author':'Veera',
        'title': "First Blog Post",
        'content': "Content of first blog post",
        'date posted': "11-Nov-2020"
    },
    {
        'author':'Vignesh',
        'title': "Second Blog Post",
        'content': "Content of second blog post",
        'date_posted': "13-Nov-2020"
    }
]
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html",posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)