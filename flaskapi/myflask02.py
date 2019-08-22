#!/usr/bin/python3

from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello admin!"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return f"Hello, How are you {guest}"

#app = Flask(__name__)

@app.route("/hello/<name>")

def hello(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest",guest=name))


if __name__ == "__main__":
    app.run(port=5006)
