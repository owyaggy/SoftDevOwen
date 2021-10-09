# Unicorns - Lucas Tom-Wong (LTW), Owen Yaggy, Justin Morrill
# SoftDev
# K13 -- Template for Success/Flask Template Usage/Uses Flask and Templates to display occupations on an html page
# 2021-10-8
# Contains code copied from k10

import csv, random
from flask import Flask, render_template
app = Flask(__name__)

def read_occupations(filename):
    dict = {}
    with open(filename) as f:
         lines = csv.reader(f, delimiter=',')
         next(lines) # Skips the header of the csv

         for line in lines: # Loops through each line of the csv
             job = line[0]
             percentage = float(line[1]) # Converts string to a number
             link = line[2]

             dict[job] = [percentage, link] # Crates a new dict entry with the job and percentage

    del dict['Total'] # Removes the sum of all the percentages
    return dict

def get_random_occupation(dict):

    # Chooses a random key using the values as weights
    # Returns a list with one element
    # print(list(dict.keys()))
    # print(list(dict.values()))
    w = []
    for i in dict.values():
        w.append(i[0])
    choice = random.choices(list(dict.keys()), weights = w, k = 1)
    print(choice)
    return choice[0] # Picks out the first element

app = Flask(__name__)

@app.route('/')
def main_page():
    return '<a href="http://127.0.0.1:5000/occupyflaskst">Click here</a>'
    # if page loaded at main route ('/') display a link to the occupyflaskst route

@app.route("/occupyflaskst")
def display_occupations():
    occupations = read_occupations('data/occupations.csv')
    choice = get_random_occupation(occupations)
    return render_template('tablified.html', c = choice, t = 'Random Occupation', o = occupations)


if __name__ == "__main__":
    app.debug = True
    app.run()
