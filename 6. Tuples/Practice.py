# Exercises: Level 1

# 1. Create an empty tuple
empty = ()

# 2. Create a tuple containing names of your sisters and brothers
brother = ("aniket", "siddharth", "saurabh")
sister = ("priya", "priyanka")

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brother + sister
print(siblings)

# 4. How many siblings do you have?
siblings_count = len(siblings)
print(siblings_count)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append("father")
siblings.append("mother")
family_members = tuple(siblings)
print(family_members)

# Exercises: Level 2

# 1. Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print(siblings)

# 2. Create fruits, vegetables, and animal products tuples. Join the three tuples and assign them to a variable called food_stuff_tp.
fruits = ("banana", "orange", "mango")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "cheese", "yogurt")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp[len(food_stuff_tp)//2])
print(food_stuff_lt[len(food_stuff_lt)//2])

# 5. Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# 6. Delete the food_stuff_tp tuple completely
food_stuff_tp.clear()
print(food_stuff_tp)

# 7. Check if 'Estonia' is a Nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
is_estonia = "Estonia" in nordic_countries
print(is_estonia)

# 8. Check if 'Iceland' is a Nordic country
is_iceland = "Iceland" in nordic_countries
print(is_iceland)

# Exercises: Level 3

# 1. Create a tuple of 5 elements and access them using index.
tuple1 = (10, 20, 30, 40, 50)
print("Tuple elements:", tuple1)
print("Accessed element at index 2:", tuple1[2])

# 2. Convert a list to a tuple.
list1 = [1, 2, 3, 4, 5]
tuple2 = tuple(list1)
print("Converted tuple:", tuple2)

# 3. Find the length of a tuple.
print("Length of tuple1:", len(tuple1))

# 4. Count occurrences of an item.
print("Occurrences of 20 in tuple1:", tuple1.count(20))

# 5. Find index of an item.
print("Index of 30 in tuple1:", tuple1.index(30))

# 6. Slice a tuple.
sliced_tuple = tuple1[1:4]
print("Sliced tuple (index 1 to 3):", sliced_tuple)

# 7. Check if an item exists in a tuple.
item = 40
print(f"Does {item} exist in tuple1?", item in tuple1)

# 8. Concatenate two tuples.
tuple3 = (60, 70, 80)
concatenated_tuple = tuple1 + tuple3
print("Concatenated tuple:", concatenated_tuple)

# 9. Unpack a tuple into variables.
a, b, c, d, e = tuple1
print("Unpacked values:", a, b, c, d, e)

# 10. Use tuple as a key in a dictionary.
tuple_key = (1, 2, 3)
dict_with_tuple_key = {tuple_key: "Tuple as key example"}
print("Dictionary with tuple as key:", dict_with_tuple_key)
