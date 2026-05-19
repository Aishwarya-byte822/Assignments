# 2) Input 2 strings concatinate them and store in another variable. then perform generally used string methods on it like
# lower(), upper(), title(), swapcase(), capitalize(), casefold(), center(), count(), endswith(), find(), isalnum(), isdigit(), isnumeric(), isspace(), replace()

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s3=s1+" "+s2
print("Concatenated String: ",s3)
print("Lowercase: ",s3.lower())
print("Uppercase: ",s3.upper())
print("Title: ",s3.title())
print("Swapcase: ",s3.swapcase())
print("Capitalize: ",s3.capitalize())
print("Casefold: ",s3.casefold())
print("Center: ",s3.center(60))
print("Count of a: ",s3.count('a'))
print("Endswith 'a': ",s3.endswith('a'))
print("Find 'a': ",s3.find('a'))
print("Is Alphanumeric: ",s3.isalnum()) 
print("Is Digit: ",s3.isdigit()) 
print("Is Numeric: ",s3.isnumeric()) 
print("Is Space: ",s3.isspace()) 
print("Replace 'a' with 'x': ",s3.replace('a','x'))







