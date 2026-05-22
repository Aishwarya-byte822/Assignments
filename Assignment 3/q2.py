# 2) Write a function for basic math operations like add multiply substract divide and use this in your program, take 2 number input from user.

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

def add(a,b):
    return a+b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("Addition of numbers:",add(n1,n2)) 
print("Subtraction:", subtract(n1, n2))
print("Multiplication:", multiply(n1, n2))
print("Division:", divide(n1, n2))   