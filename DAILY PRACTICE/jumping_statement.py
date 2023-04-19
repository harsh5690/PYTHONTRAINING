"jumping statement"
"""
break : to break the loop - will terminate the loop
continue : to skip current statement - it will continue the loop
"""
# accept 5 subject matrks froma user 
# break example
"""
for i in range(1,6):
    marks = int (input("enter the marks : "))
    if marks>35:
         print("pass")
    else:
         print("fail")
         break
         """
#continue example

for i in range(1,6):
    marks = int (input("enter the marks : "))
    if marks>35:
         print("pass")
    else:
         print("fail")
         continue