import random
computer_guess = random.randint(1,100)

status = True

while status :
    user_choice = int(input("enter your choice : "))
    if user_choice > computer_guess:
        print("hint : Guess lower number")
    elif user_choice < computer_guess:
        print("hint : guess higher number :")
    else: 
        print("right guess")
        status = False