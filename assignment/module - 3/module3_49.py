#a Python function to check whether a number is in a given range
def n_range(n):
    #check n Is in range or not
    if n in range(1,101):
        print(n," Is in range")
    else :
        print(n,"Is not in range")
n=int(input("Enter Integer Number: "))
n_range(n)