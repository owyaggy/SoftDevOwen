# Team Toast
# Owen Yaggy, Haotian Gan, Justin Morrill
# SoftDev
# K15
# 10-14-2021

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
try:
    c.execute("DROP TABLE courses")
    c.execute("DROP TABLE students")
except:
    print("no preexisting database tables found")

with open('courses.csv') as csvfile:
    c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        c.execute(f"INSERT INTO courses VALUES ('{row['code']}', {row['mark']}, {row['id']})")

with open('students.csv') as csvfile:
    c.execute("CREATE TABLE students (code TEXT, mark INTEGER, id INTEGER)")
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        c.execute(f"INSERT INTO students VALUES ('{row['name']}', {row['age']}, {row['id']})")

'''
Output Verification:
for row in c.execute("SELECT * FROM courses"):
    print(row)

for row in c.execute("SELECT * FROM students"):
    print(row)
'''

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


