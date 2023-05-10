#function with parameter and with return types

def checkevenodd(number):
    if number % 2 == 0:
       return "even number"
    else:
        return "odd number"

num = int(input("enter your number : "))
print(checkevenodd(num))