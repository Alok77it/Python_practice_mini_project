<<<<<<< HEAD
# 📌 Pattern Practice Set (Using Loops)

# 📂 Part 1: Basic Star Patterns

# Q1: Print the following pattern (Right-Angled Triangle)
"""
*
**
***
****
*****
"""
# Write your code here

for i in range(1, 6):
    print("*" * i)

# Q2: Print the following pattern (Inverted Right-Angled Triangle)
"""
*****
****
***
**
*
"""
# Write your code here

for i in range(5, 0, -1):
    print("*" * i)

# Q3: Print the following pattern (Square)
"""
*****
*****
*****
*****
*****
"""
# Write your code here

for i in range(5):
    print("*" * 5)

# 📂 Part 2: Number Patterns

# Q4: Print the following pattern
"""
1
12
123
1234
12345
"""
# Write your code here

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 📂 Part 3: Alphabet Patterns

# Q5: Print the following pattern
"""
A
AB
ABC
ABCD
ABCDE
"""
# Write your code here

for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end="")
    print()

#65: The ASCII value of the letter 'A'.
#70: The ASCII value of the letter 'F'. 

# 📂 Part 4: Pyramid Patterns

# Q6: Print the following pattern (Pyramid)
"""
    *
   ***
  *****
 *******
*********
"""
# Write your code here

for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
    print()

# 📂 Part 5: Hollow Patterns

# Q7: Print the following pattern (Hollow Square)
"""
*****
*   *
*   *
*   *
*****
"""
# Write your code here

for i in range(5):
    if i == 0 or i == 4:
        print("*" * 5)
    else:
        print("*" + " " * 3 + "*")
        print()
=======


# Basic Python

# Print "Hello, World!".
print("Hello, World")

# Take a user's name as input and print "Hello, [name]!".
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Take two numbers as input and print their sum, difference, product, and quotient.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")

# Swap the values of two variables without using a third variable.
num1, num2 = num2, num1
print(f"num1: {num1}, num2: {num2}")

# Check if a given number is even or odd.
num1 = int(input("Enter a number: "))
if num1 % 2 == 0:
    print("Even")
else:
    print("Odd")

# Numbers & Operators

# Find the maximum and minimum of three numbers.
# Compute the square and cube of a number.
# Convert a decimal number to binary, octal, and hexadecimal.
# Find the sum of digits of a given number.
# Check if a number is a palindrome.

# Strings

# Reverse a string without using [::-1].
# Count the number of vowels and consonants in a string.
# Check if a given string is a palindrome.
# Remove whitespaces from a string.
# Find the longest word in a sentence entered by the user.

# Lists

# Create a list with 5 numbers and print the largest and smallest.
# Sort a list in ascending and descending order.
# Remove duplicate elements from a list.
# Reverse a list without using [::-1].
# Count occurrences of an element in a list.

# Tuples

# Create a tuple and access elements using indexing.
# Convert a tuple into a list and modify an element.
# Find the index of an element in a tuple.
# Merge two tuples into one.
# Find the length of a tuple without using len().

# Dictionaries

# Create a dictionary of student names and their marks.
# Add, update, and remove an item from a dictionary.
# Print all keys, values, and items from a dictionary.
# Merge two dictionaries into one.
# Check if a given key exists in a dictionary.

# Sets

# Create two sets and perform union, intersection, and difference.
# Check if a set is a subset of another set.
# Remove an element from a set safely.
# Convert a list with duplicate values into a set.
# Find the common elements between two sets.

# Conditional Statements

# Take a number as input and check if it is positive, negative, or zero.
# Take a year as input and check if it is a leap year.
# Write a program that prints:
#     "Fizz" for numbers divisible by 3,
#     "Buzz" for numbers divisible by 5,
#     "FizzBuzz" for numbers divisible by both.
# Find the grade of a student based on their marks.
# Check if a triangle is scalene, isosceles, or equilateral.

# Loops

# Print numbers from 1 to 50 using a loop.
# Print the even numbers from 1 to 50.
# Print this pattern:
# *
# **
# ***
# ****
# *****
# Reverse a number using a loop.
# Print the first 10 Fibonacci numbers.

# List & Dictionary Comprehension

# Create a list of squares of numbers from 1 to 10 using list comprehension.
# Filter out even numbers from a list using list comprehension.
# Create a dictionary where keys are numbers from 1 to 5 and values are their squares.
# Swap keys and values in a dictionary.
# Generate a list of numbers divisible by 3 from 1 to 100 using list comprehension.
>>>>>>> d3fb04e (Update)
