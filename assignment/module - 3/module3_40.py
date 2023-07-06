# Python program to map two lists into a dictionary 
rno=[1,2,3]
name=[4,5,6]

result = map(lambda x, y: x + y, rno,name)
print(list(result))
'''
test=dict(zip(rno,name))
print(test)'''