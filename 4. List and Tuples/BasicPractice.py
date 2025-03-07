#Create and Access Elements:
    #Create a list of 5 numbers and print each number.

numlist = [1, 2, 3, 4, 5]
print(numlist[0])
print(numlist[1])
print(numlist[2])
print(numlist[3])
print(numlist[4])

#List Modification:
    #Replace the second element of a list with a new value.

newvalue = input("Enter new value: ")
numlist.pop(1)
numlist.insert(1, newvalue)
print(numlist)

#Append and Insert Elements:
    #Append a new element at the end of a list.
    #Insert an element at index 2.

numlist.append(6)
numlist.insert(2, 9)
print(numlist)

#Remove Elements:
    #Remove an element by value.
    #Remove an element using pop().

numlist.remove(1)
numlist.pop(2)
print(numlist)

#List Slicing:
    #Print the first three elements of a list.
    #Print the last two elements of a list.

print(numlist[0:2])
print(numlist[-3:-1])

#Sum of List Elements:
    #Write a program to find the sum of all numbers in a list.
numlist = [1,2, 3, 4, 5]
total_sum = sum(numlist)
print(total_sum)


#Find Maximum and Minimum:
    #Write a program to find the maximum and minimum numbers in a list.

print(max(numlist))
print(min(numlist))

#Reverse a List:
    #Reverse a list using slicing and .reverse().

reversed_list_slicing = numlist[::-1]
print(reversed_list_slicing)

numlist.reverse()
print(numlist)

#Check Element Existence:
    #Check if a given number exists in a list.
print(numlist)
num_to_check = int(input("enter the number to check: "))
if num_to_check in numlist:
    print(f"{num_to_check} exists")
else:
    print(f"{num_to_check} not exists")

    #Count Element Occurrences:

    #Count how many times a specific number appears in a list.
num_to_count = int(input("enter the number: "))
count = numlist.count(num_to_count)
print(f"{num_to_count} appears {count}")


#Create and Access Elements:
    #Create a tuple with 5 elements and print each element using indexing.

new_tuple = (1, 2, 3, 4, 5)
print(new_tuple.index(1))
print(new_tuple.index(2))
print(new_tuple.index(3))
print(new_tuple.index(4))
print(new_tuple.index(5))

#Tuple Slicing:
    #Print the first three elements of a tuple.
    #Print the last two elements of a tuple.

print(new_tuple[0:2])
print(new_tuple[-2:])


#Tuple Unpacking:
    #Assign a tuple (10, 20, 30) to three variables and print them separately.

tuple_new = (10, 20, 30)
a, b, c = tuple_new
print(a)
print(b)
print(c)

#Check Element Existence:
    #Write a program to check if a given element exists in a tuple.

print(10 in tuple_new)

#Count Occurrences:
    #Given a tuple (1, 2, 3, 2, 4, 2), count how many times 2 appears.

new_tuple = (1, 2, 3, 4, 5, 3, 2, 3, 2)
print(new_tuple.count(2))

#Find Index of an Element:
    #Find the index of the first occurrence of 5 in the tuple (3, 5, 7, 5, 9).

example_tuple = (3, 5, 7, 5, 9)
index_of_5 = example_tuple.index(5)
print("The index of the first occurrence of 5 is:", index_of_5)

#Convert List to Tuple:
    #Convert a list [5, 10, 15, 20] into a tuple.

listnum = [5, 10, 11, 15]
numtuple = tuple(listnum)
print(numtuple)


#Tuple Concatenation:
    #Concatenate two tuples (1, 2, 3) and (4, 5, 6).

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)


#Tuple Repetition:
    #Repeat a tuple (‘Python’,) three times.

a = ('python',)
b = a * 3
print(b)

#Tuple to String:

    #Convert a tuple of characters ('H', 'e', 'l', 'l', 'o') into a string

a = ('h', 'e', 'l', 'l', 'o')
b = ''.join(a)
print(b)

