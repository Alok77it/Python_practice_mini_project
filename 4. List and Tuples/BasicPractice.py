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