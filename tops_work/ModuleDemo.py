import udf

while True:

    print("*"*50)
    sname=input("Enter Your Name : ")
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Pattern")
    print("7. Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice : "))
    print("*"*50)

    if choice==1:
        a=int(input("Enter Value : "))
        udf.OddEven(a)
        print("You Opted OddEven Function")
        print("*"*50)

    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        udf.MaxOfTwo(a,b)
        print("*"*50)

    elif choice==3:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        udf.MaxOfThree(a,b,c)
        print("*"*50)

    elif choice==4:
        a=int(input("Enter Value : "))
        udf.Fibonacci(a)
        print("*"*50)

    elif choice==5:
        a=int(input("Enter Value : "))
        udf.Prime(a)
        print("*"*50)

    elif choice==6:
        a=int(input("Enter Value : "))
        udf.Pattern(a)
        print("*"*50)

    else:
        print("Thank You. Good By")
        break
    
