#Python script to sort (ascending and descending) a dictionary by value. 
d={'c':3,'a':1,'b':2}
#print(d)
d1=sorted([(key,value)for (key,value) in d.items()])
print("Ascending: ",d1)
print("Descending: ",d1[::-1])
