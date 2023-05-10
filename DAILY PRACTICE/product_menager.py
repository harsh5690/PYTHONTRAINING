#declare blank dictinory
stock = {}

# creating manu

menu = """
                  manu
            1) product mamger
            2) customer
            3) exit
"""

status  = True
while status :
    print(menu)
    choice = int(input("select your role:"))
    if choice == 1:
        product_manger_status = True
        while product_manger_status:
            spec= {} # sictionery for specification
            print("PRODUCT MEANGER")
            
            # accept product and product detalis from product manger
            product_name = input("enter product name:")
            product_qty = int(input("enter no. of product qty : "))
            product_price= int(input("enter product price:"))
            
            #creting nasetd dictonery first
            spec['qty']= product_qty               # "qty":5
            spec['price'] =product_price
            
            #creating outer dictionery
            stock[product_name] = spec             # {laptop : {"qty":5 , "price" : 4000}} 
            
            print(stock)

            manager_choice = input("do you want to add more product : ")
            if manager_choice == "y" or manager_choice == "n":
                product_manger_status = True
            else:
                product_manger_status = False
    elif choice ==2 :
        print("CUSTOMER")
    else:
        print("EXIT")
    
