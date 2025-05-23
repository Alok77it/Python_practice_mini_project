# Create an empty dictionary called dog
dog = {}
print(dog)

# Add name, color, breed, legs, and age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, 
# marital status, skills, country, city, and address as keys for the dictionary
student = {
    "first_name" : 'John',
    "last_name" : 'Doe',
    "gender" : "Male",
    "age" : 20,
    "marital_status" : "Single",
    "skills" : ["Python", "Java", "C++"],
    "country" : "USA",
    "city" : "New York",
    "address" : "123 Main St"
}
print(student)
    
    
# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('JavaScript')
student['skills'].append('HTML')
print(student['skills'])

# Get the dictionary keys as a list
print(student.keys())  # Get the dictionary keys as a list

# Get the dictionary values as a list
print(student.values())  # Get the dictionary values as a list


# Change the dictionary to a list of tuples using the items() method
student_items = student.items()
print(student_items)

# Delete one of the items in the dictionary
student.pop('address')
print(student)

# Delete one of the dictionaries
student.clear()
print(student)
