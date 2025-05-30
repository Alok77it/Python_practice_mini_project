# === BASIC PYTHON ===
# 1. Write a program to check if a number is prime.
def prime_number(number):
    if number <= 1:
        return False
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if prime_number(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# 2. Implement a function to find the factorial of a number.
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative number"
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

print(factorial(5))

# 3. Check if a given year is a leap year.
def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("enter the year: "))
if leap_year(year):
    print(f"{year} is leap year")
else:
    print(f'{year} is not leap year ')
     

# 4. Find the greatest common divisor (GCD) of two numbers.
import math

a = 10
b = 20

gcd = math.gcd(a, b)

print(f"GCD of a: {a} and b: {b} is {gcd}")

# 5. Reverse the digits of an integer without converting to string.
def reverse(number):
    reversed_num = 0
    sign = 1 if number > 0 else -1
    number = abs(number)
    
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number = number // 10
    
    return reversed_num * sign

print(reverse(1234))    # Output: 4321
print(reverse(-9876))   # Output: -6789


# 6. Calculate the sum of digits of a number.
def sum_of_digits(a,b):
    return a + b

a = int(input("Enter the 1st number: "))  
b = int(input("Enter the 2nd number: "))
sum = sum_of_digits(a, b)
print(sum)


# 7. Given two numbers, swap their values without using a temporary variable.
num1 = 10
num2 = 12
num1, num2 = num2, num1
print(num1)
print(num2)

# 8. Write a program to check if a number is a palindrome.
def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Example usage:
num = 12321
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


# 9. Find the nth Fibonacci number using iteration.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 7
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

# 10. Check if a string contains only digits.
s = "123123"
if s.isdigit():
    print("Strings contains only digits")
else:
    print("Strings not contains only digits")

# 11. Convert Celsius to Fahrenheit.
def cel_to_fah(celsius):
    return (celsius * 9 / 5) + 32

temp_c = 23
temp_f = cel_to_fah(temp_c)
print(f"{temp_c}C : {temp_f}F")

# 12. Calculate the area of a circle given the radius.
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

r = 4
print(f"The area of circle: {r} = {area_of_circle(r)}")
    
# 13. Print all even numbers from 1 to N.
n = int(input("Enter the limit: "))
for num in range(1, n +1):
    if num % 2 == 0:
        print(num)

# 14. Find the minimum and maximum from three numbers.
import math
a = [1,5,10]
max_num = max(a)
print(f"Maximum number: {max_num}")
min_num = min(a)
print(f"Minimum number: {min_num}")

# 15. Check if a number is Armstrong number.
num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
power = len(digits)
total = sum(d ** power for d in digits)

if num == total:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")


# 16. Write a program to calculate the compound interest.
p = int(input("Enter the principal: "))
r = int(input("Enter the rate interest: "))
t = int(input("time: "))


# 17. Convert a decimal number to binary.


# 18. Calculate the sum of all natural numbers below N that are multiples of 3 or 5.


# 19. Implement integer division without using the division operator.


# 20. Write a function to check if a character is a vowel or consonant.


# === OPERATORS ===
# 1. Implement a calculator supporting +, -, *, / using functions.


# 2. Given two integers, determine if their bitwise AND is zero.
# 3. Swap two numbers using XOR operator.
# 4. Check if a number is even or odd using bitwise operators.
# 5. Write a program to count the number of set bits in an integer.
# 6. Calculate the result of (a^b) % m efficiently (modular exponentiation).
# 7. Check if two integers have opposite signs using bitwise operators.
# 8. Clear the lowest set bit of a number.
# 9. Determine if a number is a power of two using bitwise operations.
# 10. Implement addition of two numbers without using '+' operator.
# 11. Find the maximum of two numbers without using comparison operators.
# 12. Implement a function to toggle the ith bit of a number.
# 13. Given an integer, set its rightmost zero bit.
# 14. Check if a number is divisible by 4 using bitwise operators.
# 15. Reverse the bits of a 32-bit unsigned integer.
# 16. Calculate XOR of all numbers in an array where every element appears twice except one.
# 17. Given a number, count how many bits need to be flipped to convert it to another number.
# 18. Check if a number is divisible by 3 using bitwise operators.
# 19. Write a program to find two numbers that appear only once in an array where every other number appears twice.
# 20. Implement right rotate and left rotate on bits of an integer.

# === CONDITIONS ===
# 1. Given three sides, check if they form a valid triangle.
# 2. Write a program to grade students based on their marks.
# 3. Check if a character is uppercase, lowercase, digit, or special character.
# 4. Determine if a year is a century year and leap year.
# 5. Find the largest of three numbers using nested if-else.
# 6. Check if a person is eligible to vote based on age.
# 7. Check if a string is a valid email (basic validation).
# 8. Determine if a number is positive, negative, or zero.
# 9. Write a program to check divisibility by 7 and 11.
# 10. Implement a simple calculator with if-elif for operations.
# 11. Check if a triangle is equilateral, isosceles, or scalene.
# 12. Given a day number (1 to 7), print the day name.
# 13. Find if a character is a digit or alphabet.
# 14. Determine if a number is prime using conditional checks.
# 15. Classify angles as acute, right, obtuse based on degrees.
# 16. Check if a string contains only alphabets.
# 17. Implement a traffic light logic: green, yellow, red based on seconds.
# 18. Validate a password (length, contains digits, uppercase, lowercase).
# 19. Check if a point lies inside, on, or outside a circle.
# 20. Find if a year is a leap year or not using a single conditional expression.

# === STRINGS ===
# 1. Reverse a string without using slicing.
# 2. Check if a string is a palindrome.
# 3. Count the frequency of each character in a string.
# 4. Remove all vowels from a string.
# 5. Find the first non-repeating character in a string.
# 6. Check if two strings are anagrams.
# 7. Implement a function to capitalize the first letter of each word.
# 8. Count the number of words in a string.
# 9. Remove all whitespace from a string.
# 10. Check if a string contains only digits.
# 11. Implement strstr (find substring) without built-in functions.
# 12. Convert a string to lowercase without using built-in functions.
# 13. Replace all occurrences of a substring with another substring.
# 14. Find the longest palindrome substring.
# 15. Compress a string using counts of repeated characters (e.g. aabcc -> a2b1c2).
# 16. Check if a string contains balanced parentheses.
# 17. Count the number of uppercase and lowercase letters.
# 18. Reverse words in a sentence.
# 19. Implement a Caesar cipher encryption.
# 20. Find all permutations of a string.

# === LISTS ===
# 1. Find the maximum and minimum in a list.
# 2. Reverse a list in place.
# 3. Remove duplicates from a list without using sets.
# 4. Find the second largest number in a list.
# 5. Rotate a list by k elements to the right.
# 6. Find the intersection of two lists.
# 7. Merge two sorted lists into one sorted list.
# 8. Check if a list is a palindrome.
# 9. Find the missing number in a list of 1 to N.
# 10. Find all pairs in a list whose sum equals a given number.
# 11. Implement list flattening for a nested list.
# 12. Move all zeros in a list to the end without changing order of other elements.
# 13. Find the longest increasing subsequence in a list.
# 14. Find the common elements in three lists.
# 15. Remove all negative numbers from a list.
# 16. Find the element that appears only once in a list where others appear twice.
# 17. Implement binary search on a sorted list.
# 18. Find the product of all elements except self.
# 19. Check if two lists are rotations of each other.
# 20. Find the kth smallest element in a list.

# === TUPLES ===
# 1. Create a tuple and access elements by index.
# 2. Write a function that returns multiple values as a tuple.
# 3. Swap two variables using tuple unpacking.
# 4. Check if an element exists in a tuple.
# 5. Count occurrences of an element in a tuple.
# 6. Convert a list to a tuple.
# 7. Find the index of an element in a tuple.
# 8. Unpack a tuple of 3 elements into separate variables.
# 9. Find the length of a tuple.
# 10. Concatenate two tuples.
# 11. Slice a tuple from index i to j.
# 12. Convert a tuple to a string.
# 13. Use tuple in a dictionary as a key.
# 14. Iterate over a tuple and print all elements.
# 15. Compare two tuples lexicographically.
# 16. Sort a list of tuples based on the second element.
# 17. Swap the first and last element in a tuple.
# 18. Find the maximum and minimum element in a tuple.
# 19. Convert a tuple of numbers into a list of squares.
# 20. Use a tuple to return both quotient and remainder of division.

# === SETS ===
# 1. Create a set from a list and remove duplicates.
# 2. Find union of two sets.
# 3. Find intersection of two sets.
# 4. Find difference of two sets.
# 5. Check if a set is a subset of another.
# 6. Check if a set is a superset of another.
# 7. Add elements to a set.
# 8. Remove elements from a set.
# 9. Find symmetric difference between two sets.
# 10. Check if two sets are disjoint.
# 11. Find elements present in exactly one of two sets.
# 12. Convert a string to a set of characters.
# 13. Find the length of a set.
# 14. Clear all elements from a set.
# 15. Use sets to find duplicates in a list.
# 16. Given two lists, find elements that are common and unique using sets.
# 17. Find elements that appear in at least two out of three sets.
# 18. Find the complement of a set given a universal set.
# 19. Remove all elements of one set from another.
# 20. Implement set intersection without using built-in methods.

# === DICTIONARIES ===
# 1. Create a dictionary from two lists: keys and values.
# 2. Access and update dictionary elements.
# 3. Remove a key-value pair from a dictionary.
# 4. Check if a key exists in a dictionary.
# 5. Iterate over keys, values, and items.
# 6. Count frequency of characters in a string using a dictionary.
# 7. Merge two dictionaries.
# 8. Invert keys and values in a dictionary.
# 9. Find the key with the maximum value.
# 10. Sort a dictionary by values.
# 11. Group a list of tuples into a dictionary with keys and list of values.
# 12. Create a dictionary with default values using `dict.fromkeys()`.
# 13. Use dictionary comprehension to create squares of numbers.
# 14. Find common keys between two dictionaries.
# 15. Find keys that are unique to one dictionary.
# 16. Count occurrences of words in a list.
# 17. Create a nested dictionary and access nested values.
# 18. Update dictionary with another dictionary's values.
# 19. Remove duplicate values in a dictionary keeping first occurrence.
# 20. Implement a phone book using dictionary with add, search, and delete features.

# === LOOPS ===
# 1. Print all numbers from 1 to N using a for loop.
# 2. Print the multiplication table of a number.
# 3. Sum all numbers in a list using a loop.
# 4. Print all even numbers between 1 and 100.
# 5. Calculate factorial using a while loop.
# 6. Print Fibonacci series up to N terms.
# 7. Find the sum of digits of a number using a loop.
# 8. Iterate over a list and print index and element.
# 9. Use nested loops to print a pattern (e.g. triangle of stars).
# 10. Find the maximum number in a list using a loop.
# 11. Break the loop when a condition is met.
# 12. Continue to skip printing certain numbers.
# 13. Use else with a loop to print if no break occurred.
# 14. Loop through a string and count vowels.
# 15. Print all prime numbers up to N.
# 16. Implement a guessing game with limited tries using loops.
# 17. Sum all multiples of 3 or 5 below N.
# 18. Reverse a list using a loop.
# 19. Use a loop to remove all occurrences of an element from a list.
# 20. Use enumerate in a loop to get index and value.

# === FUNCTIONS ===
# 1. Write a function to check if a number is prime.
# 2. Implement a recursive function for factorial.
# 3. Write a function with default argument values.
# 4. Implement a function to check palindrome string.
# 5. Write a function that returns multiple values as a tuple.
# 6. Write a function to calculate the sum of all arguments using *args.
# 7. Write a function that accepts keyword arguments (**kwargs).
# 8. Implement a function to find the nth Fibonacci number recursively.
# 9. Write a lambda function to square a number.
# 10. Implement a higher-order function that takes another function as argument.
# 11. Write a function with a nested helper function.
# 12. Use function annotations to specify types.
# 13. Implement a memoized version of Fibonacci.
# 14. Write a function to count occurrences of a character in a string.
# 15. Write a recursive function to reverse a string.
# 16. Write a function to check if two strings are anagrams.
# 17. Implement a function to merge two dictionaries.
# 18. Write a function to flatten a nested list.
# 19. Implement a function to generate all substrings of a string.
# 20. Write a decorator function to time execution of another function.

# === COMPREHENSIONS ===
# 1. Use list comprehension to create a list of squares from 1 to 20.
# 2. Create a list of even numbers between 1 and 50 using comprehension.
# 3. Use dictionary comprehension to map numbers to their squares.
# 4. Create a set comprehension to find unique vowels in a string.
# 5. Filter a list to keep only prime numbers using list comprehension.
# 6. Use nested list comprehension to create a multiplication table (2D list).
# 7. Use list comprehension to flatten a list of lists.
# 8. Use dictionary comprehension to invert keys and values of a dict.
# 9. Use comprehension to remove vowels from a string.
# 10. Create a list of tuples (number, square) for numbers 1 to 10.
# 11. Use set comprehension to find common characters between two strings.
# 12. Create a list comprehension that applies a function to elements of a list.
# 13. Use list comprehension to filter words longer than 5 letters from a list.
# 14. Create a dictionary comprehension from two lists: keys and values.
# 15. Use comprehension to create a list of factorials for numbers 1 to N.
# 16. Use comprehension with conditionals to replace negative numbers with zero.
# 17. Use generator comprehension to yield even numbers up to N.
# 18. Create a list comprehension that converts strings to uppercase.
# 19. Use comprehension to find all palindromic substrings in a list of strings.
# 20. Use comprehension to create a frequency dictionary from a list of words.

# === EXCEPTION HANDLING ===
# 1. Write a program that handles division by zero exception.
# 2. Catch and handle ValueError when converting string to int.
# 3. Handle multiple exceptions in a single try block.
# 4. Use try-except-else-finally blocks.
# 5. Raise a custom exception when a negative number is passed to a function.
# 6. Write a function that retries an operation on exception.
# 7. Use exception chaining with 'raise ... from'.
# 8. Write a program to handle file not found exception.
# 9. Catch exceptions raised by invalid list indexing.
# 10. Implement context manager using try-finally.
# 11. Create a custom exception class.
# 12. Handle KeyboardInterrupt exception gracefully.
# 13. Use assertions to check function input validity.
# 14. Write a program that logs exceptions to a file.
# 15. Catch and handle exceptions in nested function calls.
# 16. Implement retry logic with exponential backoff on exceptions.
# 17. Use else clause in exception handling to run code if no exception occurs.
# 18. Handle JSON decode errors when parsing input.
# 19. Write a function that safely closes resources on exception.
# 20. Create a decorator to catch exceptions and log errors.

