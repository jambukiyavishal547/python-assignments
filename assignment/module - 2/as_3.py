#Fibonacci series 

a,b=0,1
n=int(input("Enter Last Value: "))
print(a,end=" ")
while b<=n:
    print(b,end=" ")
    a,b=b,a+b
    
