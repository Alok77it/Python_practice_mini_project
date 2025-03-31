# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string1 = "Thirty"
string2 = "Days"
string3 = "Of"
string4 = "Python"
full_string = string1 + " " + string2 + " " + string3 + " " + string4
print(full_string)

string5 = "Coding"
string6 = "For"
string7 = "All"
full_string2 = string5 + " " + string6 + " " + string7
print(full_string2)

# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
comapany = full_string2
print(comapany)
print(len(comapany))

# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
# Use capitalize(), title(), swapcase() methods to format the value of the string "Coding For All".
string1 = "coding for all"
string2 = "CODING FOR ALL"
string3 = "Coding For All"
print(string1.upper())
print(string2.lower())
print(string3.capitalize())
print(string3.title())
print(string3.swapcase())

# Cut(slice) out the first word of "Coding For All" string.
# Check if "Coding For All" string contains a word "Coding" using the method index, find or other methods.
string = "Coding For All"
first_word = string.split()[0]
print(first_word)

# Replace the word "Coding" in the string 'Coding For All' to "Python".
# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
string = "Coding For All"
string = string.replace("Coding", "Python")
print(string)
string = "Python for Everyone"
string = string.replace("Python for Everyone", "Python for All")
print(string)

# Split the string 'Coding For All' using space as the separator (split()).
# Split the string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the comma.
string = "Coding For All"
words = string.split()
print(words)
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
words = string.split(", ")
print(words)

# What is the character at index 0 in the string "Coding For All".
# What is the last index of the string "Coding For All".
# What character is at index 10 in "Coding For All" string.
str = "Coding For All"
print(str[0])  # First character
print(str[-1])  # Last character
print(str[10])  # Character at index 10

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
name1 = "Python For Everyone"
acronym1 = ''.join([word[0].upper() for word in name1.split()])
print(f"Acronym for '{name1}': {acronym1}")

name2 = "Coding For All"
acronym2 = ''.join([word[0].upper() for word in name2.split()])
print(f"Acronym for '{name2}': {acronym2}")

# Use index to determine the position of the first occurrence of 'C' in "Coding For All".
# Use index to determine the position of the first occurrence of 'F' in "Coding For All".
# Use rfind to determine the position of the last occurrence of 'l' in "Coding For All People".
name1 = 'Coding For All'
print(f"Index of 'C': {name1.index('C')}")
print(f"Index of 'F': {name1.index('F')}")
print(f"Index of 'l': {name1.rfind('l')}")

# Use index or find to find the position of the first occurrence of the word 'because' in the sentence:
name1 = 'You cannot end a sentence with because because because is a conjunction'
print(f"Index of 'because': {name1.index('because')}")

# Use rindex to find the position of the last occurrence of the word 'because' in the same sentence.
print(f"Index of 'because': {name1.rindex('because')}")

# Slice out the phrase 'because because because' in the sentence:
print(f"Slice: {name1[30:55]}")

# Does "Coding For All" start with a substring "Coding"?
# Does "Coding For All" end with a substring "coding"?
print(f"Does 'Coding For All' start with 'Coding'? {'Coding For All'.startswith('Coding')}")
print(f"Does 'Coding For All' end with 'coding'? {'Coding For All'.endswith('coding')}")

# Remove the left and right trailing spaces in the given string: '   Coding For All      '.
name = '   Coding For All      '
print(f"Original string: '{name}'")
print(f"String with spaces removed: '{name.strip()}'")

# The following list contains the names of some python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.
sting1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(f"Joining names with a hash: {'# '.join(sting1)}")

# Use the new line escape sequence to separate the following sentences:
string = "I am enjoying this challenge.\nI just wonder what is next."
print(string)

# Use a tab escape sequence to write the following lines:
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
# Using tab escape sequence to format the table
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

# Define the numbers
a = 8
b = 6

# Perform calculations and format the output
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # Format division result to 2 decimal places
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
