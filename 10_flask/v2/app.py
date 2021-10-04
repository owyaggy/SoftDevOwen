# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

# OBSERVATIONS
# We predict this will output "about to print __name__..." and "__main__" to the terminal
# it will also create a webpage with the text "No hablo queso!"
# We also noticed every time you reload the page the terminal output occurs again

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

