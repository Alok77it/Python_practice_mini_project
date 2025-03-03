#1️⃣ Create a Dictionary

    #Create a dictionary with keys: name, age, and city. Assign values to them and print the dictionary.

my_dict = {
    "name" : "Alok",
    "age" : 22,
    "skills" : ["python", "DevOps"]
}
print(my_dict)


#2️⃣ Accessing Dictionary Values

    #Given the dictionary:

    #student = {"name": "Alok", "age": 22, "course": "DevOps"}

    #Print the values of "name" and "course" using both [] and .get() methods.

student = {"name": "Alok", "age": 22, "course": "DevOps"}
print(student["name"])
print(student.get("age"))

#3️⃣ Updating Dictionary Values

    #Update the "age" key in the dictionary to 23.

student["age"] = 23
print(student)


#4️⃣ Adding a New Key-Value Pair

    #Add a new key "skills" with the value ["Python", "Kubernetes"].

student["skills"] = ["Python", "Kubernetes"]
print(student)

#5️⃣ Removing Elements

    #Remove the key "city" from the dictionary using pop().
student = {"name": "Alok", "age": 22, "course": "DevOps", "city": "Bangalore"}
student.pop("city")
print(student)

#6️⃣ Iterating Over a Dictionary

    #Write a program to iterate through a dictionary and print both keys and values.

student = {"name": "Alok", "age": 23, "course": "DevOps", "skills": ["Python", "Kubernetes"]}
for key, value in student.items():
    print(f"{key} : {value}")


#7️⃣ Check If a Key Exists

    #Write a function to check if "salary" exists in a dictionary.

def check_status(dictionary):
    if "salary" in dictionary:
        return True
    else:
        return False

student = {"name": "Alok", "age": 23, "course": "DevOps", "skills": ["Python", "Kubernetes"]}
print(check_status(student))

#8️⃣ Merging Two Dictionaries

    #Merge the following two dictionaries:

#dict1 = {"a": 1, "b": 2}
#dict2 = {"c": 3, "d": 4}

dic1 = {"a":1, "b":2}
dic2 = {"c":3, "d":4}
dic1.update(dic2)
print(dic1)

#9️⃣ Count Word Frequency

    #Write a program to count the frequency of words in a given sentence.
   # Example:

          #text = "python is fun and python is powerful"

#Output:

    #{"python": 2, "is": 2, "fun": 1, "and": 1, "powerful": 1}




#🔟 Find the Student with the Highest Marks

    #Given a dictionary of student names and their marks:

#students = {"Alok": 85, "Ravi": 92, "Priya": 78}




#1️⃣1️⃣ Invert a Dictionary
'''
    Given:

    my_dict = {"a": 1, "b": 2, "c": 3}

    Write a program to swap keys and values to get {1: "a", 2: "b", 3: "c"}.
'''
    
#1️⃣2️⃣ Sort a Dictionary by Value

    #Sort the given dictionary in ascending and descending order by values.

    #marks = {"Alice": 88, "Bob": 75, "Charlie": 92}

#1️⃣3️⃣ Nested Dictionary Access
'''
    Given:

    employee = {
        "name": "John",
        "department": {
            "name": "IT",
            "location": "Bangalore"
        }
    }

    Write a program to access "IT" and "Bangalore" from this dictionary.
'''
    

#1️⃣4️⃣ Remove Duplicates in a Dictionary (Values as List)
'''
    Given:

    data = {"a": [1, 2, 2, 3], "b": [4, 4, 5], "c": [6, 7, 7]}

    Remove duplicate numbers from the list values.
'''
    

#1️⃣5️⃣ Find Common Key-Value Pairs Between Two Dictionaries
'''
    Given:

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 4, "d": 5}
'''