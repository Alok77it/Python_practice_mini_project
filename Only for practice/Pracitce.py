# ================================
# Track 1: Python Core Concepts
# ================================

# ------------ 1. Variables, Data Types, and Operators ------------
# Easy (20)
# 1. Declare two integers and print their sum
a = 10
b = 12
print(a+b)


# 2. Swap two variables using a third variable
a = 10
b = 12
c = a
a = b
b = c
print(a)
print(b)

# 3. Swap two variables without a third variable
a = 10
b = 12
a, b = b, a
print(a)
print(b)


# 4. Check data type of a variable
a = "str"
b = 12
print(type(a))
print(type(b))


# 5. Take input from user and print it
user = input("Enter the name: ")
print(user)

# 6. Add two float numbers
a = 10.12
b = 12.23
print(a + b)

# 7. Multiply an int and float
int1 = 10
float1 = 12.12
print(int1 * float1)


# 8. Convert int to string
int1 = 10
str1 = str(int1)
print(int1)

# 9. Convert string to int
str1 = "10"
int1 = int(str1)
print(int1) 

# 10. Perform modulus operation
a = 10
b = 12
print(a % b)

# 11. Perform floor division
a = 10
b = 2
print(a / b)


# 12. Use exponent operator to square a number
a = 12
print(a * a)

# 13. Chain multiple assignments (a = b = c = 10)
a = b = c = 10

print(a)  # 10
print(b)  # 10
print(c)  # 10


# 14. Use augmented assignment (+=, -=)
a = 10
c = 2
b = 12
b += a
a -= c
print(a)
print(b)
print(c)


# 15. Use relational operators and print results
a = 5
b = 10

print("a == b:", a == b)   # False
print("a != b:", a != b)   # True
print("a > b:", a > b)     # False
print("a < b:", a < b)     # True
print("a >= b:", a >= b)   # False
print("a <= b:", a <= b)   # True


# 16. Use logical operators: and, or, not
x = 5
print(x > 2 and x < 10)   # True, because both conditions are True
x = 5
print(x < 2 or x < 10)    # True, because one condition is True

x = 5
print(not(x > 2 and x < 10))  # False, because condition is True, and `not` reverses it



# 17. Use identity operator (is, is not)
a = [1, 2]
b = a
c = [1, 2]

print(a is b)      # True, because both refer to same object
print(a is c)      # False, different objects even if contents are same
print(a is not c)  # True



# 18. Use membership operator (in, not in)
my_list = [1, 2, 3, 4]

print(2 in my_list)      # True
print(5 not in my_list)  # True



# 19. Print variable memory address (id)
x = 10
print(id(x))  # Prints the memory address (unique ID) of variable x


# 20. Use type casting to add int + string correctly
x = 5
y = "10"
result = x + int(y)
print(result)  # ✅ 15


# Advanced (20)
# 1. Print binary, octal, hexadecimal of a number
a = 12
print(bin(a))
print(oct(a))
print(hex(a))

# 2. Demonstrate difference between == and is
a = [1,3]
b = [1,3]
print(a == b)
print(a is b)

# 3. Convert float to int and observe truncation
x = 5.99
print("Before:", x)
print("After truncation:", int(x))  # Output: 5


# 4. Evaluate complex expression using brackets
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20


# 5. Use divmod() function
quotient, remainder = divmod(10, 3)
print("Quotient:", quotient)
print("Remainder:", remainder)


# 6. Use round(), abs(), pow() functions
x = -5.678
print("Rounded:", round(x, 2))
print("Absolute:", abs(x))
print("Power:", pow(2, 3))


# 7. Input multiple variables in one line
a, b, c = map(int, input("Enter 3 numbers: ").split())
print(f"a {a}, b {b}, c {c}")


# 8. Format output using f-string
name = "Alok"
age = 25
print(f"My name is {name} and I am {age} years old.")

# 9. Use input() with type casting
num = int(input("Enter an integer: "))
print(f"You entered: {num}")


# 10. Use math module to calculate square root
import math

num = float(input("Enter a number: "))
print(f"Square root: {math.sqrt(num)}")



# ------------ 2. Conditionals and Loops ------------
# Easy (20)
# 1. Check if a number is even or odd
num = int(input("Enter the number: "))
def even_odd(num):
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

even_odd(num)


# 2. Check if a number is positive, negative, or zero
num = float(input("Enter the number: "))
def value_check(num):
    if num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    elif num == 0:
        print("Number is zero")
    else:
        print("invalid number")

value_check(num)
    
# 3. Find the largest of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)    

# 4. Print 1 to 10 using for loop
n = 10
for i in range(1, n + 1):
  print(i)
  
# 5. Print 10 to 1 using while loop
i = 10
while i >= 1:
  print(i)
  i = i -1

# 6. Print even numbers from 1 to 20
n = 20
for i in range(1, n + 1):
  if i % 2 == 0:
    print(f"{i} : Even")
  else:
    print(f"{i} : Odd")

# 7. Print all numbers divisible by 3 between 1–30
n = 30
def divisible_by_3(n):
  for i in range(1, n + 1):
    if i % 3 == 0:
      print(f"{i}: Divisible by 3")

divisible_by_3(n)

# 8. Sum first 10 natural numbers
def sum_all(n):
  total = 0
  for i in range(1, n + 1):
    total += i
  print(total)

n = 10
sum_all(n)

# 9. Calculate factorial of a number using loop
def factorial(n):
  if n <  0:
    return "Factorial is not defined for negative number"
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

num = 5
fact = factorial(num)
print(f"The factorial of {num},is {fact}")

# 10. Print multiplication table of a number
n = int(input("Enter the number: "))
for i in range(1,11):
  print(f"{n} X {i} = {n * i }")

# 11. Break a loop when value reaches 5
for i in range(1, 11):
    if i == 5:
        print(f"Breaking loop at i = {i}")
        break  #this will stop the loop
    print(i)

# 12. Use continue to skip odd numbers
for i in range(1, 11):
    if i == 5:
        print(f"Breaking loop at i = {i}")
        continue #skip the this loop point
    print(i)

# 13. Loop through a string and print each char
str = "Hello, I am Alok"
for i in str:
  print(i)

# 14. Count digits in a number using loop
def count_digits(number):
  """
  Counts the number of digits in an integer using a while loop.

  Args:
    number: The integer for which to count digits.

  Returns:
    The number of digits in the integer.
  """
  # Handle the case of 0 separately as the loop won't execute
  if number == 0:
    return 1

  # Make the number positive to handle negative inputs
  number = abs(number)

  count = 0
  # Loop until the number becomes 0
  while number > 0:
    # Integer division by 10 removes the last digit
    number = number // 10
    # Increment the count for each digit removed
    count += 1

  return count

# Example usage:
my_number = 12345
digit_count = count_digits(my_number)
print(f"The number of digits in {my_number} is: {digit_count}")


# 15. Reverse a number using loop


# 16. Check if a year is leap year


# 17. Check if a number is prime


# 18. Print triangle pattern using *


# 19. Create basic calculator using if-else


# 20. Print sum of digits of a number


# Advanced (20)
# 1. Use nested if to validate login system
# 2. Use nested loop to print number triangle
# 3. Print all prime numbers between 1 and 100
# 4. Use while-else and for-else blocks
# 5. Print Floyd’s triangle using numbers
# 6. Generate Fibonacci series up to n
# 7. Print pyramid pattern with *
# 8. Calculate GCD using loop
# 9. Calculate LCM of two numbers
# 10. Use pass statement in a loop
# 11. Print inverted triangle pattern
# 12. Use match-case (Python 3.10+)
# 13. Generate perfect numbers below 1000
# 14. Use zip() in a loop
# 15. Use enumerate() to access index + value
# 16. Print numbers in reverse using range()
# 17. Simulate ATM withdrawal system
# 18. Write menu-driven program using loop
# 19. Count uppercase/lowercase letters in string
# 20. Validate password strength using conditions


# ------------ 3. Strings ------------
# Easy (20)
# 1. Reverse a string
# 2. Count number of vowels
# 3. Remove spaces from a string
# 4. Convert string to uppercase
# 5. Convert string to lowercase
# 6. Check if string is palindrome
# 7. Count occurrences of a character
# 8. Find first occurrence of substring
# 9. Slice first 5 characters
# 10. Concatenate two strings
# 11. Use string formatting with % operator
# 12. Use format() method
# 13. Capitalize the first character
# 14. Split string into list
# 15. Join list into string
# 16. Replace a word in string
# 17. Check if string starts/ends with a word
# 18. Check if string contains only digits
# 19. Use strip() to remove spaces
# 20. Escape special characters using backslash

# Advanced (20)
# 1. Compress a string (aaaabb → a4b2)
# 2. Check if two strings are anagrams
# 3. Remove all duplicate characters
# 4. Longest word in a sentence
# 5. Count frequency of all characters
# 6. Find all substrings of a string
# 7. Use list comprehension with strings
# 8. Use regex to validate email
# 9. Title-case a string manually
# 10. Swap first and last characters
# 11. Reverse words in a sentence
# 12. Convert sentence into camelCase
# 13. Use translate() with mapping
# 14. Encode and decode using ord()/chr()
# 15. Use isalpha(), isalnum(), isnumeric()
# 16. Mask part of a string (like a password)
# 17. Remove punctuation from string
# 18. Custom find & replace function
# 19. Format string using f-string with expressions
# 20. Parse CSV-style data in a string

# ------------ 4. Lists and Tuples ------------
# Easy (20)
# 1. Create a list of 5 integers and print it
# 2. Append an element to a list
# 3. Remove an element from a list
# 4. Find length of a list
# 5. Access first and last element of a list
# 6. Slice a list from index 1 to 3
# 7. Iterate over list and print elements
# 8. Check if an element exists in list
# 9. Concatenate two lists
# 10. Repeat a list n times
# 11. Create a tuple with 4 elements
# 12. Access tuple elements by index
# 13. Count occurrences of an element in a list
# 14. Find max and min in a list
# 15. Sort a list in ascending order
# 16. Reverse a list
# 17. Convert tuple to list
# 18. Convert list to tuple
# 19. Insert element at specific index in list
# 20. Clear all elements from a list

# Advanced (20)
# 1. Remove duplicates from a list preserving order
# 2. Flatten a list of lists (e.g. [[1,2],[3,4]] → [1,2,3,4])
# 3. Use list comprehension to create squares of numbers 1–10
# 4. Find common elements between two lists
# 5. Merge two sorted lists into one sorted list
# 6. Implement your own function to reverse a list
# 7. Count frequency of each element in a list
# 8. Use zip() to combine two lists into list of tuples
# 9. Find second largest number in a list
# 10. Sort a list of tuples by second element
# 11. Use tuple unpacking in function return values
# 12. Create nested lists and access elements
# 13. Swap elements at two indices in a list
# 14. Rotate a list by n elements
# 15. Use list slicing to skip every alternate element
# 16. Convert list of strings to a single string with delimiter
# 17. Implement stack operations using list
# 18. Use enumerate() with lists
# 19. Use filter() with a lambda on list
# 20. Use map() to convert list of strings to ints

# ------------ 5. Dictionaries and Sets ------------
# Easy (20)
# 1. Create a dictionary with 3 key-value pairs
# 2. Access value by key in dictionary
# 3. Add new key-value pair to dictionary
# 4. Update value for an existing key
# 5. Delete a key-value pair from dictionary
# 6. Check if key exists in dictionary
# 7. Iterate over dictionary keys
# 8. Iterate over dictionary values
# 9. Iterate over key-value pairs
# 10. Get keys and values as lists
# 11. Create an empty set and add elements
# 12. Remove element from set
# 13. Check if element in set
# 14. Perform union of two sets
# 15. Perform intersection of two sets
# 16. Perform difference of two sets
# 17. Clear a set
# 18. Get length of dictionary and set
# 19. Use dict.get() method with default value
# 20. Copy a dictionary

# Advanced (20)
# 1. Count frequency of characters in a string using dictionary
# 2. Merge two dictionaries
# 3. Use dictionary comprehension to square numbers 1–5 as {n: n*n}
# 4. Create nested dictionaries and access values
# 5. Invert keys and values in a dictionary
# 6. Sort dictionary by keys
# 7. Sort dictionary by values
# 8. Remove duplicates from list using set
# 9. Use frozenset and explain difference from set
# 10. Create a default dictionary using collections.defaultdict
# 11. Use set comprehension
# 12. Find keys with maximum values in dictionary
# 13. Count words in a sentence using dictionary
# 14. Implement phonebook with add/search/delete operations using dict
# 15. Use popitem() method of dictionary
# 16. Use update() method with another dictionary
# 17. Check if two dictionaries are equal
# 18. Use dict.fromkeys() method
# 19. Filter dictionary items based on condition
# 20. Implement LRU cache using OrderedDict (conceptual)

# ------------ 6. Functions and Recursion ------------
# Easy (20)
# 1. Define a function that adds two numbers
# 2. Function with default argument
# 3. Function that returns multiple values
# 4. Use keyword arguments in function call
# 5. Use *args in a function
# 6. Use **kwargs in a function
# 7. Anonymous function (lambda) to add two numbers
# 8. Use map() with lambda and list
# 9. Use filter() with lambda and list
# 10. Use reduce() to sum list elements
# 11. Recursive function to find factorial
# 12. Recursive function to calculate nth Fibonacci number
# 13. Use return statement to exit function early
# 14. Function with no return value (returns None)
# 15. Nested functions (define function inside function)
# 16. Use global variable inside function
# 17. Use nonlocal variable inside nested function
# 18. Write docstring for a function
# 19. Use function annotations (type hints)
# 20. Call function using function object

# Advanced (20)
# 1. Decorator to print function execution time
# 2. Memoization in recursive Fibonacci
# 3. Use functools.partial to create partial functions
# 4. Generator function using yield
# 5. Create a closure and explain
# 6. Recursive function to solve Tower of Hanoi
# 7. Function that accepts another function as argument
# 8. Use function to generate infinite Fibonacci sequence with yield
# 9. Recursive binary search implementation
# 10. Tail recursion (conceptual, Python doesn’t optimize)
# 11. Use assert statement in function
# 12. Currying function example
# 13. Function with variable scope examples
# 14. Recursive function to generate permutations of a string
# 15. Recursive function to solve subset sum problem
# 16. Use lambda inside a function
# 17. Decorator with arguments
# 18. Use context manager as a function (with statement)
# 19. Partial application of function arguments
# 20. Implement a retry decorator

# ------------ 7. File Input/Output ------------
# Easy (20)
# 1. Open a file and write a string
# 2. Read the whole content of a file
# 3. Read a file line by line
# 4. Append text to a file
# 5. Use with statement to open file
# 6. Write list of strings to a file
# 7. Read file and count number of words
# 8. Copy content from one file to another
# 9. Check if file exists before reading
# 10. Use try-except for file operations
# 11. Read CSV file and print each row (basic)
# 12. Write CSV file with header row
# 13. Use os module to get file size
# 14. Rename a file
# 15. Delete a file
# 16. Read binary file content
# 17. Write binary data to file
# 18. Use pathlib for file operations
# 19. Read large file using buffered read
# 20. Write JSON data to a file

# Advanced (20)
# 1. Parse CSV file and convert to list of dicts
# 2. Use JSON module to load and dump data
# 3. Read and write compressed files using gzip
# 4. Write a log file with timestamps
# 5. Use configparser to read config files
# 6. File locking concepts (basic)
# 7. Use mmap module for file mapping
# 8. Write file using contextlib.redirect_stdout
# 9. Handle Unicode errors while reading files
# 10. Implement file watcher to detect file changes
# 11. Use pathlib to iterate files in directory
# 12. Read fixed-width formatted files
# 13. Write multi-line strings to file
# 14. Read partial file (seek and read)
# 15. Use tempfile module for temp files
# 16. Use shutil to copy files/directories
# 17. Read Excel files using openpyxl (basic)
# 18. Write Excel files using openpyxl
# 19. Create a file backup script
# 20. Write script to remove duplicate lines from a file

# ------------ 8. Classes and Object-Oriented Programming (OOP) ------------
# Easy (20)
# 1. Define a class with __init__ method
# 2. Create an object of a class
# 3. Add method to class that prints attribute
# 4. Use self keyword in class methods
# 5. Create class with class variables and instance variables
# 6. Use __str__ method to print object info
# 7. Create two instances with different attributes
# 8. Access and modify instance variables
# 9. Use default argument in class constructor
# 10. Create methods to update attributes
# 11. Define a method outside __init__
# 12. Create class with a method that returns a value
# 13. Use del keyword to delete an attribute
# 14. Create a class method (@classmethod)
# 15. Create a static method (@staticmethod)
# 16. Use property decorator to define getter
# 17. Use setter decorator to modify attribute
# 18. Create a class with private attributes (__var)
# 19. Use inheritance: define subclass inheriting superclass
# 20. Override method in subclass

# Advanced (20)
# 1. Use super() to call parent constructor
# 2. Multiple inheritance example
# 3. Use __repr__ method for object representation
# 4. Implement operator overloading (__add__, __str__)
# 5. Use abstract base class (ABC module)
# 6. Implement interfaces using ABCs
# 7. Use composition instead of inheritance
# 8. Implement property with validation
# 9. Use metaclasses (basic)
# 10. Implement singleton pattern in Python
# 11. Create iterator class (__iter__, __next__)
# 12. Use context manager with __enter__ and __exit__
# 13. Use descriptors for attribute management
# 14. Implement class decorators
# 15. Create mixins for reusable functionality
# 16. Use slots to reduce memory footprint
# 17. Dynamic class creation using type()
# 18. Use dataclasses module for classes
# 19. Serialization and deserialization of objects (pickle)
# 20. Write unit tests for class methods using unittest


