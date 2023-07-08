file=open("tops1.txt","w")
file.write("This is file management demo using python.")
file.close()
print("File Writen Successfully")

print("*"*50)

file=open("tops1.txt","r")
print(file.read())
file.close()

print("*"*50)

file=open("tops1.txt","a")
file.write("\nNow This File Is Appended.")
file.close()
print("File Appended Successfully")

print("*"*50)

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*"*50)

file=open("tops2.txt","w+")
file.write("This is w+ operation in file management using python.")
#print("Cursor Position : ",file.tell())
file.seek(10)
print(file.read())
file.close()








