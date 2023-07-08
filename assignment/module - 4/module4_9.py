#Python program to count the number of lines in a text file

file=open("demo.txt","r")
count=0
tmp=file.read()
div=tmp.split("\n")

for i in div:
    if i :
        count+=1
print(count)