# ===========================
# 1. Variables and Data Types
# ===========================
# 1. Swap two variables without using a third variable.
a = 5
b = 10
a, b = b, a
print(f"Swapped values: a = {a}, b = {b}")

# 2. Check if a variable is of type int.
print(type(a))

# 3. Convert a float to an integer.
float_num = 2.82
int_num = int(float_num)
print(int_num)

# 4. Convert an integer to binary and back.
binary = bin(int_num)
print(binary)

back_to_int = int(binary, 2)
print(back_to_int)

# 5. Create a variable of each data type.
var1 = 42  # int
var2 = 3.14  # float
var3 = "Hello"  # str
var4 = True  # bool
var5 = [1, 2, 3]  # list
var6 = (1, 2, 3)  # tuple
var7 = {1, 2, 3}  # set
var8 = {'key': 'value'}  # dict
print(type(var1), type(var2), type(var3), type(var4), type(var5), type(var6), type(var7), type(var8))

# 6. Get the memory size of a variable.
import sys
example_var = "Hello"
memory_size = sys.getsizeof(example_var)
print(f"Memory size of '{example_var}': {memory_size} bytes")

# 7. Create constants using naming convention.
CONSTANT_NAME = 42
print(f"Constant value: {CONSTANT_NAME}")

# 8. Convert a string to a float and check type.
string_num = "3.14"
float_num = float(string_num)
print(f"Converted float: {float_num}, Type: {type(float_num)}")

# 9. Round a float to 2 decimal places.
float_num = 2.819
rounded_num = round(float_num, 2)
print(f"Rounded number: {rounded_num}")

# 10. Assign multiple variables in one line.
a, b = 1, 2
print(f"Assigned values: a = {a}, b = {b}")

# 11. Use type hints for variable annotations.
name: str = "Alice"
age: int = 30
height: float = 5.5

print(f"Name: {name}, Age: {age}, Height: {height}")
print(f"Type of name: {type(name)}, Type of age: {type(age)}, Type of height: {type(height)}")

# 12. Convert boolean to int and vice versa.
bool_value = True
int_value = int(bool_value)
print(f"Boolean to int: {int_value}")
int_value = 0
bool_value = bool(int_value)
print(f"Int to boolean: {bool_value}")

# 13. Create a hexadecimal number and print it.
int_num = 10
hex_num = hex(int_num)
print(f"Hexadecimal representation: {hex_num}")

# 14. Use the `id()` function to compare variable identities.
a = 10
b = 10
c = 20
print(f"ID of a: {id(a)}, ID of b: {id(b)}, ID of c: {id(c)}")
print(f"a and b point to the same object: {id(a) == id(b)}")
print(f"a and c point to the same object: {id(a) == id(c)}")


# 15. Perform complex number arithmetic.
complex_num1 = 1 + 2j
complex_num2 = 3 + 4j
complex_sum = complex_num1 + complex_num2
complex_product = complex_num1 * complex_num2
print(f"Complex Sum: {complex_sum}, Complex Product: {complex_product}")

# 16. Cast int to string using `str()` and f-string.
int_num = 42
str_num = str(int_num)
print(f"String representation of {int_num}: {str_num}")

# 17. Demonstrate dynamic typing with reassignments.
variable = 42
print(f"Initial type: {type(variable)}")

variable = "Hello"
print(f"Reassigned type: {type(variable)}")


# 18. Create and display a large integer (e.g., factorial of 100).
import math
factorial_100 = math.factorial(100)
print(f"Factorial of 100: {factorial_100}")

# 19. Print a variable’s type in a formatted string.
variable = "Hello, World!"
print(f"The value of the variable is '{variable}', and its type is {type(variable)}.")

# 20. Check if two variables point to the same memory location.
a  = 1
b = 1
print(f"Are a and b pointing to the same memory location? {a is b}")

# ===========================
# 2. Operators
# ===========================
# 1. Use all arithmetic operators in one expression.
a = 5
b = 10
print(f"Arithmetic operations: {a + b}, {a - b}, {a * b}, {a / b}, {a % b}, {a ** b}, {a // b}")

# 2. Use comparison operators to compare strings.
a = "apple"
b = "banana"
print(f"String comparison: {a < b}, {a > b}, {a == b}, {a != b}")

# 3. Use logical operators in an if condition.
if a < b and b != "cherry":
    print(f"{a} is less than {b} and {b} is not 'cherry'.")

# 4. Use `is` and `is not` to compare object identities.
a = [1, 2, 3]
b = a
print(f"Are a and b the same object? {a is b}")
print(f"Are a and b not the same object? {a is not b}")


# 5. Use bitwise AND and OR on two integers.
a = 5  # 0101 in binary
b = 3  # 0011 in binary
print(f"Bitwise AND: {a & b}, Bitwise OR: {a | b}")

# 6. Write a compound assignment using `+=`, `*=`, etc.
a = 10
b = 12
a += b
print(f"Compound assignment: {a}")
a *= 2
print(f"After multiplication: {a}")

# 7. Demonstrate operator precedence.
result = 10 + 5 * 2 ** 2 - 8 / 4
print(f"Operator precedence result: {result}")

# 8. Use the ternary operator for min/max.
min_value = a if a < b else b
print(f"Minimum value: {min_value}")

# 9. Use `in` and `not in` operators for lists.
my_list = [1, 2, 3, 4, 5]
print(f"Is 3 in the list? {3 in my_list}")
print(f"Is 6 not in the list? {6 not in my_list}")

# 10. Shift bits left and right.
shifted_left = a << 1
shifted_right = a >> 1
print(f"Shifted left: {shifted_left}, Shifted right: {shifted_right}")

# 11. Use modulo to check if a number is odd.
is_odd = a % 2 != 0
print(f"Is {a} odd? {is_odd}")

# 12. Compare the ASCII values of characters.
# 13. Use `not` in a logical expression.
# 14. Use bitwise XOR to swap two numbers.
# 15. Use `//` for integer division.
# 16. Use identity and equality together in conditions.
# 17. Demonstrate short-circuiting using `and/or`.
# 18. Write a custom function that uses relational operators.
# 19. Use `+=` to build a string character by character.
# 20. Chain multiple comparison operators in one line.

# ===========================
# 3. Strings
# ===========================
# 1. Reverse a string using slicing.
# 2. Check if a string is a palindrome.
# 3. Count vowels in a string.
# 4. Capitalize the first letter of each word.
# 5. Find the longest word in a sentence.
# 6. Replace spaces with hyphens.
# 7. Find the frequency of each character.
# 8. Remove all punctuations from a string.
# 9. Find all duplicate characters.
# 10. Convert a string to title case.
# 11. Format a string using f-string and `format()`.
# 12. Check if two strings are anagrams.
# 13. Split a sentence into words without using `split()`.
# 14. Convert string to list and back.
# 15. Replace all digits with asterisks.
# 16. Get ASCII value of characters.
# 17. Encode and decode a string using base64.
# 18. Remove consecutive duplicate characters.
# 19. Extract domain from email.
# 20. Convert camelCase to snake_case.

# ===========================
# 4. Lists
# ===========================
# 1. Reverse a list without using reverse().
# 2. Find max and min in a list.
# 3. Remove all duplicates.
# 4. Sort a list of strings by length.
# 5. Merge two sorted lists.
# 6. Find common elements in two lists.
# 7. Flatten a nested list.
# 8. Rotate a list by n positions.
# 9. Separate even and odd numbers.
# 10. Find the second largest number.
# 11. Replace every nth element.
# 12. Count occurrences of an element.
# 13. Remove all empty strings.
# 14. Find the intersection without using set.
# 15. Zip and unzip lists.
# 16. Check if a list is sorted.
# 17. Shuffle a list.
# 18. Multiply all elements in a list.
# 19. Slice a list in chunks of n.
# 20. Find sublists with sum equal to target.

# ===========================
# 5. Tuples
# ===========================
# 1. Create a tuple with one element.
# 2. Convert list to tuple and vice versa.
# 3. Find an element’s index in tuple.
# 4. Unpack multiple values from a tuple.
# 5. Swap two tuples.
# 6. Concatenate two tuples.
# 7. Repeat a tuple n times.
# 8. Check if item exists in tuple.
# 9. Find the length of the longest tuple.
# 10. Create a nested tuple.
# 11. Slice a tuple.
# 12. Count occurrences of element.
# 13. Find max and min of a tuple.
# 14. Reverse a tuple.
# 15. Merge multiple tuples.
# 16. Use tuple in a set or dict key.
# 17. Remove item by converting to list.
# 18. Sort a tuple of numbers.
# 19. Zip lists into tuple list.
# 20. Check for tuple immutability (TypeError).


# ===========================
# 6. Sets
# ===========================
# 1. Create a set with unique elements.
# 2. Remove duplicates from a list using set.
# 3. Find union of two sets.
# 4. Find intersection of two sets.
# 5. Find difference of two sets.
# 6. Check if one set is subset of another.
# 7. Add elements to a set.
# 8. Remove items using discard and remove.
# 9. Pop an element from a set.
# 10. Find symmetric difference.
# 11. Convert string to set of characters.
# 12. Check if two sets are disjoint.
# 13. Create an immutable set (frozenset).
# 14. Count elements in a set.
# 15. Copy a set.
# 16. Clear all elements from set.
# 17. Compare two sets for equality.
# 18. Use set comprehension to filter numbers.
# 19. Iterate through a set.
# 20. Find duplicates using sets.

# ===========================
# 7. Dictionaries
# ===========================
# 1. Create a dictionary with key-value pairs.
# 2. Access a value by key.
# 3. Iterate through keys and values.
# 4. Sort dictionary by keys.
# 5. Sort dictionary by values.
# 6. Merge two dictionaries.
# 7. Find key with max value.
# 8. Remove a key from dictionary.
# 9. Check if key exists.
# 10. Count word frequency in a string.
# 11. Use dictionary comprehension.
# 12. Convert two lists into dictionary.
# 13. Create nested dictionary.
# 14. Update dictionary with new keys.
# 15. Get all keys/values/items.
# 16. Use `get()` with default value.
# 17. Invert keys and values.
# 18. Use dictionary as function arguments.
# 19. Delete all items.
# 20. Group values by keys in list of tuples.

# ===========================
# 8. If-Else and Loops
# ===========================
# 1. Check if a number is positive, negative or zero.
# 2. Find the greatest of three numbers.
# 3. Check if a year is leap year.
# 4. Print multiplication table using loop.
# 5. Sum all numbers in a list.
# 6. Print even numbers from 1 to 100.
# 7. Print prime numbers up to n.
# 8. Reverse a number using loop.
# 9. Count number of digits.
# 10. Find factorial of a number.
# 11. Use `for-else` construct.
# 12. Use `while` to generate Fibonacci.
# 13. Check if string is palindrome using loop.
# 14. Use `break` and `continue` in a loop.
# 15. Use nested loops to print pattern.
# 16. Print pyramid of stars.
# 17. Calculate power using loop.
# 18. Sum of digits of a number.
# 19. Generate all even numbers using while.
# 20. Print a triangle pattern with numbers.

# ===========================
# 9. Functions
# ===========================
# 1. Write a function to calculate area of circle.
# 2. Write a recursive factorial function.
# 3. Use default and keyword arguments.
# 4. Return multiple values from function.
# 5. Write a lambda function for square.
# 6. Use `*args` and `**kwargs`.
# 7. Write a function to reverse a string.
# 8. Write function to filter odd numbers.
# 9. Write a higher-order function.
# 10. Use map() to double list items.
# 11. Use reduce() to multiply list.
# 12. Use filter() for non-empty strings.
# 13. Use zip() in a function.
# 14. Calculate GCD using recursion.
# 15. Count vowels using lambda and filter.
# 16. Create closure that remembers a value.
# 17. Create decorator to measure time.
# 18. Write recursive Fibonacci.
# 19. Use function annotations.
# 20. Create a generator function.

# ===========================
# 10. File Handling
# ===========================
# 1. Read contents from a text file.
# 2. Write text to a new file.
# 3. Append text to an existing file.
# 4. Count number of lines in a file.
# 5. Copy contents from one file to another.
# 6. Read file line by line.
# 7. Write a list to a file.
# 8. Read all words in a file.
# 9. Find the most frequent word in a file.
# 10. Count number of words in a file.
# 11. Read a file and strip newline characters.
# 12. Create a log file with timestamps.
# 13. Search for a word in a file.
# 14. Replace a word in a file.
# 15. Check if file exists before reading.
# 16. Use `with` statement for file operations.
# 17. Read a CSV file line by line.
# 18. Write a dictionary to a CSV file.
# 19. Delete a file safely.
# 20. Use try-except while reading files.

# ===========================
# 11. Regex (Regular Expressions)
# ===========================
# 1. Validate an email address.
# 2. Check if a string is a valid phone number.
# 3. Extract all digits from a string.
# 4. Split a string by multiple delimiters.
# 5. Replace all non-alphanumeric characters.
# 6. Extract domain name from a URL.
# 7. Find all dates in a string.
# 8. Validate a strong password.
# 9. Find all capitalized words.
# 10. Match a pattern at the beginning of string.
# 11. Check if a string is a valid time (HH:MM).
# 12. Extract hashtags from a tweet.
# 13. Replace duplicate spaces with single space.
# 14. Validate IP address.
# 15. Remove HTML tags from string.
# 16. Find all words starting with a vowel.
# 17. Count number of words using regex.
# 18. Find repeated words.
# 19. Match only whole words, not substrings.
# 20. Escape special characters in a string.

# ===========================
# 12. Datetime
# ===========================
# 1. Get today’s date and time.
# 2. Convert string to datetime.
# 3. Calculate difference between two dates.
# 4. Add days to current date.
# 5. Subtract days from current date.
# 6. Format datetime into string.
# 7. Parse a custom date format.
# 8. Get the current time in UTC.
# 9. Compare two datetime objects.
# 10. Get day of the week from date.
# 11. Get the first and last day of the month.
# 12. Get number of days in a given month.
# 13. Check if a date is in the future.
# 14. Convert timestamp to datetime.
# 15. Convert datetime to timestamp.
# 16. Get time difference in seconds.
# 17. Create a countdown timer.
# 18. Display current time in different timezones.
# 19. Get week number of year.
# 20. Create datetime range (daily intervals).

# ===========================
# 13. Unit Testing
# ===========================
# 1. Write a unit test for a sum function.
# 2. Test a function that reverses a list.
# 3. Use `setUp()` method in test class.
# 4. Use `tearDown()` method.
# 5. Test for exceptions using `assertRaises`.
# 6. Use `unittest.mock` to mock an API call.
# 7. Group multiple tests in a test case.
# 8. Use `assertEqual`, `assertNotEqual`, `assertIn`.
# 9. Use test discovery with `unittest`.
# 10. Run tests from command line.
# 11. Measure code coverage.
# 12. Test edge cases like empty input.
# 13. Test return type of function.
# 14. Write parameterized tests.
# 15. Mock file read/write operations.
# 16. Assert object identity.
# 17. Skip a test conditionally.
# 18. Write test for recursive function.
# 19. Test a function with random output using seeds.
# 20. Create custom assertion method.

# ===========================
# 14. Basic Algorithms
# ===========================
# 1. Implement binary search.
# 2. Implement bubble sort.
# 3. Implement insertion sort.
# 4. Implement selection sort.
# 5. Find the GCD of two numbers.
# 6. Find LCM of two numbers.
# 7. Check if a number is prime.
# 8. Generate Fibonacci series.
# 9. Find factorial using loop.
# 10. Reverse an integer.
# 11. Find missing number in list 1 to n.
# 12. Check if two strings are permutations.
# 13. Move all zeroes to end of list.
# 14. Check if a number is a power of two.
# 15. Count frequency of elements in a list.
# 16. Find peak element in an array.
# 17. Implement a palindrome checker.
# 18. Rotate a matrix 90 degrees.
# 19. Find duplicate in a list.
# 20. Merge overlapping intervals.

# ===========================
# 15. OOP (Object-Oriented Programming)
# ===========================
# 1. Create a class with constructor and attributes.
# 2. Add instance method to return formatted string.
# 3. Add class method and static method.
# 4. Implement inheritance with multiple classes.
# 5. Override a method in child class.
# 6. Use `super()` to call parent constructor.
# 7. Create private and protected variables.
# 8. Use `__str__` and `__repr__` methods.
# 9. Track object count using class variable.
# 10. Create abstract class with abstractmethod.
# 11. Implement a simple bank account class.
# 12. Implement polymorphism via duck typing.
# 13. Use property decorators for getter/setter.
# 14. Raise custom exceptions in class.
# 15. Use operator overloading (`__add__`, etc.).
# 16. Implement method chaining.
# 17. Use mixins for reusable functionality.
# 18. Use composition instead of inheritance.
# 19. Create singleton class.
# 20. Serialize and deserialize object using `pickle`.

# ===========================
# 16. Exception Handling
# ===========================
# 1. Catch divide by zero error.
# 2. Handle file not found error.
# 3. Use `finally` block.
# 4. Raise custom exception.
# 5. Use multiple `except` blocks.
# 6. Use `else` with try-except.
# 7. Catch multiple exceptions in one block.
# 8. Create your own exception class.
# 9. Log exceptions using logging module.
# 10. Retry operation using exception handling.
# 11. Handle type errors.
# 12. Gracefully exit on exception.
# 13. Wrap exception in another error.
# 14. Catch exceptions in a loop.
# 15. Handle exceptions in recursion.
# 16. Handle exception with default return value.
# 17. Capture traceback details.
# 18. Raise error when value is not valid.
# 19. Use context manager with error-prone code.
# 20. Validate function input with error raising.
# ===========================