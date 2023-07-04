"""class a : # parent class
    def display(self):
        print("a class here")

class b(a):
    def displayb(self):
        print("b class here ")

obj = b()
obj.display()
obj.displayb()"""

"""class A:
    def inputA(self):
        self.n1 = int(input("enter number 1 :"))
        self.n2 = int(input("enter number 2 :"))
    def displayA(self):
        ans = self.n1 + self.n2
        return ans
class B:
    def inputB(self): 
        self.n3 = int(input("enter number 3 :"))
        self.n4 = int(input("enter number 4 :"))
    def displayB(self):
        ans = self.n3 * self.n4
        return ans
class C(A,B):
    def displayC(self):
        print("welcome to cale world")

obj = C()
obj.displayC()

obj.inputA()
obj.inputB()
print("addition =",obj.displayA())
print("multiplication = ",obj.displayB())
"""

class a : # parent class
    def display(self):
        print("a class here")

class b(a):
    def displayb(self):
        print("b class here ")

class c(b):
    def displayb(self):
        print("b class here ")

obj = c()
obj.displayc()
obj.inputA()
obj.inputB()