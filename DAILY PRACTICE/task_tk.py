# tkinter : inbuilt python module which is used to create GUI application
from tkinter import *

sc = Tk() #screen tkinter store
sc.geometry("1000x600") # w x h
sc.title("my app")

def Sum(number):
    total = sum(number)
    return total




btn1 = Button(sc,text="+",font=('arial',26,'bold'),activebackground="blue",activeforeground="white",command=lambda :Sum("Sum"))
btn1.place(x=10 , y=10)

btn2 = Button(sc,text="-",font=('arial',26,'bold'),activebackground="red",activeforeground="white",command=lambda :DIS("Dis"))
btn2.place(x=150 , y=10)

lb1 = Label(sc,textvariable=,font=(count_var'arial',26,'bold'))
lb1.place(x=10,y=120)


sc.mainloop()