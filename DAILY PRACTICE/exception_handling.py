"""
exception : which disturb the normal flow of program to handle this kind of exception 
its called exception handling

-->exception handling is possible with try and except block 

"""

"""try:
    print(a)
except:
    print("something went worng")"""

"""num1 = int(input("enter the number 1 :"))
num2 = int(input("enter the number 2 :"))
try:
    ans= num1 / num2
    print(ans)

except:
     print("something went worng")"""

#example
"""
try:
    num1 = input("enter the number 1 :")
    num2 = int(input("enter the number 2 :"))
    ans= num1 / num2
    print(ans)
except ZeroDivisionError:
     print("cannot be divide by zero")
except ValueError:
     print("only numeric values requied ")
except:
     print("something went worng")"""

#example 2 
"""
try :
     print(a)
except Exception as e :
     print("exception message ",e)
"""

#example 3

"""import sys
try:
    print(a)
except:
    print(f"{sys.exc_info()[0]} - {sys.exc_info()[1]}")"""

#example 4 

class NegativeException(Exception):
    pass
try:
    num = int(input("enter number :" ))
    if num<0:
        raise NegativeException
    else:
        print("num = ",num)
except NegativeException:
    print("negative number entered ")