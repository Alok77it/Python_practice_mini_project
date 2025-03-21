# 📌 Pattern Practice Set (Using Loops)

# 📂 Part 1: Basic Star Patterns

# Q1: Print the following pattern (Right-Angled Triangle)
"""
*
**
***
****
*****
"""
# Write your code here

for i in range(1, 6):
    print("*" * i)

# Q2: Print the following pattern (Inverted Right-Angled Triangle)
"""
*****
****
***
**
*
"""
# Write your code here

for i in range(5, 0, -1):
    print("*" * i)

# Q3: Print the following pattern (Square)
"""
*****
*****
*****
*****
*****
"""
# Write your code here

for i in range(5):
    print("*" * 5)

# 📂 Part 2: Number Patterns

# Q4: Print the following pattern
"""
1
12
123
1234
12345
"""
# Write your code here

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 📂 Part 3: Alphabet Patterns

# Q5: Print the following pattern
"""
A
AB
ABC
ABCD
ABCDE
"""
# Write your code here

for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end="")
    print()

#65: The ASCII value of the letter 'A'.
#70: The ASCII value of the letter 'F'. 

# 📂 Part 4: Pyramid Patterns

# Q6: Print the following pattern (Pyramid)
"""
    *
   ***
  *****
 *******
*********
"""
# Write your code here

for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
    print()

# 📂 Part 5: Hollow Patterns

# Q7: Print the following pattern (Hollow Square)
"""
*****
*   *
*   *
*   *
*****
"""
# Write your code here

for i in range(5):
    if i == 0 or i == 4:
        print("*" * 5)
    else:
        print("*" + " " * 3 + "*")
        print()
# 📂 Part 6: Advanced Patterns


# 📂 Part 7: Special Patterns

# Q9: Print the following pattern (Butterfly Pattern)
"""
*       *
**     **
***   ***
**** ****
*********
**** ****
***   ***
**     **
*       *
"""
# Write your code here

for i in range(1, 6):
    print("*" * i + " " * (5 - i) + "*" * i)
for i in range(4, 0, -1):
    print("*" * i + " " * (5 - i) + "*" * i)


# Q10: Print the following pattern (Zig-Zag Pattern)
"""
  *   *   *  
 * * * * * * 
*   *   *   *
"""
# Write your code here

