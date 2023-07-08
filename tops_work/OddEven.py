import random

#print(random.randint(1000,9999))
file=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    file.write(str(num)+",")
file.close()

file=open("data.txt","r")
odd=open("odd.txt","w")
even=open("even.txt","w")
prime=open("prime.txt","w")

l=file.read().split(",")[:-1]
print(l)
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
    if int(i)%2!=0:
        for j in range(3,int(int(i)/2)+1,2):
            if int(i)%j==0:
                break
        else:
            prime.write(i+",")
            
even.close()
odd.close()
file.close()
prime.close()

print("Data File Content")
data=open("data.txt","r")
print(data.read())
data.close()

print("Even File Content")
even=open("even.txt","r")
print(even.read())
even.close()

print("Odd File Content")
odd=open("odd.txt","r")
print(odd.read())
odd.close()

print("Prime File Content")
prime=open("prime.txt","r")
print(prime.read())
prime.close()

