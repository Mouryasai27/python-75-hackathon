#Inheritance concept in Python

class Person:
    def work(self):
        print("Different people have different names")
        
class Name(Person):
    def __init__(self):
        self.first = "Mourya"
        self.last = "sai"
    def show(self):
        print("Name of one person: ",end="")
        print(self.first,"",self.last)
        
class Name1(Person):
    def __init__(self):
        self.firstname = "charan"
        self.lastname = "Reddy"
    def show(self):
        print("Name of another person: ",end="")
        print(self.firstname,"",self.lastname)
        
n1 = Name()
n1.show()

n2 = Name1()
n2.show()