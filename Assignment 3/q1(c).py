# sets
# 1 Create a set containing: 10, 20, 30, 40
s = {10, 20, 30, 40}
print(s)

# 2 Adding Elements to Set
# Given:
s = {1, 2, 3}
# Add:
# 4
# 5
s.add(4)
s.add(5)

print(s)

# 3 Add multiple elements: add 3,4,5
s = {1, 2} 
s.update([3,4,5])
print(s)

# 4 union operation
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))
print(s1 | s2)

# 5 Intersection operation
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.intersection(s2))
print(s1 & s2)

# 6 Difference Operation
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 - s2)
print(s2 - s1)

#  Symmetric Difference
print(s1 ^ s2)

# 7 Clearing Sets
s = {1, 2, 3}
s.clear()
print(s)


# 8 Membership Operators
# Check:
# Is 20 present?
# Is 50 absent?
print(20 in s)
print(50 not in s)


# 9 Equality Operators
s1 = {1, 2, 3}
s2 = {3, 2, 1}

print(s1 == s2)
print(s1 != s2)

# 10 Subset Operators
s1 = {1,2}
s2 = {1,2,3,4}
print(s1 <= s2)
print(s1 < s2) 

# 11 Superset Operators
s1 = {1,2,3,4}
s2 = {1,2}
print(s1 >= s2)
print(s1 > s2)

# 12 
# Find:
# A | B
# A & B
# A - B
# B - A
# A ^ B
A = {1,2,3,4}
B = {3,4,5,6}

print(A | B)
print(A & B)
print(A - B)
print(B - A)
print(A ^ B)
