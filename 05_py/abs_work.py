# Owen Yaggy, Justin Morill, Aaron Contreras
# SoftDev
# K05 -- Pick a name from period 1 and period 2
# 2021-09-28

# SUMMARY OF TRIO DISCUSSION
# We discussed how whether to amalgamate or "winner take all" and decided to go with
# with a modified version of one person's code. We discussed how to extract data
# from a dictionary, and decided to store the lists contained in the dictionary
# within a standalone "final" list, from which we could draw a random name. We
# decided add information to othe "final" list in twoo separate lines to improve
# readability.
# DISCOVERIES
# We discovered that random.randrange was a more efficient way to pick a random
# name from a list.
# QUESTIONS
# ...
# COMMENTS
# ...

import random
# import random module to allow picking of random number

KREWES = {
    'orpheus': ['whosit','whatsit'],
    'endymion': ['fee','fye','foe']
}
# set up dictionary with a list of names stored under each key, which represents a group

final = KREWES['orpheus'] # create a new list with the first list of people
final += KREWES['endymion'] # add the second list of people, creating combined list
print(final[random.randrange(len(final))]) # print a random name from the combined list
