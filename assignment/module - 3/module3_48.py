#Python function to calculate the factorial of a number (a nonnegative integer)
def factorial(n):
	
	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n - 1)

# Driver Code
num = int(input("Enter Intiger Number: "))
print("Factorial of",num,"is",factorial(num))
 