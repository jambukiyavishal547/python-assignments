#Python program to write a list to a file
l=["a","b","c","d","e"]
file=open("demo2.txt","w")
for i in l:
    file.write(i+"\n")
    print(i)
file.close()