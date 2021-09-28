import csv
import random


def open_csv(fname):
    data = {}
    with open(fname, newline='') as f:
        f.readline()
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0] not in 'Total':
                data[float(row[1])] = row[0]
    return data


print(open_csv('occupations.csv'))
