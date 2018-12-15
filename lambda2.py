
#Map function in lambda in Python

list1 = [1,2,4,8]

new_list = list(map(lambda x : (x ** 2),list1))

print(new_list)

#the output should return the list with square of values present
#output should be as '[1,4,16,64]'