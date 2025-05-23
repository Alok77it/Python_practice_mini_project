# Pattern Practice Set - Python

# Q1. Print a right-angled triangle of stars
# Example:
# *
# **
# ***
# ****
# *****

n = 4
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Q2. Print an inverted right-angled triangle of stars
# Example:
# *****
# ****
# ***
# **
# *

n = 5
for i in range(n, 0, -1):
    print("*" * i)

# Q3. Print a right-angled triangle with numbers
# Example:
# 1
# 12
# 123
# 1234
# 12345

rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Q4. Print Floyd's triangle
# Example:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

rows = 4
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Q5. Print a pyramid pattern with stars
# Example:
#     *
#    ***
#   *****
#  *******
# *********

rows = 4

for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")

    # Print ascending numbers from 1 to i
    for j in range(1, i + 1):
        print("*", end="")

    # Print descending numbers from i-1 to 1
    for j in range(i - 1, 0, -1):
        print("*", end="")

    print()  # New line after each row

