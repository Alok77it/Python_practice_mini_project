# Creating a tuple
colors = ("red", "green", "blue")

# Accessing elements
print(colors[1])  # Output: green

# Tuple unpacking
a, b, c = colors
print(a, b, c)  # Output: red green blue

# Checking for an element
print("red" in colors)  # Output: True

# Finding index
print(colors.index("blue"))  # Output: 2

# Tuple concatenation
new_tuple = colors + ("yellow",)
print(new_tuple)  # Output: ('red', 'green', 'blue', 'yellow')

# Tuple with one element (Note the comma)
single_element_tuple = ("hello",)
print(type(single_element_tuple))  # Output: <class 'tuple'>
