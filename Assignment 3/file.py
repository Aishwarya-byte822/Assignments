# > Practise reading, writing , appending data in a file

# Writing to a file
file = open('name.txt','w')
file.write("This is the first comment in this file.\n")
file.write("It is an easy method to write data in a file.\n")
file.close()

# Reading from a file
file = open('name.txt','r')
for each in file:
    print(each)

# Open the whole file and read everything at once.
file = open('name.txt','r')
print(file.read())

# use of with
with open('name.txt','r') as file:
    data=print(file.read())
print(data)    

# 
file = open("name.txt", "r") 
print (file.read(6)) 

# 
with open('name.txt','r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

#
with open("name.txt", "w") as f:
    f.write("Hello World!!!")

#  appendinmg to a file
file = open('name.txt','a')
file.write("\nLet's add this")
file.close()
