#a Python program to append text to a file and display the text
file=open("demo.txt","w")
file.write("This is file management demo using python.\n")
file.write("this is second line")
file.close()
file=open("demo.txt","r")
print(file.read())
file.close()