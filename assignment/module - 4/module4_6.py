#program to read a file line by line and store it into a list
l=[]
file=open("demo.txt","r")
for i in file:
    print(i)
    l.append(i)
print(l)
file.close()