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
