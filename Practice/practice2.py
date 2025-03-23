def greet(name = "Guest"):
    print(f"Hello, {name}!")
greet()
greet("John")

def student_info(name, age):
    print(f"Name: {name}, Age: {age}")
student_info("Alice", 20)

def sum_all(*numbers):
    return sum(numbers)
print(sum_all(1, 2, 3, 4, 5))

def student_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
student_details(name="Alice", age=20, city="New York")


square = lambda x: x * x
print(square(5))

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

"""with open("/var/log/syslog", "w") as log_file:
    logs = log_file.readlines()
    print(logs[-1])
    """
    
import subprocess
output = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(output.stdout)

import os
home_dir = os.getenv("HOME")
print(home_dir)
