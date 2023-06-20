#string count char,digit,upper,lower,space
st=input("Enter string: ")

upper=0
lower=0
char=0
digit=0
space=0

for i in st:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    if i.isalpha():
        char+=1
    elif i.isnumeric():
        digit+=1
    elif i.isspace():
        space+=1
print("Total Upper: ",upper)
print("Total lower: ",lower)
print("Total char: ",char)
print("Total Digit: ",digit)
print("Total space: ",space)
