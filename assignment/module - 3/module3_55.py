#set the starting value in generating random numbers
'''The random number generator needs a number to start with (a seed value),
# to be able to generate a random number. By default the random number generator uses the current system time.
# Use the seed() method to customize the start number of the random number generator.'''
import random

random.seed(9)
print(random.random())

random.seed(10)
print(random.random())