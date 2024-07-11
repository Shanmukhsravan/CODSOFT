import random #importing Random module 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers= "0123456789"
symbols = "{}!@#$%&*_+"
all = lower+upper+numbers+symbols
length =10
print("\tRandom Password Generator\t")
n = int(input("Enter number of passwords u want?:"))
for i in range(n):
 password = " ".join(random.sample(all,length))
 print(password)
