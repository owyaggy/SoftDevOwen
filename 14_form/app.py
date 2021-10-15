# Team Toast
# Owen Yaggy, Haotian Gan, Justin Morrill (Duckies: Rio, Gregory, Cinnamon)
# SoftDev
# K13
# 10-14-2021


from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return render_template('login.html')

@app.route("/", methods=['GET']) 
def disp_loginpage():
    
    print(request.args)
    
  
    return render_template( 'login.html' )


@app.route("/auth", methods=['POST']) # , methods=['GET', 'POST'])
def authenticate():
    print(request.form)
    return render_template('response.html', username=request.form['username'])  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()


app.debug = True
app.run()