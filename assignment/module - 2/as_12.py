# Sum Of First N Number Positive Number

n = int(input("Input an integer: "))
result = sum(range(1,n+1))
print("Sum of the first", n ,"positive integers:",result)
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)