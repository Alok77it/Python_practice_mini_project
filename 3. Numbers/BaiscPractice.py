# Arithmetic Operations
    #Write a Python script to perform addition, subtraction, multiplication, division, floor division, modulus, and exponentiation on two numbers.

a = int(input("First number:" ))
b = int(input("Second number: "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#Find Even or Odd
    #Write a function that takes an integer and returns whether it is even or odd.

num = int(input("Enter the number: " ))
if (num % 2 == 0 ):
    print ("even")
else:
    print("Odd")


#Number Conversion
    #Convert a given decimal number into binary, octal, and hexadecimal.

num = 10
print("This is binary: ",bin(num))
print("This is hexadecimals: ",hex(num))
print("This is octal: ",oct(num))


#Factorial Calculation
    #Write a function to compute the factorial of a number using a loop.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
 
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")


#Round a Float
    #Take a floating-point number and round it to two decimal places.

num = float(input("Enter the float number: "))
print(round(num, 2))


#Simple Interest Calculation
    #Write a program to calculate simple interest using the formula:
'''   SI = P x R x T 
     ----------------
           100
'''        

def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time period (in years): "))

SI = simple_interest(P, R, T)
print(f"Simple Interest = {SI}")




#Find Maximum and Minimum
    #Find the maximum and minimum of three numbers using the max() and min() functions.

a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
print(max(a, b, c))
print(min(a, b, c))