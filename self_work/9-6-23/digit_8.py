n=int(input("enter number for pattern: "))
for i in range(n-1,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print(j+1,end=" ")
    print()
