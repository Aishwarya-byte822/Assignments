# 1) Write a python program that takes in a student name, class. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class,  and percentage are printed.

n1 = input("Enter student name: ")
n2 = input("Enter student class: ")

m1=float(input("Enter marks 1: "))
m2=float(input("Enter marks 2: "))
m3=float(input("Enter marks 3: "))
m4=float(input("Enter marks 4: "))
m5=float(input("Enter marks 5: "))

total = m1+m2+m3+m4+m5

percentage = (total/500)*100

print("Name: ",n1)
print("Class: ",n2)
print("Total Marks: ",total)
print("Percentage: ",percentage,"%")
