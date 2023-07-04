# Write a Python program to get the Fibonacci series of given range.

n=int(input("enter the number:"))
a = 1
b = 1
s = 0

for i in range(n):
    print(s,end=" ")
    s = a + b
    b = a
    a = s