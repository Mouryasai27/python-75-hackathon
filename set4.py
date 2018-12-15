
#deleting the values from the set

set = {1,2,3,4,5,6}
set.remove(4)
print(set)          #it will remove the value '4' from the set

set.discard(6)
print(set)
                #discard also performs the same function like remove
                
set_1 = {3,2,5,4}
set_1.remove(6)
print(set_1)        #this will produce the error named 'KeyError' as the element '6' is not present in the set                