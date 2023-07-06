#Write a Python function to insert a string in the middle of a string.
s=input("Enter 1 string: ")
st=input("Enter 2 string: ")
cen=len(s)//2
print(s[0:cen]+st+s[cen:])
