#Python program to check multiple keys exists in a dictionary
d={ 10:'vishal', 11:'bhargav',12:"abc",13:"abcd"}
print(d.keys() >= {10,11})
print(d.keys() >= {10,15})
