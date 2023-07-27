import fm_manage

Generator = {}
# status for menu repeatation 
status = True

# printing the welcome note
print("\n\t\tWelcome To python E-note\n\n")

while status:
    # printing menu for choosing our choice from the module
    x=fm_manage.menu()
    print(x)
     # creating an empty dictionary specification for fruit quantity and price
    specification = {}
    # getting input from the user for choice from the menu
    choice = int(input("Enter your choice : "))
    
    # choice 1 add
    if choice == 1:
        
        # taking Generator name,quantity and price from user 
        Generator_name = input("Enter python E-note Generator Name : ")
        Title = input("Enter Python E-Note Title : ")
        Contect= input("Enter Python E-Note Content : ")

        Generator[Generator_name] = specification

     # choice 2 view
    elif choice == 2:
        
        # using for loop to view
        for k in Generator.keys():
            print("-----------------------------------")
            print(f"generator name : {k} ")
            print(f"title :  ,{k}")
            print(f"contect :  ,{k}")
    
     # choice 3 for exit
    elif choice == 3:
        
        status = False
        break
    
        # for asking the user if they want to perform more operation

    user_choice = input("do you want to continue press 'y' for yes and press 'n' for no : ")
    if user_choice == 'n':
        status= False
    else:
        status = True