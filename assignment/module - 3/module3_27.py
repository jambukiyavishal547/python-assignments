# Python program to find the repeated items of a tuple.
t=(1,2,3,4,5,6,1,2,3)
l1=[]
l2=[]
for i in t :
    if t.count(i) > 1:
        l1.append(i)
    for i in l1:
        if i not in l2:
            l2.append(i)
print(l2)
    
