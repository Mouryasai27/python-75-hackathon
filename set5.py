
#Operations on sets

set_1 = {1,2,3,4,5}

set_2 = {3,5,6,7,8}

print(set_1 | set_2)        #this will perform the Union operation which combines all values present in two sets
print(set_1.union(set_2))


print(set_1 & set_2)
print(set_1.intersection(set_2))

#the above two print statements perform the intersection operation and prints the common values present in two sets
#if there are no common values present in two sets then it will print 'set()'

print(set_1 - set_2)
print(set_1.difference(set_2))

#the above code performs the set difference that means prints the values present which are not present in other set

