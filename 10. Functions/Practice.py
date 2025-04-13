# 🔁 PRACTICE SET: FUNCTIONS, ARGS, KWARGS, LAMBDA, RECURSION, YIELD

# 1. Write a simple function that prints "Hello, World!".
def greet():
    print("Hello World!")
    
greet()

# 2. Write a function that takes two numbers and returns their sum.
def sum(a, b):
    return a + b

sum(10, 12)

# 3. Write a function that takes a name and age, and prints a greeting using both (multiple parameters).
def greeting(name, age):
    return f"Hello {name}, you are {age} years old."

data = greeting("John", 30)

print(data)


# 4. Demonstrate a function that returns multiple values (like name and age as a tuple).
def multiple():
    name = "Alok"
    age = 22
    return name, age

status = multiple()
print(status)
print(type(status))

# 5. Write a function using *args to calculate the sum of any number of numbers.
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

all = sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(all)

# 6. Write a function using **kwargs to print employee details (like name, id, location).
def employee_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
employee_details(name="John Doe", age=30, department="HR", salary=50000)


# 7. Create a function with both *args and **kwargs, and print both inside the function.
def mixed_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
mixed_args(1, 2, 3, name="Alice", age=25, city="New York")

# 8. Write a lambda function to square a number.
square = lambda x: x ** 2
print(square(5))


# 9. Write a lambda function to check if a number is even or odd.
is_even = lambda x: "Even"  if x % 2 == 0 else "Odd"
print(is_even(4))  # Output: Even
print(is_even(5))  # Output: Odd 

# 10. Create a list of numbers and use `map()` with a lambda to double each number.
num = [1, 2, 3, 4, 5]
double = list(map(lambda x: x * 2, num))
print(double)  


# 11. Write a function that demonstrates polymorphism by accepting two different types of arguments (e.g., string and list) and printing their lengths.
def multiply(a, b):
    return a * b 

print(multiply(5, 10))
print(multiply([1], 3))

# 12. Write a recursive function to calculate factorial of a number.
def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a - 1)
    
print(factorial(10))

# 13. Write a recursive function to print numbers from n to 1.
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)
    
print_numbers(5)

# 14. Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
        
print(sum(10))    

# 15. Create a generator function that yields numbers from 1 to 5.
def generator():
    for i in range(1, 6):
        yield i
        
for value in generator():
    print(value)
    

# 16. Create a generator function that yields squares of numbers up to n.
def generator(n):
    for i in range(n):
        yield i * i

for value in generator(10):
    print(value)

# 17. Use `next()` to get values one by one from a generator.
def generator(n):
    for i in range(n):
        yield i
        
gen = generator(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# 18. Write a function that receives a filename and uses a generator to read the file line by line.ex
def read_file_line(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist")

filename = "example.txt"
for line in read_file_line(filename):
    print(line)

# 19. Compare `return` vs `yield` by writing two similar functions: one returns a list, and the other yields values one by one.
def return_function(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result

print(return_function(5))

def yield_function(n):
    for i in range(1, n + 1):
        yield i
    
for value in yield_function(5):
    print(value)


# 20. ✅ BONUS: Try combining recursion, *args, and **kwargs in one program!

def recursive_function(n, *args, **kwargs):
    if n == 0:
        print("Args: ", args)
        print("kwargs: ", kwargs)
        return
    print(f"Current value of n: {n}")
    recursive_function(n - 1, *args, **kwargs)

recursive_function(3, 1, 2, 3, name="Alice", age=23, city="New York")