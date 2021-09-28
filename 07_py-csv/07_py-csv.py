import csv
import random


def open_csv(fname):
    data = {}
    sum = 0
    with open(fname, newline='') as f:
        f.readline()
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0] not in 'Total':
                data[row[0]] = float(row[1])*10
    return data


def consecutive_sum_dict(data):
    n = 0
    for key in data:
        data[key] += n
        n = data[key]
    return data




def main():
    data = open_csv('occupations.csv')
    data = consecutive_sum_dict(data)
    print(data)


main()
