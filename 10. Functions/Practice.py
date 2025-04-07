# Exercises: Level 1

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"The sum of {a} and {b} is: {add_two_numbers(a, b)}")

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    return pi * r * r
radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle with radius {radius} is: {area_of_circle(radius)}")

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
#    Check if all the list items are number types. If not do give a reasonable feedback.

#    Check if all the list items are number types. If not do give a reasonable feedback.


# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
def convert_c_to_f(c):
    return (c * 9/5) + 32
celsius = float(input("Enter the celsius temperature:"))

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return "Invalid month"
name_month = input("Enter the month: ")
print(f"The season for the month {name_month} is: {check_season(name_month)}")    


# 6. Write a function called calculate_slope which return the slope of a linear equation.
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined"
    else:
        return (y2 - y1) / (x2 - x1)
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
print(f"The slope of the line through points ({x1}, {y1}) and ({x2}, {y2}) is: {calculate_slope(x1, y1, x2, y2)}")

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. 
#    Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c, x):
    return a*x**2 + b*x + c
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
x = float(input("Enter x: "))
print(f"The solution of the quadratic equation {a}x² + {b}x + {c} = 0 at x = {x} is: {solve_quadratic_eqn(a, b, c, x)}")

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
list_items = [1, 2, 3, 4, 5]
def print_list(lst):
    for item in lst:
        print(item)
print_list(list_items)

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
#    print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
#    print(reverse_list(["A", "B", "C"]))  # ["C", "B", "A"]


# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items.
def capitalize_list_items(list):
    return [item.capitalize() for item in list]

'''It will take your print output as a item then 
create a new list with capitalized items
if you use set as i used there so they take items form set
convert it to list then capitalize it'''

print(capitalize_list_items({'apple', 'banana', 'cherry'})) 

# 11. Declare a function named add_item. It takes a list and an item as parameters. 
#     It returns a list with the item added at the end.
#     food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#     print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
#     numbers = [2, 3, 7, 9]
#     print(add_item(numbers, 5))          # [2, 3, 7, 9, 5]
def add_item(lst, item):
    lst.append(item)
    return [lst]
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))


# 12. Declare a function named remove_item. It takes a list and an item as parameters. 
#     It returns a list with the item removed from it.
#     food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#     print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
#     numbers = [2, 3, 7, 9]
#     print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
#     print(sum_of_numbers(5))   # 15
#     print(sum_of_numbers(10))  # 55
#     print(sum_of_numbers(100)) # 5050
print(5)   # 15

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.


# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.


# Exercises: Level 2

# 1. Declare a function named evens_and_odds. It takes a positive integer as parameter and it counts number of evens and odds in the number.
#    print(evens_and_odds(100))
#    # The number of odds are 50.
#    # The number of evens are 51.


# 2. Call your function factorial. It takes a whole number as a parameter and it returns the factorial of the number.


# 3. Call your function is_empty. It takes a parameter and it checks if it is empty or not.


# 4. Write different functions which take lists. They should:
#    - calculate_mean
#    - calculate_median
#    - calculate_mode
#    - calculate_range
#    - calculate_variance
#    - calculate_std (standard deviation)


# Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.


# 2. Write a function which checks if all items are unique in the list.


# 3. Write a function which checks if all the items of the list are of the same data type.


# 4. Write a function which checks if the provided variable is a valid Python variable.


# 5. Go to the data folder and access the countries-data.py file.


# 6. Create a function called the_most_spoken_languages in the world. 
#    It should return 10 or 20 most spoken languages in the world in descending order.


# 7. Create a function called the_most_populated_countries. 
#    It should return 10 or 20 most populated countries in descending order.
