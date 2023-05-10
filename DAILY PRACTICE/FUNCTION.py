"""
function: function is a block of code - piece of code
 function which is provide reusabilities ans using of function we can call same many time and reduce our code
 
 there are 2 types of function
 
 1)built-in function : which is predefine by python
 
   e,g.. print(),len(),range(),random()
    ,append(), .extend() this is methods
    
    
 2) user definr function : which id define BY user
 
hoow we can create function :

using of def keyword we can create function

syntax:

def funname():
  black of code 
  
  caling:
  funname()
 """
 # create new function 

"""def mygreeting():
    print("welcome to python")
    print("good morining ")
mygreeting()"""

def mysun():
     n1= int(input("enter number1:"))
     n2= int(input("enter number2:"))
     ans= n1+n2
     print(ans)
for i in range(1,4):
    mysun()