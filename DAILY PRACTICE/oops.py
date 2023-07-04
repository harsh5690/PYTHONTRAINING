"""
oops  : object oriented programming syastem 

class : class is a collection of data member and member function 
        or
        class which is contain data member and mem+ber function is single entity
        or
        class is like group which is store different data member in it 



object : object is an instance of class
        if class is a data then object is an isinstance or varible of class
        using of object we can access all the properties of class
                
one class can have mamny objects

"""
#example
"""
class student :
    def display(self):
        print("this is student class ")

odj = student()
odj.display()

#self : here , self is a keyword which is represent current class properties


"""
"""
class program :
    def checkevenodd(self,number):
        if number % 2 == 0:
            print("even")
        else :
            print("odd")
obj = program()
obj.checkevenodd(10)
"""

class program:
        def input(self,firstname,lastname):   
            self.fname = firstname
            self.lname = lastname

        def display (self):
            print("\n firstname = ", self.fname)
            print("\n lastname = ",self.lname)

obj = program()
obj.input("anjali","patel")
obj.display()
