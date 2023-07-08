import random

#l=[10,20,"tops",True,1.1,"python",False,1]
#print(random.choice(l))


l=[]
lucky=[]

for i in range(1,101):
    l.append(i)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)

print(l)
print(lucky)
