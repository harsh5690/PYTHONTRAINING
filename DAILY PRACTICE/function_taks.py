"""function categories :

1) function without parameters and function without retrun types
2) function with parameters and function without retrun types
3) function without parameters and function with retrun types
4) function with parameters and function with retrun types
                

              menu
              1) prees 1 for addition
              2) press 2 for multiplication
              3) press 3 for find factorial value
              4) press 4 for fibbonacci series
              5) press 5 for prime number
"""

   # function with parameter :
menu= """menu
               1) prees 1 for addition
               2) press 2 for multiplication
               3) press 3 for find factorial value
               4) press 4 for fibbonacci series
               5) press 5 for prime number
   """
def addition():
    print(menu)
    choice = int(input("select your role:"))
    if choice == 1:
         num1 = int(input("enter the number 1 :"))
         num2 = int(input("enter the number 2 :"))
         ans = num1 + num2
         print(ans)
      
    elif choice == 2:
         ans2 = num1 * num2
         print(ans2)

    elif choice == 3:
       num3 = int (input("enter a number : "))
       factorial = 1
       for i in range(1,num3 + 1):
            factorial = factorial * i   
       print("The factorial of", num3,"is",factorial)   
    
    elif choice ==4:
        n=int(input("enter the number"))
        x= 0
        y= 1
        z = 0 
        while z<=n:
         print(z)
         x= y
         y= z
         z = x+y
        
            
addition()
