# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

# OBSERVATIONS
# We predict this will only create a webpage with the text "No hablo queso!",
# with no side effects on the terminal output

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

