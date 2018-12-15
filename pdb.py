
#python debugger 

import pdb
def sample(x,y):
    x = y * y
    y = y *x
    z = x + y
    return z
 
x = 5
y = 10
z = 15
n = 20

sample(5,10)
print('z = '+str(z))
pdb.set_trace()
print(n)

#the breakpoint is present at line 19 and executes accordingly
