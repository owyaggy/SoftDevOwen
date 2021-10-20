# Team Toast
# Owen Yaggy, Haotian Gan, Justin Morrill (Duckies: Rio, Gregory, Cinnamon)
# SoftDev
# K15
# 10-14-2021

accounts = {
    "Justin" : "Stuyvesant"
}
import os
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__) 

app.secret_key = os.urandom(32)

@app.route("/", methods=['GET']) 
def disp_loginpage():
    """Landing page for the site"""
    if(session.get("username")):
        return render_template('login.html', loggedIn=True, username=session.get("username"))
    return render_template( 'login.html', loggedIn=False )

@app.route("/logout", methods=['GET'])
def logout():
    if(session.get('username')):
        session.pop('username')
    return redirect("/", code=302)


@app.route("/auth", methods=['POST', 'GET']) 
def authenticate():
    """
    Gives the client a session cookie with their username as its value, in response to a successful login.
    Unsuccessful logins return an error page.
    """
    if(request.method == 'GET'):
        return redirect("/", code=302)

    ##If request.method == 'POST'
    try:
        requestArguments = {
            'username': request.form.get('username'), 
            'password': request.form.get('password')
        }
        if(requestArguments['username'] not in accounts or 
            requestArguments['password'] != accounts[requestArguments['username']]):
            raise Exception("Credentials were incorrect.")
        
        if(session.get("username")):
            return redirect("/", code=302)
        else:
            session["username"] = requestArguments['username']
        return render_template('response.html', **requestArguments)
    except Exception as e:
        return render_template('response.html', error=True, errorMessage=e) 
    
    


    
if __name__ == "__main__": 
    app.debug = True 
    app.run()


app.debug = True
app.run()