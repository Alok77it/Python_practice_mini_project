# Exercises: Level 1

# 1. Get user input for age and determine if they are old enough to drive.
#    - If age is 18 or older, print "You are old enough to learn to drive."
#    - If age is below 18, print how many years are left until they can drive.
age = int(input("enter the age you want to drive: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    remaining_years = 18 - age
    print(f"You are {remaining_years} years old. You need to wait {remaining_years} more years to learn to drive.")

# 2. Compare the user's age with a predefined age (my_age).
#    - Print who is older.
#    - Use "year" if the difference is 1, otherwise use "years".
#    - If ages are the same, print a custom message.
my_age = 25
user_age = int(input("Enter your age: "))
if user_age > my_age:
    age_difference = user_age - my_age
    if age_difference == 1:
        print(f"You are {age_difference} year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")
elif user_age < my_age:
    age_difference = my_age - user_age
    if age_difference == 1:
        print(f"I am {age_difference} year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
else:
    print("We are the same age.")

# 3. Get two numbers from the user and compare them.
#    - Print if the first number is greater, smaller, or equal to the second number.
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
if first_number > second_number:
    print("The first number is greater than the second number.")
elif first_number < second_number:
    print("The first number is smaller than the second number.")
else:
    print("The first number is equal to the second number.")

# Exercises: Level 2

# 1. Assign grades based on user input score.
#    - 80-100: A
#    - 70-79: B
#    - 60-69: C
#    - 50-59: D
#    - 0-49: F
grade_score = int(input("Enter your score: "))
if grade_score >= 80 and grade_score <= 100:
    print("Grade: A")
elif grade_score >= 70 and grade_score < 80:
    print("Grade: B")
elif grade_score >= 60 and grade_score < 70:
    print("Grade: C")
elif grade_score >= 50 and grade_score < 60:
    print("Grade: D")
elif grade_score >= 0 and grade_score < 50:
    print("Grade: F")
else:
    print("Invalid score. Please enter a score between 0 and 100.")


# 2. Determine the season based on user input month.
#    - September, October, November: Autumn
#    - December, January, February: Winter
#    - March, April, May: Spring
#    - June, July, August: Summer
month = input("Enter a month: ").strip().lower()
if month.lower() in ["september", "october", "november"]:
    print("Season: Autumn")
elif month.lower() in ["december", "january", "february"]:
    print("Season: Winter")
elif month.lower() in ["march", "april", "may"]:
    print("Season: Spring")
elif month.lower() in ["june", "july", "august"]:
    print("Season: Summer")
else:
    print("Invalid month. Please enter a month between September and August.")
 
# 3. Check if a fruit exists in a given list.
#    - If it exists, print "That fruit already exists in the list."
#    - If not, add it to the list and print the updated list.
fruit_list = ["banana", "orange", "mango", "lemon"]
if "apple" in fruit_list:
    print("That fruit already exists in the list.")
else:
    fruit_list.append("apple")
    print("Fruit added to the list.")
print("Updated fruit list:", fruit_list)

# Exercises: Level 3

# 1. Given a dictionary containing personal information:
#    - Check if the "skills" key exists.

personal_information = dict(
    first_name='Asabeneh',
    last_name='Yetayeh',
    age=250,
    country='Finland',
    city='Helsinki',
    skills=['HTML', 'CSS', 'JavaScript', 'React', 'Node', 'Python', 'MongoDB'],
    is_married=True,
    job_title='Instructor'
)
if "skills" in personal_information:
    find_skill = input("Please enter the skill you want to check: ")
    if find_skill in personal_information["skills"]:
        print(f"{find_skill} is a skill in Asabeneh Yetayeh's personal information.")
    else:
        print(f"{find_skill} is not a skill in Asabeneh Yetayeh's personal information.")

# 2. Determine the person's role based on their skills:
#    - If only JavaScript and React, print "He is a front-end developer."
#    - If Node, Python, and MongoDB, print "He is a back-end developer."
#    - If React, Node, and MongoDB, print "He is a full-stack developer."
#    - Otherwise, print "Unknown title."
if "Javascript" in personal_information["skills"] and "React" in personal_information["skills"]:
    print("He is a front-end developer.")
elif "Node" in personal_information["skills"] and "Python" in personal_information["skills"] and "MongoDB" in personal_information["skills"]:
    print("He is a back-end developer.")
elif "React" in personal_information["skills"] and "Node" in personal_information["skills"] and "MongoDB" in personal_information["skills"]:
    print("He is a full-stack developer.")
else:
    print("Unknown title.")


# 3. If the person is married and lives in Finland, print:
#    "Asabeneh Yetayeh lives in Finland. He is married."

if personal_information["is_married"] and personal_information["country"] == "Finland":
    print(f"{personal_information['first_name']} {personal_information['last_name']} lives in {personal_information['country']}. He is married.")

