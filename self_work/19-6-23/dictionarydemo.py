d={231:"vishal",765:"Bhargav",908:"rinkal",564:"krina",434:"krishna"}

print(d)
print(d[765])
#not valid print(d["krina"])
print(d.get(908))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(564))
print(d)
print(d.popitem())
d1={101:"krina",102:"krishna",103:"anchal",104:"sohan"}
d.update(d1)
print(d)



for i in d:
    print(i," : ",d[i])
