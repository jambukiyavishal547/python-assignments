# Python function that checks whether a passed string is palindrome or not
st=input("Enter String: ")
s = ""
for i in st:
	s = i + s

if (st == s):
	print("Yes")
else:
	print("No")
