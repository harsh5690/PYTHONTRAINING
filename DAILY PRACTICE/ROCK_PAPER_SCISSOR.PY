import random
menu = """
                    menu

                    chose your choice
                        
                        Rock 
                        Paper 
                        Scissor


"""


game_list = ["Rock","Paper"," Scissor"]
computer = random.choice(game_list)

status = True
while status:
    print(menu)
    user_choice = input ("enter your choice :").upper()

    print("COMPUTER CHOICE :",computer)
    if user_choice == computer: 
        print("TIE")
    elif user_choice == "Rock" and computer == "Paper":
        print("computer won")
    elif user_choice == "Rock" and computer == "Scissor":
        print("user won")

    elif user_choice == "paper" and computer == "rock":
        print("user won")
    elif user_choice == "paper" and computer == "Scissor":
        print("computer won")


    elif user_choice == "scissorr" and computer == "rock":
        print("computer won")
    elif user_choice == "scissorr" and computer == "paper":
        print("user won")

    exit_choice = input(" do you want to play again? press y for yes and press n for no : ")

    if exit_choice == 'y' or exit_choice == 'y':
        status = True
    else:
        status = False
