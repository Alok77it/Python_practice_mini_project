


# Python Sets Practice Problems (Basic to Intermediate)

# 1️⃣ Create a Set and Print It
# Create a set with {1, 2, 3, 4, 5} and print it.

set_name = {1, 2, 3, 4, 5}
print(set_name)

# 2️⃣ Add Elements to a Set
# Add elements 6 and 7 to the set {1, 2, 3, 4, 5}.

set_name.add(6)
set_name.add(7)
print(set_name)

# 3️⃣ Remove an Element from a Set
# Remove 3 from the set {1, 2, 3, 4, 5} using remove() and discard().

set_name.remove(3)
set_name.discard(2)
print(set_name)

# 4️⃣ Check if an Element Exists in a Set
# Given {10, 20, 30, 40}, check if 25 and 30 exist in the set.

set_example = {10, 20, 30, 40, 50}

if 25 in set_example:
    print("25 exists in the set")
else:
    print("25 is not exist in the set")

# 5️⃣ Find the Length of a Set
# Given {1, 2, 3, 4, 5}, find the total number of elements using len().

print(len(set_example))

# 6️⃣ Convert a List to a Set (Remove Duplicates)
# Convert [1, 2, 2, 3, 4, 4, 5, 5] into a set to remove duplicates.

set_example = [1, 2, 3, 2, 4, 5, 5, ]
unique_set = set(set_example)
print(unique_set)

# 7️⃣ Iterate Over a Set
# Print all elements of {10, 20, 30, 40, 50} using a loop.

set_example = {10, 20, 30, 40, 50}
for i in set_example:
    print(i)

# 8️⃣ Find the Union of Two Sets
# Given:
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# Find the union of set1 and set2.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)

# 9️⃣ Find the Intersection of Two Sets
# Given:
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# Find common elements between set1 and set2.

print(set1.intersection(set2))

# 🔟 Find the Difference of Two Sets
# Given:
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# Find elements in set1 that are not in set2.

print(set1.difference(set2))

# 1️⃣1️⃣ Find the Symmetric Difference Between Two Sets
# Given:
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# Find elements that are in either set1 or set2, but not both.

print(set1.symmetric_difference(set2))

# 1️⃣2️⃣ Check if One Set is a Subset of Another
# Check if {2, 3} is a subset of {1, 2, 3, 4, 5}.

print(set1.issubset(set2))

# 1️⃣3️⃣ Check if One Set is a Superset of Another
# Check if {1, 2, 3, 4, 5} is a superset of {3, 4}.

print(set1.issuperset(set2))

# 1️⃣4️⃣ Remove Common Elements Between Two Sets
# Remove elements that are common between {1, 2, 3, 4, 5} and {3, 4, 6, 7}.


print(set1.difference_update(set2))

# 1️⃣5️⃣ Find Unique Elements in a List Using a Set
# Given the list [1, 2, 2, 3, 4, 4, 5], find the unique elements using a set.

list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_elements_set = set(list_with_duplicates)
print("Unique elements in the list:", unique_elements_set)