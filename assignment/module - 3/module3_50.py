#Python function to check whether a number is perfect or not
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
n=int(input("Enter Integer Number: "))
print(perfect_number(n))
