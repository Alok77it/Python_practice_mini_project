# Exercises: Level 1

# 1. Declare an empty list
empty = []

# 2. Declare a list with more than 5 items
list1 = []
list1.append('Apple')
list1.append('Banana')
list1.append('Orange')
list1.append('Grapes')
list1.append('Mango')
print(list1)

# 3. Find the length of your list
print(len(list1))   

# 4. Get the first item, the middle item, and the last item of the list
print(list1[0])
print(list1[len(list1)//2])
print(list1[-1])

# 5. Declare a list called mixed_data_types with (name, age, height, marital status, address)
mixed_data_types =["name", "age", "height", "marital status", "address"]

# 6. Declare a list variable named it_companies and assign initial values: 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list
print(mixed_data_types)
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle, and last company
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# 11. Add an IT company to it_companies
IT_cpmpany = 'Tesla'
it_companies.append(IT_cpmpany)
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
IT_company = 'Nvidia'
it_companies.insert(len(it_companies)//2, IT_company)
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
new_company = it_companies[0].upper()
print(new_company)

# 14. Join the it_companies with a string '#;  '
join_company = '#; '.join(it_companies)
print(join_company)

# 15. Check if a certain company exists in the it_companies list
if "Meta" in it_companies:
    print('Meta exists in the list')
else:
    print('Meta does not exist in the list')

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[0:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-1:-4:-1])

# 20. Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies)//2])

# 21. Remove the first IT company from the list
remove_first_company = it_companies.pop(0)
print(remove_first_company)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
remove_middle_company = it_companies.pop(len(it_companies)//2)
print(remove_middle_company)
print(it_companies)

# 23. Remove the last IT company from the list
remove_last_company = it_companies.pop()
print(remove_last_company)
print(it_companies)

# 24. Remove all IT companies from the list
remove_all_companies = it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies
try:
    print(it_companies)
except NameError:
    print("it_companies is not defined")
    
# 26. Join the following lists:
#     front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#     back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
new_list = front_end + back_end
print(new_list)

# 27. After joining the lists in question 26, copy the joined list and assign it to 
#     a variable full_stack, then insert Python and SQL after Redux.
full_stack = new_list.copy()
index_of_redux = full_stack.index('Redux')
full_stack.insert(index_of_redux + 1, 'Python')
full_stack.insert(index_of_redux + 2, 'SQL')
print(full_stack)

# Exercises: Level 2

# 1. The following is a list of 10 students' ages:
#    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 2. Sort the list and find the min and max age
ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)
print(f'Min age: {min_age}')
print(f'Max age: {max_age}')

# 3. Add the min age and the max age again to the list
min_age = min(min_age, max_age)
ages.append(min_age)
max_age = max(min_age, max_age)
ages.append(max_age)
print(ages) 

# 4. Find the median age (one middle item or two middle items divided by two)
ages.sort()
if len(ages) % 2 == 0:
    mid1 = len(ages) // 2
    mid2 = mid1 - 1
    median_age = (ages[mid1] + ages[mid2]) / 2
else:
    mid = len(ages) // 2
    median_age = ages[mid]
print(f'Median age: {median_age}')

# 5. Find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)
print(f'Average age: {average_age}')

# 6. Find the range of the ages (max minus min)
min_age = max(ages) - min(ages)
print(f'Range of ages: {min_age}')

# 7. Compare the value of (min - average) and (max - average), use abs() method
min_age = min(ages)
max_age = max(ages)
average_age = sum(ages) / len(ages)
diff_min = abs(min_age - average_age)
diff_max = abs(max_age - average_age)
print(f'Difference between min and average: {diff_min}')
print(f'Difference between max and average: {diff_max}')

# 8. Find the middle country(ies) in the countries list
countries = ["india", "USA", "China", "Russia", "Finland", "Sweden", "Norway", "Denmark"]
print(countries[len(countries)//2])

# 9. Divide the countries list into two equal lists if it is even, if not, 
#    one more country for the first half.
if len(countries) % 2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]
print(f'First half: {first_half}')
print(f'Second half: {second_half}')

