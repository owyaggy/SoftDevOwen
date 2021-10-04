# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

# OBSERVATIONS
# We predict this will output "the __name__ of this module is... __main__" to the terminal
# it will also create a webpage with the text "No hablo queso!"

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
