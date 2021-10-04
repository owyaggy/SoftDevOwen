# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

# OBSERVATIONS
# This program is the same as v2, with the exception of app.debug being TRUE
# This means that as we make changes in the code, the live website will update
# NOTE: It actually prints "app" instead of "__main__"

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()
