import csv

data = {}

with open('occupations.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        data[row[0]] = row[1];

print(data)