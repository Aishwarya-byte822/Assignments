# 1) Practise dictionary,tuple and set
# dictionary

# Creating a dictionary for a student:
student = {"name": "Riya",
           "age": 20, 
           "course": "BTech"
           }
print(student)


# Accessing Nested Dictionary
students = {
    101: {"name": "Aman", "marks": 85},
    102: {"name": "Riya", "marks": 90},
}
print(students[102]["marks"])  
print(students[101]["name"])


# Adding Elements to Dictionary
student["city"] = "Delhi"
print(student)


# Add multiple keys using update:
student.update({"college": "SKIT", "year": 2})
print(student)


# Deleting Elements using del:
del student["year"]
print(student)


# clear() method
student.clear()
print(student)


# copy() method
student = {"name": "Aman", "age": 21}
new_student = student.copy()
print(new_student)


# items() method
student = {"name" : "Riya", "age":20}
for k, v in student.items():
    print(f"{k} = {v}")


# keys() method
print(student.keys())   


# values() method
print(student.values())


# update() method
d1 = {"a": 1, "b": 2}
d2 = {"c": 3}

d1.update(d2)
print(d1)


# pop(key) method
d = {"a": 10, "b": 20, "c": 30} 
d.pop("b")
print(d)


# popitem() method
d = {"a": 1, "b": 2, "c": 3}

d.popitem()
print(d)


# Merge Two Dictionaries(2 ways)
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print(d1)

d3 = d1|d2
print(d3)



# QUESTIONS
# 1
student = {
    "name": "Aman",
    "marks": 90,
    "subjects": {
        "math": 95,
         "science": 88
    }
}

print(student["subjects"]["science"])
student["city"] = "Jaipur"
print(student)
del student["marks"]
print(student)
student.keys()
print(student.keys()) 
new_student = student.copy()
print(new_student)    

# 2
'''Create a dictionary named student with:

name
age
course
marks

Then print:

entire dictionary
only marks'''

student ={"name": "Raj","age": 21,"course": "Btech","marks": 95}
print(student)
print(student["marks"])


# 3
'''Given:

student = {"name": "Aman", "age": 20, "course": "BTech"}

Add:

city = Jaipur
college = SKIT

Print final dictionary.'''
student = {"name": "Aman", "age": 20, "course": "BTech"}
student.update({"city":"Jaipur","college":"SKIT"})
print(student)

# 4
'''Given:

student = {"name": "Riya", "age": 21, "course": "BCA"}

Update:
age → 22
course → BTech'''

student = {"name": "Riya", "age": 21, "course": "BCA"}
student.update({"age": 22, "course": "B.TECH"})
print(student)


# 5
'''Given:

d = {"a": 10, "b": 20, "c": 30, "d": 40}

Do:

delete key "b" using del
remove key "c" using pop()
remove last item using popitem()

Print dictionary after each step.'''

d = {"a": 10, "b": 20, "c": 30, "d": 40}
del d["b"]
print(d)
d.pop("c")
print(d)
d.popitem()
print(d)









