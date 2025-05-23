rows = 4
cols = 4
for i in range(rows):
    for j in range(1, cols+1):
        print(j, end = " ")
    print()
    
rows = 4
cols = 4
for i in range(rows):
    for j in range(cols):
        print("*", end = " ")
    print()
    
n = 4
for i in range(n):
    for j in range(65, 65 + n):
        print(chr(j), end = " ")
    print()
    
n =4
for i in range(1, n + 1):
    for j in range(i):
        print("*", end= " ")
    print()

n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
n = 4
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
    
n = 4
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    
rows = 4
nums = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(nums, end=" ")
        nums += 1
    print()
    
rows = 4
for i in range(1, rows + 1):
    print(" " * (i - 1), end="")
    for j in range(rows - i + 1):
        print(i, end="")
    print()
    
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i), end=" ")
    
    for j in range(1, i + 1):
        print(j, end="")
    
    for j in range(i - 1, 0, -1 ):
        print(j, end="")
    print()
    
n = 5

# Upper half
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Print stars and spaces
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Print stars and spaces
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = 5

# Upper half
for i in range(1, n + 1):
    print("*" * i, end="")            # Left wing stars
    print(" " * (2 * (n - i)), end="") # Spaces between wings
    print("*" * i)                    # Right wing stars

# Lower half
for i in range(n, 0, -1):
    print("*" * i, end="")            # Left wing stars
    print(" " * (2 * (n - i)), end="") # Spaces between wings
    print("*" * i)                    # Right wing stars
