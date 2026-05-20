# tuple

# 1
'''Create a tuple containing:

10, 20, 30, 40, 50
Print the tuple.'''
t = (10,20,30,40)
print(t)

# 2
'''Given:

t = (1, 2, 3, 4, 5)

Print each element using loop.'''

t = (1, 2, 3, 4, 5)
l = len(t)
for x in range(l):
    print(t[x])


# 3
'''Join two tuples:

t1 = (1, 2, 3)
t2 = (4, 5, 6)'''
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1+t2)


# 4
'''Create nested tuple:

t = (1, 2, (3, 4, 5))
print 4'''
t = (1, 2, (3, 4, 5))
print(t[2][1])


# 5
'''Repeat tuple 3 times:
t = (1, 2)'''
t = (1, 2)
print(t*3)


# 6
'''t = (10, 20, 30, 40, 50)
Print:
first 3 elements
last 2 elements'''

t = (10, 20, 30, 40, 50)
print(t[0:3])
print(t[-2:])

# 7
'''Delete entire tuple:'''

t = (1, 2, 3)
del t


# 8  Length of Tuple
t = (10, 20, 30, 40)
print(len(t))


# 9 
'''Create tuple with:

int
string
float
boolean'''

t = (10, "Python", 3.14, True)
print(t)


# 10 List to Tuple Conversion
lst = [1, 2, 3, 4]
t = tuple(lst)
print(t)


# 11 Tuple in Loop
# Print tuple elements with index:
t = (10, 20, 30)
for i in range(len(t)):
    print(i,t[i])


# 12 Tuple Methods
# count
t = (1, 2, 2, 3, 2)
print(t.count(2))

# index
t = (10, 20, 30, 20)
print(t.index(20))

# Built-in Functions
t = (5, 2, 9, 1)
print(min(t))
print(max(t))
print(sum(t))


# 13 

'''Do:

Slice middle 3 elements
Concatenate with (60, 70)
Repeat result 2 times
Find max and min'''

t = (10, 20, 30, 40, 50)
t1 = (60,70)
print(t[1:4])
print(t+t1)
print(t*2)
print(max(t))
print(min(t))







