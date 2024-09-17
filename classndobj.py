
""""class School:
    def __init__(self,moment) -> None:
        print("Moment is {}".format(moment))
        print(type(moment))
        self.mom=moment

    def display(self):
        print(f"the exact moment is {self.mom}")

schl=School("25")
schl.display()

class A:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b

    def display(self):
        print(f"A is {self.a}")
        print(f"B is {self.b}")

    def printf(self):
        c=0
        x=int(input("enter the element"))
        for i in range(x):
            c=self.a * self.b
        print(c)

w=A(3,5)
w.display()
w.printf()"""
'''

class Aa():
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def display(self):
        print(f"my name is {self.name} and my age is {self.age}")


    def wordin(self):
        print("AAAAAAA")

class Bb(Aa):
    def __init__(self, name, age,color) -> None:
        super().__init__(name, age)
        self.color=color

    def wordin(self):
        print("BBBBB")
a=Aa("srikanth",21)
a.display()
a.wordin()
b=Bb("guru",50,"blue")
b.display()
b.wordin()'''
'''
class A():
    def __init__(self,name) -> None:
        self.name=name
    def display(self):
        print(f"my name is {self.name}")

class B(A):
    def __init__(self, name,age) -> None:
        super().__init__(name)
        self.age=age

    def display(self):
        print(f"age is {self.age} years")

class C(B):
    def __init__(self, name, age,color) -> None:
        super().__init__(name, age)
        self.color=color

    def display(self):
        print(f"my color is {self.color} and my age is {self.age}")
    
a=A("srikanth")
a.display()
b=B("guru",50)
b.display()
c=C("ram",20,"blue")
c.display()'''

class P():
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        self.coo=(self.x,self.y)
    def display(self):
        print(f"coordinate is {self.coo}")
    
    def __add__(self,p):
        return P(self.x+p.x,self.y+p.y)
    






p1=P(12,25)
p2=P(8,5)
p3=p1+p2
p3.display()