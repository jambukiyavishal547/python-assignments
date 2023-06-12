n=int(input("enter row: "))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i,-1,-1):
        print(i+1,end=" ")
    print()
        
    
    
