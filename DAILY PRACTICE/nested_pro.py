"""
 nested if statement 
"""
CSK = int(input("enetr csk score :"))
DC = int(input("enetr DC score :"))
GT = int(input("enetr GT score :"))
if DC > GT :
    if DC > CSK:
        print("DC won the match")
    else:
        print("CSK won the match ")
else:
    if GT > CSK:
        print("GT won the match ")
    else:
        print("CSK won the match ")