def findfactorial(num):
    f = 1 #factorial initial value=1
    for i in range(1,num+1):
        f*=1
    print("factorial =",f)
    
#accept number from user

number = int(input("enter the number : "))
findfactorial(number)