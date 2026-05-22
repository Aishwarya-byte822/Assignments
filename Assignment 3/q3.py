#  Write a program to check Palindrome Number

#  For example Number 12321 is a Palindrome Number, because 12321 is equal to its reverse Number 12321.

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse number is:", reverse)

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")