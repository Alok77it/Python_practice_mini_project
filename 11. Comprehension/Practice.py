# 🔹 List Comprehension Practice

# ✅ Basic
# 1. Create a list of squares of numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]
print(squares) 

# 2. Extract all even numbers from a list.
even = [x for x in range(1, 21) if x % 2 == 0]
print(even)

# 3. Convert a list of strings to uppercase.
str1 = ['hello', 'world', 'python']
uppercase = [s.upper() for s in str1]
print(uppercase)

# 4. Filter only words with more than 3 letters from a list.
words = ['hi', 'hello', 'world', 'python']
filter = [word for word in words if len(word) > 3]
print(filter)

