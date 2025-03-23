# 1. Basic Functions

# Q1: Print a Greeting Message
# Define a function greet() that prints "Hello, World!" when called.

def greet():
    print("Hello, World!")
greet()

# Q2: Check if a Number is Positive, Negative, or Zero
# Define a function check_number(n) that takes an integer n and prints:
# - "Positive" if n > 0
# - "Negative" if n < 0
# - "Zero" if n == 0

def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
check_number(5)
check_number(-5)
check_number(0)

# Q3: Reverse a String
# Define a function reverse_string(s) that takes a string s and returns its reverse.

def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

# 2. Functions with Parameters & Return Values

# Q4: Find the Maximum of Three Numbers
# Define a function find_max(a, b, c) that returns the largest of three numbers.

def find_max(a, b, c):
    return max(a, b, c)
print(find_max(5, 3, 8))

# Q5: Sum of Digits
# Define a function sum_of_digits(n) that returns the sum of the digits of an integer n.

def sum_of_digits(n):
    return sum(int(i) for i in str(n))
print(sum_of_digits(123))

# Q6: Even Numbers from a List
# Define a function filter_even(numbers) that takes a list of numbers and returns 
# a new list containing only the even numbers.

def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]
print(filter_even([1, 2, 3, 4, 5, 6]))

# 3. Advanced Functions

# Q7: Palindrome Checker
# Define a function is_palindrome(s) that returns True if the given string s is 
# a palindrome, otherwise False.

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))


# Q8: Student with Highest Marks
# Define a function top_student(students) that takes a list of tuples containing 
# student names and marks and returns the name of the student with the highest marks.

def top_student(students):
    return max(students, key=lambda x: x[1])[0]
print(top_student([("Alice", 90), ("Bob", 85), ("Charlie", 95)]))


# Q9: Recursive Fibonacci
# Define a recursive function fibonacci(n) that returns the nth Fibonacci number.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))


# Q10: Lambda Function for Prime Numbers
# Define a lambda function to filter prime numbers from a list.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers = lambda numbers: list(filter(is_prime, numbers))
print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# 4. Special Function Types

# Q11: Using *args
# Define a function sum_all(*args) that takes any number of arguments and returns their sum.

def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))


# Q12: Using **kwargs
# Define a function student_info(**kwargs) that takes student details as keyword arguments 
# and prints them in a formatted manner.


def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_info(name="Alice", age=20, city="New York")

# Q13: Using map() to Square Numbers
# Define a function that uses map() and a lambda function to square all numbers in a list.


def square_numbers(numbers):
    return list(map(lambda x: x * x, numbers))
print(square_numbers([1, 2, 3, 4, 5]))

# Q14: Using filter() to Get Even Numbers
# Define a function that uses filter() and a lambda function to extract even numbers from a list.

def filter_even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))
print(filter_even([1, 2, 3, 4, 5, 6]))


# Q15: Using reduce() to Find Product of List
# Define a function that uses reduce() to find the product of all numbers in a list.


def product_of_numbers(numbers):
    from functools import reduce
    return reduce(lambda x, y: x * y, numbers)
print(product_of_numbers([1, 2, 3, 4, 5]))

# 5. Real-World Applications

# Q16: Web Scraping with Functions
# Define a function get_page_title(url) that fetches and returns the title of a webpage 
# using requests and BeautifulSoup.




# Q17: File Renaming Automation
# Define a function rename_files(folder_path, prefix) that renames all files in a given 
# folder with a specified prefix.




# Q18: AI Assistant
# Define a function ai_assistant(query) that takes user input and returns an appropriate 
# response based on keywords.



# 6. Bonus Challenges

# Q19: Decorators
# Define a decorator execution_time() that measures and prints the execution time of any function.



# Q20: Function Inside Function
# Define a function outer_function() that contains another function inner_function() inside it, and calls it.


