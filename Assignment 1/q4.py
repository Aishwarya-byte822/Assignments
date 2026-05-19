# 5) In your last program where you find the total and percentage of a student's marks of 5 subject, find the grade of the student using conditional statement. Eg. grade 'A' if percentage is greator than or equals to 60, 'B' for  percentage is greator than or equals to 50 and less than 60,  'C' for  percentage is greator than or equals to 40 and less than 50,  'D' for  percentage is greator than or equals to 33 and less than 40, otherwise 'Fail'

n1 = input("Enter student name: ")
n2 = input("Enter student class: ")

m1=float(input("Enter marks 1: "))
m2=float(input("Enter marks 2: "))
m3=float(input("Enter marks 3: "))
m4=float(input("Enter marks 4: "))
m5=float(input("Enter marks 5: "))

total = m1+m2+m3+m4+m5

percentage = (total/500)*100

if(percentage>=60):
    print("Grade: A")
elif(percentage>=50 and percentage<60):
    print("Grade: B")
elif(percentage>=40 and percentage<50):
    print("Grade: C")
elif(percentage>=33 and percentage<40):
    print("Grade: D")
else:
    print("Grade: Fail")
