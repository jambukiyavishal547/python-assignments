# python program to find the longest words. 
file=open("demo.txt","r")
word=file.read().split()
long=len(max(word,key=len))
result=[text for text in word if len(text)==long]
print(result)
file.close()