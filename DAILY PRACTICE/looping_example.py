"""
looping example :

there are 2 types of loop
1) for loop : for loop = sequence control loop
2) while loop : while loop : enter controll loop
  -> condition check at enter level
  if condition goes true loop will execute
"""
"""
for i in range(5): # by defuilt loop start fromm 0 to 4
    print(i)
""" 
"""
for i in range(1,6): # by defuilt loop start fromm 1 to 5
    print(i) 
"""
"""
for i in range(1,6):
    num = int(input("enter number :"))
"""
"""
sum=0
for i in range(1,6):
    num = int(input("enter number :"))
    sum += num
print("ans =",sum)
"""

# while loop :
"""
 syntax :
 intialization
 while condition :
   satement
  updation 

  """
status = True
while status:
    num = int(input("enter number :"))
    choice = int(input("do you want to continue 1 for yes and press 2 for exit :"))
    if choice == 1:
        status = True
    else:
       status = False
    
    
