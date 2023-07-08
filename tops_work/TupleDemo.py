t=(1,2,10,1.1,"tops",[10,20,30],True,"python",1,2,100)

print(t)
print(t.count(10))
print(t.index(100))

for i in t:
    print(i)

print(1.2 in t)
print(t[5])
t[5].append(40)
print(t[5])
t.append(1000)
