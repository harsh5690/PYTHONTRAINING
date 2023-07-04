"""

            A
            |
            B
----------------------
            A
            |
            B
            |
            C
---------------------
        A       B
        |       |
        ---------
            |
            C
---------------------
            A
            |
        ---------
        |       |
        B       C
"""

class A:
    num1 = 10
class B:
    num2 = 15

class C(A,B):
    def display(self):
        self.ans = A.num1 + B.num2
        return self.ans
    
obj = C()
print(obj.display())