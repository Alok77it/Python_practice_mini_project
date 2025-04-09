# Exercises: Level 1

# 1. Iterate from 0 to 10 using a for loop
for i in range(11):
    print(i)

# 2. Iterate from 0 to 10 using a while loop
while i <= 10:
    print(i)
    i += 1

# 3. Iterate from 10 to 0 using a for loop
for i in range(10, -1, -1):
    print(i)

# 4. Iterate from 10 to 0 using a while loop
i = 10
while i >= 0:
    print(i)
    i -= 1


# 5. Write a loop that makes seven calls to print(), so the output forms the following triangle:
# #
# ##
# ###
# ####
# #####
# ######
# #######
for i in range(1, 8):
    print('#' * i)

# 6. Use nested loops to create the following 8x8 pattern:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# 7. Print the following multiplication pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 8. Iterate through the list ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out each item
list_name = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in list_name:
    print(item)

# 9. Use a for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)

# 10. Use a for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i)

# Exercises: Level 2

# 1. Use a for loop to iterate from 0 to 100 and print the sum of all numbers
# Expected output: The sum of all numbers is 5050.
for i in range(101):
    sum_of_numbers = sum(range(101))
print(f"The sum of all numbers is {sum_of_numbers}")

# 2. Use a for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds
# Expected output: The sum of all evens is 2550. And the sum of all odds is 2500.
for i in range(101):
    if i % 2 == 0:
        sum_of_evens = sum(range(0, 101, 2))
    else:
        sum_of_odds = sum(range(1, 101, 2))
print(f"The sum of all evens is {sum_of_evens}. And the sum of all odds is {sum_of_odds}.")

# Exercises: Level 3

# 1. Go to the data folder and use the countries.py file.
# Loop through the countries and extract all the countries containing the word 'land'.


# 2. Given the fruit list ['banana', 'orange', 'mango', 'lemon'], reverse the order using a loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)
print(reversed_fruits)