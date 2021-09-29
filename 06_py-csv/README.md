## Weighed Randomized Selection
* We decided that the easiest way to implement weighted randomization would be to
pick a random number within the total percentage (up to 99.8).
* To do this, we wanted to put every occupation on one number line, with each occupation occupying a
section of the number line. The size of that section corresponds to the probability of
that section being picked.
* We accomplished this by iterating through our
dictionary and modifying the values to be the sum of all the values we had previously
iterated through.