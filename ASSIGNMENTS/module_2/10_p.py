#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 
x = int(input("enter the number : "))
y = int(input("enter the number : "))

sum = x + y
dis = x - y
if x == y or sum == 5 or dis == 5:
    print("True")
else:
    print("False")

print(sum)
print(dis)    