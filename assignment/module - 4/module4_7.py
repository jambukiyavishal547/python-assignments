#Python program to read a file line by line store it into a variable.

tmp=open("demo.txt","r")
file=tmp.read()
print(file)
tmp.close()
