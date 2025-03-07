#Objective
#####Create a Python program that analyzes a given text file or user input.

'''Features
Count the number of words, characters, and lines.
'''

'''
Identify whether the text contains any numbers.
Replace a specific word with another word.'''


#Implementation Plan
'''Take input (either from a text file or user input).
Use string methods (split(), count(), replace(), isdigit()) to analyze the text.
Use regex to extract numbers and check word patterns.
Display results in a readable format.
'''

import re

a = input("Enter the text: ")

def analyzer(a):
    words = a.split()
    char_count = len(a)
    words_count = len(words)
    line_count = a.count('\n') + 1
    number = re.findall(r'\d+', a)
    print(f"Total Characters: {char_count}")
    print(f"Total words: {words_count}")
    print(f"Total line: {line_count}")
    print(f"Number found: {number}")

analyzer(a)

#Words replacement

old_word = input("enter the old word: ")
new_word = input("enter the new word: ")
updated_text = a.replace(old_word, new_word)
print(f"Updated test: {updated_text}")