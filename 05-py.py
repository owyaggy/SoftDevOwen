# Owen Yaggy
# SoftDev
# K05 -- Group work on names assignment
# 2021-09-27

# POW-WOW SUMMARY
# We talked about our various code. The main difference in our code was that
# in some cases we had decided to implement user input, and we had varying
# methods of extracting a random name from a list.

# DISCOVERIES
# Random needs to be imported, lists can be combined in a single line, and
# list.append(data) is a valid way of adding to a list in Python.

import random
pd1 = ["Gavin", "Seymour", "John"]
pd2 = ["Frank", "Alex", "Maxwell"]

final = pd1 + pd2
print(final[random.randint(0, len(final) - 1)])
