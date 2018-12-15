
#Printing details of a person using class and objects

class Details:
    def __init__(self,name,age,college,dept):
        self.name = name
        self.age = age
        self.college = college
        self.dept = dept
    def info(self):
        print("Name of a person is: " + self.name)
        print("Age of a person is: " + self.age)
        print("College person belongs to : " + self.college)
        print("Department person belongs to: " + self.dept)
        
obj = Details("sai charan","21","sathyabama","cse")
obj.info()

#it prints the details of the person metioned


        

