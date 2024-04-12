from flask import Flask

app=Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!!!"

@app.route("/bye")
def say_bye():
    return "Good Bye"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name+'12'}!"

@app.route("/dir/<path:name>")
def path(name):
    return f"Your path is {name}"

@app.route("/username/<name>/<int:number>")
def greeting(name,number):
    return f"Hi {name}! You are {number} years old."


if __name__ == '__main__':
    app.run(debug=True)

