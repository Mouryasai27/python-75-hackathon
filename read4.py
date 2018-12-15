#reading only the particular lines that are needed in a file

file = open("testing5.txt","r")
lines = file.readlines()

print(lines[5])
print(lines[6])

file.close()

#it will print the lines 5 and 6 that are present in the file