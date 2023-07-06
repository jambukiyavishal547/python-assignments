#Python program to print all unique values in a dictionary

d={1:"vishal",2:"bhargav"},{3:"sohan",4:"sohan"}
d1={}
result=list(set(val for i in d for val in i.values()))
print(str(result))