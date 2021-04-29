import os
import json
from flask import Flask, render_template # the render template function allows us to not write all of our html in a python file

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html") # Flask would find this file on the same level of our run.py file, in a folder called "templates"


@app.route("/about") # Argument passed here represents a file name. The names underneath have to correspond with the argument passed into the url_for functions on our HTML page
def about():
    data = []
    with open("data/company.json", "r") as json_data: # First we create an empty python list as data. We then open our json data with open() passing in its location as the 1st arguemnt
        # and "r" stands for read only. We then name the data as json_data. The method then parses the json data and we name it data which is then passed into render_template
        # as company (this will be i n the form of an array)
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company = data) # render_template takes as many arguemnts as you like. Variable name page_title could have been anything


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")

# Two blank lines between each python function is good code practice
if __name__ == "__main__": 
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True 
    ) 

    