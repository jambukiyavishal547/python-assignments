#Python script to check if a given key already exists in a dictionary
d={ 10:'vishal', 11:'bhargav'}
print(d)
a=int(input("Enter Any Above key: "))
if d.get(a):
    print(a," is exists in dictionary")
else:
    print(a, "is not exists in dictionary")

