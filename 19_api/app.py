# LoremIpsum: Owen Yaggy, Justin Morrill
# SoftDev Pd 1
# K19 -- API Basics
# 2021-11-23

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def display():
    with open('key_nasa.txt') as api_key:
        key = api_key.read()

    api_request = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}&count=1")#, params={"api_key": key, "count": 1})

    if api_request.status_code == 200:
        # because of count=1 in request, api_request.json() is a list of length 1, which is why [0] must be used
        pic = api_request.json()[0]["hdurl"]
        title = api_request.json()[0]['title']
        description = api_request.json()[0]['explanation']
        date = api_request.json()[0]['date']
        return render_template('main.html', pic = pic, title = title, description = description, date = date)
    return render_template('main.html')

if __name__ == "__main__":
    app.debug = True
    app.run()