#Swap two numbers without using a third variable.

a = input("Enter first numbers to swap: ")
b = input("Enter second numbers to swap: ")

a, b = b, a

print("After swapping a is", a, "and b is", b)

#Check if a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:

    print("The number is even")
else:
    print("The number is odd")

#Reverse a string without using slicing.

string = input("Enter a string: ")

reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print("The reversed string is:", reversed_string)

#Convert Celsius to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

#Find the largest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: ")) 
if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c
print("The largest number is:", largest)

