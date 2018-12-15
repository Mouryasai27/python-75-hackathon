
#filter operation in lambda 

#filter function filters the elements in the list as per the given condition

list1 = [1,2,3,4,5,6,7,8,9,10]

new_list1 = list(filter(lambda x : (x%2!=0),list1))
print(new_list1)

#the above function prints the odd numbers in the list

new_list2 = list(filter(lambda x: (x%2==0),list1))
print(new_list2)

#the above code prints all the even numbers in the list

#if we dont filter function we get the error "(<function <lambda> at 0x0000025C4ADC5268>, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])"
