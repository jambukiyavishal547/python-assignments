n=int(input("enter row: "))
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(i+1,end=" ")
    print()
        
    
    
