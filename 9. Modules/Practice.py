'''Exercises Level 1'''

#1.Write a function which generates a six digit/character random_user_id.

import random
import string

def generate_user_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

print(generate_user_id())

#2. Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters: "))
    num_ids = int(input("Enter the number of IDs: "))
    for i in range(num_ids):
        print(''.join(random.choices(string.ascii_lowercase + string.digits, k=num_chars)))

print(user_id_gen_by_user())

#3.Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

print(rgb_color_gen())

'''Exercises Level 2'''

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #.
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. 
# Check the task 6 for output examples).
#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
#Write a function generate_colors which can generate any number of hexa or rgb colors.

def list_of_hexa_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(color)
    return colors

def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        colors.append(color)
    return colors
def generate_colors(num_colors, color_type='hexa'):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return 'Invalid color type'
    
print(generate_colors(3, 'hexa'))
print(generate_colors(3, 'rgb'))
print(generate_colors(3, 'cmyk'))

'''Exercises Level 3'''

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique.

def shuffle_list(lst):
    return random.sample(lst, len(lst))

def random_numbers():
    numbers = list(range(10))
    return shuffle_list(numbers)

print(random_numbers())