#Python program to read a random line from a file
# import required module
import random

# print random word
print(random.choice(open("test.txt","r").readline().split()))
