# tkinter : inbuilt python module which is used to create GUI application
from tkinter import *

sc = Tk() #screen tkinter store
sc.geometry("1000x600") # w x h
sc.title("my app")

lbl_var = StringVar()

def mychoice(msg):
    lbl_var.set(msg)

btn1 = Button(sc,text="ROCK",font=('arial',26,'bold'),activebackground="blue",activeforeground="white",command=lambda :mychoice("ROCK"))
btn1.place(x=10 , y=10)

btn2 = Button(sc,text="PAPER",font=('arial',26,'bold'),activebackground="red",activeforeground="white",command=lambda :mychoice("PAPER"))
btn2.place(x=150 , y=10)

btn3 = Button(sc,text="SCISSOR",font=('arial',26,'bold'),activebackground="yellow",activeforeground="white",command=lambda :mychoice("SCISSOR"))
btn3.place(x=305 , y=10)

lb1 = Label(sc,textvariable=lbl_var,font=('arial',26,'bold'))
lb1.place(x=10,y=120)


sc.mainloop()