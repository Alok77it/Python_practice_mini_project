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
