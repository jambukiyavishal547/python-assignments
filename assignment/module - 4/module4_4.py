# Python program to read first n lines of a file
from itertools import islice
file=open("demo.txt","r")
n=2
for i in islice(file,n):
    print(i)
file.close()
