import os
import json
from flask import Flask, render_template, request, flash # the render template function allows us to not write all of our html in a python file
# request finds out what method we used and contains our form object when we've posted it. flash is used to display a message that will leave after navigating to a new page or reloading

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

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


@app.route("/about/<member_name>") # Angle brakcets will pass in the data from the url path into the view below
def about_member(member_name): # is the same member_name from above. So whenever we route from about into something deeper, we are using this view
    member={}
    with open("data/company.json", "r") as json_data: # opening our json file in read only access
        data = json.load(json_data) # here we pass the data through and convert it into JSON and store it in a python array
        for object in data:
            if object["url"] == member_name:
                member = object 
        return render_template("member.html", member=member) #
    
     
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(request.form.get("name"))) # Output is a dictionary therefore dictionary methods are used to accesss data
    return render_template("contact.html", page_title="Contact")

# Two blank lines between each python function is good code practice
if __name__ == "__main__": 
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True 
    ) 

    