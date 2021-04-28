import os
from flask import Flask, render_template # the render template function allows us to not write all of our html in a python file

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html") # Flask would find this file on the same level of our run.py file, in a folder called "templates"

@app.route("/about") # Argument passed here represents a file name. The names underneath have to correspond with the argument passed into the url_for functions on our HTML page
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__": 
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True 
    ) 