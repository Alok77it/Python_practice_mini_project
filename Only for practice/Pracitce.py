# ========================
# 1. Basic Python (10 Questions)
# ========================
# 1. Print "Welcome to Python on Linux!".
print("Welcome To Python on Linux!")

# 2. Take two numbers as input and print their sum, difference, and product.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum = a + b
diff = a - b
prod = a * b
print(f"Sum: {sum}, Difference: {diff}, Product: {prod}")


# 3. Print the data type of 5 different variables.
a = 5
b = 3.14
c = "Hello"
d = True
e = [1, 2, 3]
print(type(a), type(b), type(c), type(d), type(e))


# 4. Swap two numbers (without using a third variable).
a = 5
b = 10
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")

# 5. Accept a user name and print it with a greeting.   
user = input("Enter your name: ")
print(f"Hello, {user}!")

# 6. Convert meters to kilometers.
meters = float(input("Enter meters: "))
kilometers = meters / 1000
print(f"{meters} meters is equal to {kilometers} kilometers.")


# 7. Take an age input and print the year user turns 100.
age = int(input("Enter your age: "))
year_turn_100 = 2023 + (100 - age)
print(f"You will turn 100 years old in the year {year_turn_100}.")


# 8. Calculate the area of a rectangle.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is {area} square units.")

# 9. Take float input and convert to integer.
float_number = float(input("Enter a float number: "))
integer_number = int(float_number)
print(f"The integer value is {integer_number}.")


# 10. Take name and age as input and display them using f-string.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Name: {name}, Age: {age}.")

# ========================
# 2. Operators (10 Questions)
# ========================
# 1. Demonstrate use of all arithmetic operators.
a = 10
b = 5
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")
print(f"Floor Division: {a // b}")

# 2. Find the cube of a number using exponent operator.
side = 5
cube = side ** 3
print(f"The cube of {side} is {cube}.")

# 3. Use floor division and modulo to split minutes into hours and minutes.
mintues = 140
hours = mintues // 60
minutes = mintues % 60
print(f"{mintues} minutes is equal to {hours} hours and {minutes} minutes.")

# 4. Increment a variable by 5 using +=.
a = 10
a += 5
print(a)

# 5. Use relational operators to compare two numbers.

a = 10
b = 20
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

# 6. Use logical operators to check if number is between 10 and 50.
num = 30
print(f"Is {num} between 10 and 50? {'Yes' if 10 < num < 50 else 'No'}")

# 7. Use bitwise AND, OR, XOR on two integers.
a = 10
b = 4
print(f"Bitwise AND: {a & b}")
print(f"Bitwise OR: {a | b}")
print(f"Bitwise XOR: {a ^ b}")

# 8. Check if two strings are not equal using !=.
a = "Alok"
b = "alok"
print(f"Are '{a}' and '{b}' not equal? {a != b}")

# 9. Use is and is not with None.
value = None
print(f"Is value None? {value is None}")
print(f"Is value not None? {value is not None}")


# 10. Use compound assignment operators to update a score.

score = 10
score += 5
print(f"Updated score: {score}")

# ========================
# 3. Conditionals (10 Questions)
# ========================
# 1. Check if a number is positive, negative, or zero.
n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# 2. Check if number is even or odd.
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Take age and check if eligible to vote.
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 4. Find largest among three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(f"Largest number is {a}")
elif b >= a and b >= c:
    print(f"Largest number is {b}")
else:
    print(f"Largest number is {c}")

# 5. Check if a character is vowel or consonant.
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")

# 6. Simple calculator using if, elif, else.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    print(f"{a} + {b} = {a + b}")
elif operation == '-':
    print(f"{a} - {b} = {a - b}")
elif operation == '*':
    print(f"{a} * {b} = {a * b}")
elif operation == '/':
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")

# 7. Check if a year is leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 8. Check if a person is senior citizen (>60).
age = int(input("Enter your age: "))
if age > 60:
    print("Senior Citizen")
else:
    print("Not a Senior Citizen")

# 9. Take marks and print grade (A, B, C, etc.).
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 50:
    print("Grade E")
elif marks >= 40:
    print("Grade F")
else:
    print("Grade F")

# 10. Use nested if to categorize age groups (child, teen, adult).
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior")


# ========================
# 4. Strings (10 Questions)
# ========================
# 1. Count number of vowels in a string.
string = "I am alok trivedi. Learning Devops"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in string if char in vowels)
print(f"Number of vowels: {vowel_count}")

# 2. Reverse a string manually.
string = "Hello World"
reversed_string = "".join(reversed(string))
print(f"Reversed string: {reversed_string}")

# 3. Check if a string is a palindrome.
string = "madam"
is_palindrome = string == string[::-1]
print(f"Is the string '{string}' a palindrome? {'Yes' if is_palindrome else 'No'}")

# 4. Count frequency of a character in string.
string = "hello world"
char_to_count = "l"
frequency = string.count(char_to_count)
print(f"Frequency of '{char_to_count}' in '{string}': {frequency}")

# 5. Convert string to uppercase and lowercase.
string = "Python Programming"
uppercase = string.upper()
lowercase = string.lower()
print(f"Uppercase: {uppercase}, Lowercase: {lowercase}")

# 6. Remove all spaces from a string.
string = "Remove all spaces"
no_spaces = string.replace(" ", "")
print(f"String without spaces: {no_spaces}")

# 7. Replace a word in a string.
string = "I love Python"
replaced_string = string.replace("Python", "Programming")
print(f"Replaced string: {replaced_string}")

# 8. Find the index of a substring.
string = "Find the index of substring"
substring = "index"
index = string.find(substring)
print(f"Index of '{substring}' in '{string}': {index}")

# 9. Slice and print first 3 and last 3 characters.
string = "SlicingExample"
first_three = string[:3]
last_three = string[-3:]
print(f"First 3 characters: {first_three}, Last 3 characters: {last_three}")

# 10. Join a list of strings using a delimiter.
string_list = ["Python", "is", "fun"]
delimiter = "-"
joined_string = delimiter.join(string_list)
print(f"Joined string: {joined_string}")

# ========================
# 5. Lists (10 Questions)
# ========================
# 1. Create a list of 5 items and print them.
# 2. Add and remove elements from a list.
# 3. Sort list without using sort().
# 4. Find max and min from a list.
# 5. Remove duplicates using loop.
# 6. Merge two lists into one.
# 7. Print even numbers from a list.
# 8. Replace an item at a given index.
# 9. Use pop() and insert() in a list.
# 10. Reverse a list without using reverse().

# ========================
# 6. Tuples (10 Questions)
# ========================
# 1. Create a tuple of 5 elements and access them using index.
# 2. Convert a list to a tuple.
# 3. Find the length of a tuple.
# 4. Count occurrences of an item.
# 5. Find index of an item.
# 6. Slice a tuple.
# 7. Check if an item exists in a tuple.
# 8. Concatenate two tuples.
# 9. Unpack a tuple into variables.
# 10. Use tuple as a key in a dictionary.

# ========================
# 7. Sets (10 Questions)
# ========================
# 1. Create a set and add 5 elements.
# 2. Perform union, intersection, difference.
# 3. Remove an element safely using discard().
# 4. Check if two sets are disjoint.
# 5. Convert list to set to remove duplicates.
# 6. Add multiple elements to a set.
# 7. Check membership of an item in set.
# 8. Find symmetric difference.
# 9. Use set comprehension to store squares.
# 10. Create a frozen set and try modifying it.

# ========================
# 8. Dictionaries (10 Questions)
# ========================
# 1. Create a dictionary of names and marks.
# 2. Add a new key-value pair.
# 3. Update an existing key.
# 4. Delete a key-value pair.
# 5. Loop through dictionary and print key-value.
# 6. Check if key exists in dictionary.
# 7. Merge two dictionaries.
# 8. Create a nested dictionary and access value.
# 9. Count word frequency in a string.
# 10. Convert 2 lists into a dictionary using zip().

# ========================
# 9. Loops (10 Questions)
# ========================
# 1. Print numbers 1 to 10 using for loop.
# 2. Print even numbers between 1 to 50.
# 3. Print Fibonacci series up to n terms.
# 4. Print multiplication table of a number.
# 5. Calculate factorial using loop.
# 6. Use break when number divisible by 7 is found.
# 7. Use continue to skip a number.
# 8. Iterate through a list using for.
# 9. Loop through dictionary and print values.
# 10. Use while loop to print digits of a number.

# ========================
# 10. Functions (10 Questions)
# ========================
# 1. Function to add two numbers.
# 2. Function to find square and cube.
# 3. Function to return max of three numbers.
# 4. Function to check if number is prime.
# 5. Function with default arguments.
# 6. Use *args to pass variable arguments.
# 7. Use **kwargs to pass keyword arguments.
# 8. Return multiple values (sum, product).
# 9. Recursive function for factorial.
# 10. Function to check if a string is palindrome.

# ========================
# 11. Comprehensions (10 Questions)
# ========================
# 1. List of squares using list comprehension.
# 2. Filter even numbers from list using list comp.
# 3. Dict comp: keys as numbers, values as squares.
# 4. Set comp: unique chars in a string.
# 5. List comp to convert string list to uppercase.
# 6. Dict comp: count frequency of words in list.
# 7. Nested list comp: 2D matrix of 0s.
# 8. Flatten a 2D list using list comp.
# 9. Reverse each word in a sentence using list comp.
# 10. Use list comp with condition inside expression.

# ========================
# 12. Exception Handling (10 Questions)
# ========================
# 1. Handle division by zero.
# 2. Handle file not found error.
# 3. Use try, except, else, finally.
# 4. Raise a custom exception if input is negative.
# 5. Handle multiple exceptions.
# 6. Read a number from user and catch invalid input.
# 7. Catch index out of range in list.
# 8. Handle key error in dictionary.
# 9. Write to a file and handle permission error.
# 10. Use assert to validate input.

# ========================
# 13. Arrays (10 Questions)
# ========================
# 1. Create an integer array and print it.
# 2. Append elements to an array.
# 3. Access elements using indexing and slicing.
# 4. Reverse array using loop.
# 5. Find sum and average of array.
# 6. Insert an element at index.
# 7. Remove an element from array.
# 8. Search for an element in array.
# 9. Copy one array to another.
# 10. Convert list to array and back to list.
