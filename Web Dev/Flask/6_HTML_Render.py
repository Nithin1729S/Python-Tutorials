from flask import Flask
app=Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/")
@make_bold
def hello_world():
    return "Hello, World!!!"

@app.route("/username/<name>")
def greet(name):
    return f"<h1 style='text-align:center'>Hello, {name}!</h1>" \
           f"<p style='text-align:center'>This is a paragraph</p>" \
           f"<img src='https://picsum.photos/200/300?grayscale'>"


if __name__ == '__main__':
    app.run(debug=True)

