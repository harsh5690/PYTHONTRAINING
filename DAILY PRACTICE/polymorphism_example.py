"""
->poly means many and morphism means forms

->polymorphism which is deived from greek word

->one name mathod has different different forms 

*>there are 2 type pf polymorphism:

  1)method overloading 
  2)method overriding

=> method overloading :
one class same name mathood but different forms its called method overloading 

=> method overriding :

parent and child both have same name method its called method overriding 

"""
"""
1)method overloading 
class student:
    def display(self):
        print("this is default display method")

    def display(self,num1):
        print("num1 =",num1)
    
obj = student()
obj.display(10)
obj.display()
"""
# 2)method overriding

class A: 
    def display(self):
        print("A class")
class B:
    def display(self):
        A.display(self)
        print("B class")
obj = B()
obj.display()