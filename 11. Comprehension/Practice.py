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

# ✅ Intermediate
# 5. Get all numbers from 1 to 100 that are divisible by both 3 and 5.


# 6. Flatten a 2D list: [[1, 2], [3, 4], [5, 6]] → [1, 2, 3, 4, 5, 6].


# 7. Reverse each string in a list: ['hello', 'world'] → ['olleh', 'dlrow'].


# 8. Create a list of tuples where each tuple is (number, square): from 1 to 10.


# ✅ Advanced
# 9. From a string, extract all vowels using list comprehension.


# 10. Given a list of temperatures in Celsius, convert them to Fahrenheit.


# 🔸 Dictionary Comprehension Practice

# ✅ Basic
# 11. Create a dictionary where keys are numbers from 1 to 5 and values are their squares.


# 12. Swap keys and values in a dictionary.


# 13. Filter out dictionary items where the value is less than 50.


# ✅ Intermediate
# 14. Count the frequency of each character in the string "mississippi".


# 15. Create a dictionary of even numbers from 1 to 20 as keys and their cubes as values.


# 16. Merge two lists into a dictionary: keys = ['a', 'b'], values = [1, 2].


# ✅ Advanced
# 17. Invert a dictionary with duplicate values to group keys by value.
#     Example: {'a': 1, 'b': 2, 'c': 1} → {1: ['a', 'c'], 2: ['b']}


# 18. Given a dictionary of students and marks, filter those who scored > 75.


# 🔻 Generator Expression Practice

# ✅ Basic
# 19. Write a generator to produce squares of numbers from 1 to 10.


# 20. Create a generator to yield even numbers from a list.


# 21. Build a generator that yields words longer than 4 letters from a sentence.


# ✅ Intermediate
# 22. Use a generator to yield factorial of numbers from 1 to 5.


# 23. Given a list of prices, use a generator to apply 10% discount on each.


# 24. Write a generator that yields all prime numbers up to 50.


# ✅ Advanced
# 25. Write a generator that yields the Fibonacci sequence up to n terms.


# 26. From a huge list of numbers, yield only unique elements using a generator and a set.

