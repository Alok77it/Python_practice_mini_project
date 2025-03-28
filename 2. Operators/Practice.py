# Declare your age as an integer variable
age = int(22)

# Declare your height as a float variable
age = float(5.8)

# Declare a variable that stores a complex number
complex_number = 3 + 4j

# Write a script that prompts the user to enter base and height of the triangle 
base = int(input("Enter base: "))
height = int(input("Enter height: "))

# and calculate the area of this triangle (area = 0.5 * b * h).
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle.
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))

# Calculate the perimeter of the triangle (perimeter = a + b + c).
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}") 

# Get the length and width of a rectangle using input prompts.
length = int(input("Enter length: "))
width = int(input("Enter width: "))

# Calculate its area (area = length * width) and perimeter (perimeter = 2 * (length + width)).
area = length * width
print(f"The area of the rectangle is {area}")

# Get the radius of a circle using input prompt.
radius = int(input("Enter radius: "))

# Calculate the area (area = pi * r * r) and circumference (c = 2 * pi * r) where pi = 3.14.
area = 3.14 * radius * radius

# Calculate the slope, x-intercept, and y-intercept of the equation y = 2x - 2.
x_intercept = int(input("Enter x-intercept: "))
slope = 2
y = 2 * x_intercept - slope
print(f"The y-intercept is {y}")

# Using the slope formula (m = (y2 - y1) / (x2 - x1)), 
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
slope = ((y2 - y1) / (x2 - x1))
print(f"The slope is {slope}")

# find the slope and Euclidean distance between points (2,2) and (6,10).
import math
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = ((y2 - y1) / (x2 - x1))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The slope is {slope} and the distance is {distance}")

# Calculate the value of y using the equation y = x^2 + 6x + 9.
x = int(input("Enter x: "))
y = x ** 2 + 6 * x + 9
print(f"The value of y is {y}")

# Find the length of the words 'python' and 'dragon' and make a falsy comparison statement.
length_python = len("python")
length_dragon = len("dragon")
print(f"Length of 'python': {length_python}, Length of 'dragon': {length_dragon}")
falsy_comparison = length_python > length_dragon
print(f"Fasly comparison: {falsy_comparison}")

# Use the 'and' operator to check if 'on' is found in both 'python' and 'dragon'.
if 'on' in 'python' and 'on' in 'dragon':
    print("Found 'on' in both 'python' and 'dragon'")

# Check if the word "jargon" is in the sentence: "I hope this course is not full of jargon."
sentence = "I hope this course is not full of jargon."
if "jargon" in sentence:
    print("Found 'jargon' in the sentence")
else:
    print("Did not find 'jargon' in the sentence")  


# Find the length of the text 'python', convert it to a float, and then convert it to a string.
length_python = len("python")
float_length = float(length_python)
string_length = str(float_length)
print(f"Length of 'python' as float: {float_length}, Length as string: {string_length}")

# Even numbers are divisible by 2 with a remainder of zero.
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")

# Write a Python statement to check if a number is even.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

# Check if the floor division of 7 by 3 is equal to the integer-converted value of 2.7.
a = 7 // 3
b = int(2.7)
if a == b:
    print("Floor division of 7 by 3 is equal to the integer-converted value of 2.7")
else:
    print("Floor division of 7 by 3 is not equal to the integer-converted value of 2.7")

# Check if the type of '10' is equal to the type of 10.
a = '10'
b = 10
if type(a) == type(b):
    print("'10' is of the same type as 10")
else:
    print("'10' is not of the same type as 10")

# Check if int('9.8') is equal to 10.
x = '9.8'
try:
    a = int(x)
    b = 10
    if a == b:
        print("int('9.8') is equal to 10")
    else:
        print("int('9.8') is not equal to 10")
except ValueError:
    print("Error: Cannot convert '9.8' to an integer")

# Write a script that prompts the user to enter hours and rate per hour.
# Calculate the weekly pay of the person.
# Example:
#     Enter hours: 40
#     Enter rate per hour: 28
#     Your weekly earning is 1120.
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
weekly_earning = hours * rate
print(f"Your weekly earning is {weekly_earning}")


# Write a script that prompts the user to enter the number of years they have lived.
# Calculate the number of seconds they have lived, assuming a person can live up to 100 years.
# Example:
#     Enter number of years you have lived: 100
#     You have lived for 3153600000 seconds.
years = int(input("Enter number of years you have lived: "))
seconds = years * 31536000
print(f"You have lived for {seconds} seconds")

# Write a Python script that displays the following table:
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1, 6):
    print(f"{i} {i} {i**1} {i**2} {i**3}")