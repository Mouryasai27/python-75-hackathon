
#Factorial of a Number using Functions
def Factorial(n): 
    if n == 1:
        return n
    else:
        return n*Factorial(n-1)
num = int(input("enter the number:"))
print(Factorial(num))
