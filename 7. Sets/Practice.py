# Sets in Python

# Given sets:
# it_companies contains the names of major IT companies.
# A and B are sets of numbers.
# age is a list of ages with duplicate values.
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24, 22, 26, 24, 25, 24]

# Exercises: Level 1

# 1. Find the length of the set it_companies.
print(len(it_companies))

# 2. Add 'Twitter' to the set it_companies.
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once into the set it_companies.
it_companies.update(['Tesla', 'SpaceX', 'Netflix'])
print(it_companies)

# 4. Remove one company from the set it_companies.
it_companies.remove('Tesla')
print(it_companies)

# 5. Explain the difference between remove and discard.
it_companies.discard('SpaceX')  # discard does not raise an error if the item is not found
# remove raises a KeyError if the item is not found
print(it_companies)

# Exercises: Level 2

# 6. Join sets A and B.
# 7. Find the intersection of A and B.
# 8. Check if A is a subset of B.
# 9. Determine if A and B are disjoint sets.
# 10. Join A with B and B with A.
# 11. Find the symmetric difference between A and B.
# 12. Delete the sets completely.

# Exercises: Level 3

# 13. Convert the list of ages to a set and compare the length of the list and the set. Which one is bigger?
# 14. Explain the difference between the following data types: string, list, tuple, and set.
# 15. Count the number of unique words in the given sentence:
#     "I am a teacher and I love to inspire and teach people."
#     - Use the split() method and a set to get the unique words.
