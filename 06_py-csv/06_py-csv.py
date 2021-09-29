# Goofy Goobers - Oscar Wang, Owen Yaggy, Julia Nelson
# SoftDev
# K06 -- Return a random professional field based on the percentage of jobs in that field
# 2021-09-29

## OUR APPROACH ##
# We first figured out how to read a CSV file using the documentation for the csv module
# After reading the data and storing it in a dictionary, we converted that dictionary to
# one where the percentages are consecutive sums of all of the percentages of the prior
# keys in the dictionary. We decided to do this because it allows us to treat the
# dictionary as one continuous scale, making it easy to randomly pick a point along that
# scale and associate it with a profession. We divided our program into functions for
# readability and ease of use. This also allowed us to test our program with a separate
# function.

import csv
import random


# Random float from 0 to 99.8
# With each item in dict get consecutive sum
# If rand int < sum return item associated with key

def openCSV(fname):
    dict = {}
    total = 0
    with open(fname) as f:
        f.readline()
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if 'Total' in row:
                total = float(row[1])
            else:
                dict[row[0]] = float(row[1])
        return dict, total


def picker():
    jobDict, total = openCSV('occupations.csv')
    total = total * 10
    nums = list(jobDict.values())
    # print(sum(nums))
    occ = list(jobDict.keys())
    conDict = {}
    sum = 0
    for i in range(len(nums)):
        nums[i] *= 10.0
        sum += nums[i]
        nums[i] = sum
    for i in range(len(occ)):
        conDict[occ[i]] = nums[i]
    # print(jobDict)
    # print(conDict)

    # for i in occ:
    n = random.randint(0, total)
    for i in conDict:
        if (n <= conDict[i]):
            return i


def test_probs(n):
    testResults, total = openCSV('occupations.csv')
    for i in testResults:
        testResults[i] = 0
    for i in range(n):
        testResults[picker()] += 1
    for i in testResults:
        testResults[i] = [testResults[i], round(testResults[i] / n * 10000) / 100]
    print(testResults)


def main():
    print(picker())
    # test_probs(10000)


if __name__ == "__main__":
    main()