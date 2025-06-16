# 1. Square Pattern
# ****
# ****
# ****
# ****
n = int(input())
for i in range(1, n):
  for j in range(1, n):
    print("*", end="")
  print()


# 2. Right-Angled Triangle
# *
# **
# ***
# ****
n = int(input())
for i in range(1, n):
  for j in range(1, i):
    print("*", end="")
  print()

# 3. Inverted Right-Angled Triangle
# ****
# ***
# **
# *
n = int(input())
for i in range(n, 0, -1):
  print("*" * i)


# 4. Right-Aligned Triangle
#    *
#   **
#  ***
# ****



# 5. Pyramid
#    *
#   ***
#  *****
# *******

n = int(input())
for i in range(1, n + 1):
  print(" " * (n - i), end="")
  print("*" * (2 * i - 1))

# 6. Inverted Pyramid
# *******
#  *****
#   ***
#    *

# 7. Increasing Numbers
# 1
# 12
# 123
# 1234

# 8. Repeated Row Numbers
# 1
# 22
# 333
# 4444

# 9. Number Pyramid
#    1
#   121
#  12321
# 1234321

# 10. Inverted Number Triangle
# 1234
# 123
# 12
# 1

# 11. Alphabet Triangle
# A
# AB
# ABC
# ABCD

# 12. Alphabet Pyramid
#    A
#   ABA
#  ABCBA
# ABCDCBA

# 13. Repeated Alphabets
# A
# BB
# CCC
# DDDD

# 14. Diamond Pattern
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# 15. Hollow Square
# *****
# *   *
# *   *
# *****

# 16. Hollow Right Triangle
# *
# **
# * *
# ****

# 17. Hollow Pyramid
#    *
#   * *
#  *   *
# *******

# 18. Hourglass
# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******
