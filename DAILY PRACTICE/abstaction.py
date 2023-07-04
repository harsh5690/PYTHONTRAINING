"""
abstrcaion which is only achive by abstract class.
abstract class which is contain abstract method.
abstract method means which is declare only function declaration.
without function body its called abstract method. 

"""
"""
                                vehicle
                                    |  
                                    |                           
            __________________________________________________
            |                       |                        |
            |                       |                        |
            bike                    car                    truck
            
            """

#exmple:-

"""from abc import ABC # ABC : abstarct base class

class vehicle(ABC): # abstract class(bacoause it contain abstarct method : without body) 
    def speed(self):
        pass
    def wheels(self):
        pass
    def color(self):
        pass

class bike(vehicle):
    def wheels(self):
        print("i have 2 wheels0")
    def color(self):
        print("black color")
    def speed(self):
        print("70kmp")

obj = bike()
obj.color()
obj.speed()
obj.wheels()    """

#exmple_2:-

from abc import ABC # ABC : abstarct base class

class RBI(ABC): # abstract class(bacoause it contain abstarct method : without body) 
    def SBI(self):
        pass
    def HDFC(self):
        pass
    def BOI(self):
        pass

class ROI(RBI):
    def SBI(self):
        print("SBI ROI: 5%")
    def HDFC(self):
        print("HDFC ROI :6%")
    def BOI(self):
        print("BOT ROI :7%")

obj = ROI()
obj.SBI()
obj.HDFC()
obj.BOI()    