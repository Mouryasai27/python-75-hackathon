
#Creating threads in python

import threading

def area_square(n):                 #function to find the square
    print("square: {}".format(n * n))
    
def power(n):                       #function to find the power
    print("power: {}".format(n ** n))
    
if __name__ == "__main__":          #used for creating the threads for two different functions
    t1 = threading.Thread(target = area_square,args=(2,))
    t2 = threading.Thread(target = power,args=(3,))
    
    t1.start()                      #start thread1 execution
    t2.start()
    t1.join()                       #complete thread1 execution
    t2.join()
    
    