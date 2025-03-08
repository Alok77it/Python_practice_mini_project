# 📌 Loops Practice Set (Covers for, while, break, continue, pass, else, functions, and more)

# 📂 Part 1: Basic Looping (For & While)

# Q1: Print numbers from 1 to 10 using a for loop.
# Write your code here

num = 1
for i in range(1, 11):
    print(num)
    num += 1

# Q2: Print numbers from 10 to 1 using a while loop.
# Write your code here

a = 10
while a >= 1:
    print(a)
    a -= 1

# Q3: Print all even numbers between 1 and 20 using a loop.
# Write your code here
a = 1
while a <= 20:
    if a % 2 == 0:
        print(a)
    a += 1  

# Q4: Print all odd numbers between 1 and 20 using a loop.
# Write your code here

a = 1 
while a <= 20:
    if a % 2 != 0:
        print(a)
    a += 1

# Q5: Print each character of the string "PythonLoops" separately using a loop.
# Write your code here

string = "PythonLoops"
for i in string:
    print(i)


# 📂 Part 2: Loop Control Statements (break, continue, pass)

# Q6: Use break to stop the loop when the number reaches 5.
# for i in range(1, 11):
#     # Stop when i is 5

num = 1
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Q7: Use continue to skip printing 5 but print all other numbers from 1 to 10.
# for i in range(1, 11):
#     # Skip 5 and continue loop

num = 1
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Q8: Use pass inside a loop (it does nothing but prevents errors).
# for i in range(5):
#     # Use pass statement

for i in range(5):
    pass


# 📂 Part 3: else in Loops

# Q9: Use else in a for loop to print "Loop finished" after completion.

num = 1
for i in range(1, 6):
    print(i)
else:
    print("Loop finished")

# Q10: Use else in a while loop to print "Loop ended naturally" when it completes without break.

a = 1
while a <= 10:
    print(a)
    a += 1
else:
    print("Loop ended naturally")

# 📂 Part 4: Loops with Functions

# Q11: Write a function that prints numbers from 1 to n using a loop.

nums = int(input("Enter a n: "))
def print_numbers(n):
    for i in range(1, n+1):
        print(i)
        
print_numbers(nums)

# Q12: Write a function that prints all even numbers from 1 to n.

nums = int(input("Enter a n: "))
def print_even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)
            
print_even_numbers(nums)

# 📂 Part 5: Nested Loops

# Q13: Print the following pattern using nested loops.
"""
*
**
***
****
*****
"""

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Q14: Print the multiplication table of a given number n using a loop.
# def multiplication_table(n):
#     # Write loop here
# multiplication_table(5)  # Example: Should print 5x1=5 ... 5x10=50

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
multiplication_table(5)

# Q15: Create a multiplication table from 1 to 5 using nested loops.

for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()

# 📂 Part 6: Looping with range()

# Q16: Print numbers from 10 to 50, incrementing by 5 each time.
# for i in range(10, 51, 5):
#     # Write loop here

for i in range(10, 51, 5):
    print(i)

# Q17: Print numbers from 100 to 50, decrementing by 10 each time.
# for i in range(100, 49, -10):
#     # Write loop here

for i in range(100, 49, -10):
    print(i)

# 📂 Part 7: Loops with Lists & Tuples

# Q18: Print each item from the list ["apple", "banana", "cherry"] using a loop.
# fruits = ["apple", "banana", "cherry"]
# # Write loop here

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])

# Q19: Print each item from the tuple ("Python", "Java", "C++") using a loop.
# languages = ("Python", "Java", "C++")
# # Write loop here

languages = ("Python", "Java", "C++")
for i in range(len(languages)):
    print(languages[i])

# Q20: Use a loop to find the sum of all numbers in the list [10, 20, 30, 40, 50].
# numbers = [10, 20, 30, 40, 50]
# # Write loop here

numbers = [10, 20, 30, 40, 50]
sum = 0
for i in numbers:
    sum += i
print(sum)


# 📂 Part 8: Special Problems

# Q21: Count the number of vowels in the string "loops are fun".
# string = "loops are fun"
# # Write loop here

string = "loops are fun"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(count)

# Q22: Reverse the string "Python" using a loop.
# word = "Python"
# # Write loop here

word = "Python"
reverse = ""
for i in word:
    reverse = i + reverse
print(reverse)

# Q23: Find the factorial of a number using a loop.
# def factorial(n):
#     # Write loop here
# print(factorial(5))  # Example: Output should be 120 (5! = 5x4x3x2x1)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(5))

# Q24: Check if a number is prime using a loop.
# def is_prime(n):
#     # Write loop here
# print(is_prime(7))  # Example: Should return True
# print(is_prime(10)) # Example: Should return False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))

# Q25: Print numbers from 1 to 50, but for multiples of 3 print "Fizz", 
# for multiples of 5 print "Buzz", and for multiples of both 3 and 5 print "FizzBuzz".
# Write your code here

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} is FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} is Fizz")
    elif i % 5 == 0:
        print(f"{i} is Buzz")
    else:
        print(f"{i} is Nothing")