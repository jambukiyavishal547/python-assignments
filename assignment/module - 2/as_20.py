#Write a Python function that takes a list of words and returns the length 
#of the longest one.


i = input("Enter three String: ")
a = i.split()
b = max(a, key = len)
print("Longest word: ",b)
print("lenth of word: ",len(b))
