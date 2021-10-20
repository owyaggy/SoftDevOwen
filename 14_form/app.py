# Team Toast
# Owen Yaggy, Haotian Gan, Justin Morrill (Duckies: Rio, Gregory, Cinnamon)
# SoftDev
# K13
# 10-14-2021

from flask import Flask  # Facilitate flask webserving
from flask import render_template  # Facilitate jinja templating
from flask import request  # Facilitate form submission

# Create Flask object
app = Flask(__name__)


"""
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future
self and/or current teammates understand what is going on.
"""


@app.route("/", methods=["GET"])
def disp_loginpage():
    """Returns the login page."""
    return render_template("login.html")


@app.route("/auth", methods=["POST", "GET"])
def authenticate():
    """Returns the response page, including the username, request method, and
    greeting."""
    if app.debug:
        print("\n\n\n")
        print("***DIAG: this Flask obj ***")
        print(app)
        print("***DIAG: request obj ***")
        print(request)
        print("***DIAG: request.args ***")
        print(request.args)
    return render_template(
        "response.html", username=request.args["username"], method=request.method
    )

@app.route("/auth", methods=["GET"])
def provide_user():
    """Returns the login page"""
    return render_template("login.html")

if __name__ == "__main__":  # False if this file imported as module
    # Enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()