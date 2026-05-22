# Create function for following:

# 1. Write a Python function to find the maximum of three numbers.
def fun(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c
    
print(fun(10,15,25))



# 2. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def num(*numbers):
    new_list=[]

    for x in numbers:
        if x not in new_list:
            new_list.append(x)
    print(new_list)
num(1,2,5,7,2,9,5,7,9,4,2)    



# 3. Write a Python function to multiply all the numbers in a list.

def mul(*numbers):
    result = 1
    for x in numbers:
        result = result*x
    print("Multiplication of number is: ",result)
mul(2,3,4)   



# 4. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(n):
    result = 1

    for i in range(1,n+1):
        result = result * i

    return result

print(factorial(5))



# 5. Write a Python program to reverse a string.

def reverse_string(s):
    return s[::-1]
print(reverse_string("ranker"))



# 6. Write a Python function to check whether a number falls within a given range.

def check_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

print(check_range(5, 1, 10))


# 7. Write a Python function to Print Even Numbers from a Given List
def print_even(numbers):
    for x in numbers:
        if x % 2 == 0:
            print(x)

print_even([1, 2, 3, 4, 5, 6, 7, 8])



# 8. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(7))


# 9. Write a Python function that accepts a string and counts the number of upper and lower case letters. 
def count_case(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_case("Hello World")