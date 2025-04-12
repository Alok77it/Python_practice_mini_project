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


# 12. Write a recursive function to calculate factorial of a number.


# 13. Write a recursive function to print numbers from n to 1.


# 14. Write a recursive function to calculate the sum of first n natural numbers.


# 15. Write a recursive function to generate the nth Fibonacci number.


# 16. Create a generator function that yields numbers from 1 to 5.


# 17. Create a generator function that yields squares of numbers up to n.


# 18. Use `next()` to get values one by one from a generator.


# 19. Write a function that receives a filename and uses a generator to read the file line by line.


# 20. Compare `return` vs `yield` by writing two similar functions: one returns a list, and the other yields values one by one.


# ✅ BONUS: Try combining recursion, *args, and **kwargs in one program!

