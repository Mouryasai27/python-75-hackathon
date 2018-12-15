

class Atm():
    def __init__(self,name,accno,pin,amount):
        self.name = name
        self.accno = accno
        self.pin = pin
        self.amount = amount

name = input("Enter the name of account: ")        
accno = int(input("Enter the account number: "))
pin = int(input("Enter the pin number: "))
amount = int(input("Enter the amount: "))

obj = Atm(name,accno,pin,amount)


#this program takes the input from user