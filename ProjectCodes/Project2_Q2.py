str1 = input('Enter first number: ')
str2 = input('Enter second number: ')

val1 = 0
val2 = 0

if len(str1) > 0:
    for char in str1:
        val1 += ord(char)
if len(str2) > 0:
    for char in str2:
        val2 += ord(char)
if val1 > val2:
    print(f"{str1} is bigger than {str2}")
elif val1 < val2:
    print(f"{str1} is smaller than {str2}")
elif val1 == val2:
    print("Both inputs are equal")