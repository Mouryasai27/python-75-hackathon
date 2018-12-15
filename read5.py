
#same operation---reading the particular line in a file


lines = [5,6]
i = 0
file = open('testing5.txt')
for l in file:
    if i in lines:
        print(i)
    i += 1