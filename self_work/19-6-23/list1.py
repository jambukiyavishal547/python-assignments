l=[]
st=100
end=301

for i in range(st,end):
    if i%5!=0 and i%7==0:
        l.append(i)
print(l)
