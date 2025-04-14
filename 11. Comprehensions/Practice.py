# 🧠 Python Comprehensions – Practice Set (20 Questions)

# 🔹 Part 1: List Comprehensions (1–10)

# 1. Create a list of squares for numbers from 1 to 10 using list comprehension.
squares = [x ** 2 for x in range(10)]
print(squares)

# 2. Create a list of even numbers from 0 to 20 using list comprehension.
even =[x for x in range(21) if x % 2 == 0]
print(even)

# 3. Convert a list of lowercase strings to uppercase using list comprehension.
lowercase = ["apple", "banana", "cherry", "date"]
uppercase = [word.upper() for word in lowercase]
print(uppercase)

# 4. Extract numbers greater than 50 from a list using list comprehension.
greater = [23, 45, 67, 89, 75, 66, 707]
num = [x for x in greater if x > 50]
print(num)

# 5. Generate a list of strings like "Item 1", "Item 2", ..., "Item 10" using list comprehension.
items = [f"Item {i}" for i in range(1, 11)]
print(items)

# 6. Flatten a 2D list like [[1,2], [3,4]] into [1, 2, 3, 4] using list comprehension.
nested_list = [[1,2],[3, 4]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)

# 7. From a list of strings, create a list of string lengths using list comprehension.
string = ["apple", "banana", "cherry", "date"]
length = [len(word) for word in string]
print(length)

# 8. Use list comprehension to replace negative numbers in a list with 0.
numbers = [10, -5, 20, -15, 30, -25]
replaced = [x if x >= 0 else 0 for x in numbers]
print(replaced)

# 9. Extract vowels from a given string using list comprehension.
text = "Hello, World!"
vowels = [char for char in text if char.lower() in "aeiou"]
print(vowels)

# 10. Given a sentence, make a list of words that start with a capital letter using list comprehension.
sentence = "Python is Fun and Easy to Learn."
capital_words = [word for word in sentence.split() if word[0].isupper()]
print(capital_words)
