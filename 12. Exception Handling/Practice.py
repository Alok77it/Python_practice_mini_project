# 🚀 Python Exception Handling – Practice Set (20 Questions)

# 1. Write a program that handles division by zero and prints a friendly message.
try:
    result = 10 / 0 
except ZeroDivisionError:
    print("You can't divide by zero")

# 2. Write a program to open a file and handle the case where the file does not exist.
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("cleaning and closing file")

# 3. Create a list and try to access an invalid index. Handle the exception properly.
lst = [1,2,4,5,6]
try:
    lst_index = lst[4]
except IndexError:
    print("Error: The index is invalid")
else:
    print(lst_index)
    
# 4. Create a loop that processes a list of strings and converts them to integers, skipping invalid entries using exception handling.
string_list = ["10", "20", "abc", "30", "xyz"]
valid_integers = []
for item in string_list:
    try:
        number = int(item)
        valid_integers.append(number)
    except ValueError:
        print(f"Skipping invalid entry: {item}")
print("valid Integers: ", valid_integers)
        
# 5. Write a program that uses `try-except-else` to check if a number is positive and divisible by another number.
try:
    num = int(input("Enter a number: "))
    divisor = int(input("Enter a divisior: "))
    
    if divisor == 0:
        raise ZeroDivisionError("Divisor can be zero")
    
    if num <= 0:
        raise ValueError("the number must be positive")
except ValueError as ve:
    print(f"ValueError: {ve}")
except ZeroDivisionError as zde:
    print(f"ZeroDivisionError: {zde}")
else:
    if num % divisor  == 0:
        print(f"{num} is divisible by {divisor}")
    else:
        print(f"{num} is not divisible by {divisor}") 

