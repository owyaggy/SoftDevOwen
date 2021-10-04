# Goofy Goobers - Oscar Wang, Owen Yaggy, Julia Nelson
# SoftDev
# K10 -- Return a random professional field based on the percentage of jobs in that field
# 2021-10-06

## OUR APPROACH ##
# We first figured out how to read a CSV file using the documentation for the csv module
# After reading the data and storing it in a dictionary, we converted that dictionary to
# one where the keys/percentages are consecutive sums of all of the percentages of the
# prior keys in the dictionary. We decided to do this because it allows us to treat the
# dictionary as one continuous scale, making it easy to randomly pick a point along that
# scale and associate it with a profession. We divided our program into functions for
# readability and ease of use. This also allowed us to test our program with a separate
# function.

# imports csv and random as we will be using functions from those modules
import csv
import random

# creates a function called openCSV which returns a dictionary where the value is a float
# representing the percent change of being chosen and the total is the total of those
# values (since they may not add up to exactly 100)
def openCSV(fname):
    # creates an empty dictionary and sets the temp_total and total to 0
    dict = {}
    temp_total = 0
    total = 0
    # opens the files and gives it the name f
    with open(fname) as f:
        # reads the first line (where the title is) so that it will not impact the dict
        f.readline()
        # creates a csv reader of f, indicates that a comma is separation
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            # if the row is contians 'Total', instead of being saved to the dict, its
            # float is saved as total
            if 'Total' in row:
                total = float(row[1])
            else:
                # creates a new row at the start of the dict with the first element
                # read in by the csv as the key and the second as the value
                dict[row[0]] = float(row[1])
                # keeps track of consecutive sum of the values
                temp_total += float(row[1])
        # if a total is not given, sets it to the consecutive some of the value
        if total == 0:
            total = temp_total
        return dict, total

# picks an occupation based on the weighted percentages
def picker():
    jobDict, total = openCSV('occupations.csv')
    # we multiply the total by 10 so that it is represented as an integer, since the
    # randint function will produce an integer
    total = total * 10
    # creates a list of the perfecntages and occupations (indexed similarly)
    nums = list(jobDict.values())
    # print(sum(nums))
    occ = list(jobDict.keys())
    conDict = {}
    sum = 0
    # the key for the index is set as the occupation, and the value as ten times the
    # consecutive sum (so that it can be used for randint)
    for i in range(len(nums)):
        nums[i] *= 10.0
        sum += nums[i]
        nums[i] = sum
    for i in range(len(occ)):
        conDict[occ[i]] = nums[i]
    # print(jobDict)
    # print(conDict)

    # for i in occ:
    # picks a random int from 0 inclusive to total exclusive so that the number of
    # integers picked equals the possibility for probabilities
    n = random.randint(0, total-1)
    # for occupations in conDict if the randomly selected integer is less than the
    # consecutive probability it will be returned
    for i in conDict:
        if (n < conDict[i]):
            return i

# Picks random occupations repeatedly until it reaches n trials then checks to see
# if the outcomes of what was picked match their probabilities, will not be run
# in final code
def test_probs(n):
    # reads the csv file and stores its data in a dictionary using prebuilt function, stores total percent
    testResults, total = openCSV('occupations.csv')
    # loop through keys and set their counters to 0
    for i in testResults:
        testResults[i] = 0
    # run n trials - each time key (a profession) is returned increment its value in the dictionary by 1
    for i in range(n):
        testResults[picker()] += 1
    # loop through dictionary and convert value to a list with the number of times returned and a percentage
    for i in testResults:
        testResults[i] = [testResults[i], round(testResults[i] / n * 10000) / 100]
    print(testResults)


def main():
    print(picker())
    # test_probs(10000)

# ensures that the not every previous function will have to run before the main one
# (which should be called first
if __name__ == "__main__":
    main()
