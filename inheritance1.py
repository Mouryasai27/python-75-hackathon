#Inheritance concept in Python

class Vehicle:
    def gen_usage(self):
        print("transportation")
        
class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.comfort = True
        
    def spc_usage(self):
        self.gen_usage()
        print("vacation")
        
class MotorCycle(Vehicle):
    def __init__(self):
        self.wheel = 2
        self.comfort = False
        
    def spc_usage(self):
        self.gen_usage()
        print("Racing")
        
c = Car()
c.spc_usage()

m = MotorCycle()
m.spc_usage()


