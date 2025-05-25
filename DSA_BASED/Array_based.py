# Practice Coding Questions for Python Sets

# -------------------------------------------
# 1. Loops with Sets
# -------------------------------------------

# Q1: Given a set of numbers, print each element using a for loop.
lst = [10,20,30,40,50]
for ls in lst:
    print(ls)

# Q2: Given a set of strings, print all strings that start with the letter 'a'.
str = {"alok","aniket","amit","swati","anusha"}
for item in str:
    if item.startswith("a"):
        print(item)


# Q3: Iterate over a set and count how many elements are greater than 10.


# Q4: Create a set of your favorite fruits and print each fruit in uppercase.


# Q5: Given a set, print all elements except one specified element (use loop + condition).


# -------------------------------------------
# 2. Reverse (Conceptual)
# -------------------------------------------
# Note: Sets are unordered, so reversing doesn't apply directly.
# But you can convert to a list and reverse it.

# Q1: Convert a set to a list and print the reversed list.


# Q2: Given a set of integers, convert it to a list, reverse it, and print the result.


# Q3: Write a function that takes a set and returns a list with elements in reverse order.


# Q4: Explain in comments why sets cannot be reversed directly.


# Q5: Given a set, convert to a sorted list and then reverse the list before printing.


# -------------------------------------------
# 3. Indexing (Conceptual)
# -------------------------------------------
# Note: Sets do not support indexing because they are unordered.

# Q1: Explain in comments why sets cannot be indexed like lists.


# Q2: Write code to check if an element exists in a set (simulate search by "indexing").


# Q3: Convert a set to a list and access the 3rd element.


# Q4: Write a function that takes a set and returns the nth element after converting to a list.


# Q5: Given a set, try accessing an element by index and catch the error.


# -------------------------------------------
# 4. Pass by Reference
# -------------------------------------------

# Q1: Write a function that adds an element to a set passed as an argument.
#     Call the function and show that the original set is updated (pass by reference).


# Q2: Write a function that tries to reassign a new set to the argument and observe if original set changes.


# Q3: Write a function that removes an element from the set passed to it.


# Q4: Explain in comments how passing a set to a function behaves in Python.


# Q5: Write a function that clears all elements from a set passed to it.


# -------------------------------------------
# 5. Linear Search in Sets
# -------------------------------------------

# Q1: Write a function that searches for an element in a set and returns True if found, else False.


# Q2: Write a function that checks if any element in a set is divisible by 5 using linear search.


# Q3: Given a set, search for a string ignoring case sensitivity (convert elements to lower case).


# Q4: Write code that performs linear search on a set of numbers to find the largest element.


# Q5: Write a function to count how many times an element appears in a set (hint: sets don't have duplicates).


