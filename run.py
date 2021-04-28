import os
from flask import Flask # importing class from flask, capital is important

app = Flask(__name__) # creating an instance of this as a variable called app. the first arguement is the name of the applications module/package

@app.route("/") # decorator (@) a way of wrapping functions
def index():
    return "Hello, World!" # / indicates root directory which wuld then cause flask to trigger the index function designated under our app decorator


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )