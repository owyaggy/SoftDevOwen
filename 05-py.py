import random
pd1 = ["Gavin", "Seymour", "John"]
pd2 = ["Frank", "Alex", "Maxwell"]

final = pd1 + pd2
print(final[random.randint(0, len(final) - 1)])
