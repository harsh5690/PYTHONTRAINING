class cale: # creating classs of cale
    def addition(self,num1,num2):
        self.n1 = num1
        self.n2 = num2

    def display(self):
        self.ans = self.n1 + self.n2
        print("ans = ",self.ans)

obj = cale() # object creation
n1 = int(input("enter number 1: "))
n2 = int(input("enter number 2: "))
obj.addition(n1,n2)
obj.display()