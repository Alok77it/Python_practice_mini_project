#📝 Basic Level

#1️⃣ Write a program to check if a number is positive, negative, or zero.

a = -1

if (a >= 0):
    print("positive")
elif (a == 0):
    print("zero")
else:
    print("negative")

#2️⃣ Take an integer input and check whether it is even or odd.

a = int(input("enter the number: "))
if (a % 2 == 0):
    print("even")
else:
    print("odd")


#3️⃣ Write a program to check if a person is eligible to vote (age ≥ 18).

alok = 19

if (alok >= 18):
    print("Eligible")
else:
    print("not eligible")

#4️⃣ Write a program to find the maximum of two numbers.

a = 2
b = 5

if (a > b):
    print(f" {a} is greater than {b}")
else:
    print(f"{b} is greater than {a} ")

#5️⃣ Write a program to determine if a number is divisible by 5.

a = int(input("enter the number: "))
if (a % 5 == 0):
    print(f"{a} is divisble from 5")
else:
    print(f"{a} is not divisible from 5")

#6️⃣ Write a program to find the largest among three numbers.

a = 1
b = 34
c = 100

if (a > b and a > c):
    print(f"{a} is a greater number")
elif (b > a and b > c):
    print(f"{b} is a greater number")
else:
    print(f"{c} is a greater number")

#7️⃣ Check whether a number is divisible by both 5 and 11.

a = 121

if (a % 5 == 0 and a % 11 == 0):
    print(f"{a} is divisible by 5 and 11")
elif (a % 11 == 0 ):
    print(f"{a} is only divisble by 11")
elif (a % 5 == 0 ):
    print(f"{a} is only divisble by 5")
else:
    print(f"{a} is not divisble by 5 and 11")


#8️⃣ Write a program to determine if a year is a leap year.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#9️⃣ Check whether a given character is a vowel or consonant.

character = "a"

if character in "aiefbrh1":
    print("vowel")
else:
    print("consonant")

#🔟 Write a program to check whether a given number is prime or not.

        