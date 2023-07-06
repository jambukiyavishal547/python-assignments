#Python script to concatenate following dictionaries to create a new one
dic1={1:'vishal'}
dic2={2:'Bhargav'}
dic4 = {}
for d in (dic1, dic2): dic4.update(d)
print(dic4)
