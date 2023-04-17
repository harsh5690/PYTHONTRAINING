"""if condition :
    if condition:
        statement
    else;
        statement
else:
    if condition:
        statement
        """

marks = int(input("enter marks :"))
if marks >=0 and marks <= 100:
    if marks >= 70:
        print("A grade")
    elif marks>=60 and marks<70:
        print("B grade")
    elif marks>=50 and marks<60:
        print("B grade")
    elif marks>=40 and marks<50:
        print("B grade")
    else:
        print("fail")
else: 
    print("invaild input")