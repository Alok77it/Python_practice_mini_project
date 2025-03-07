#Create a string "Python is fun" and:

    #Print the first and last character.
    #Slice "Python" from the string.

s1 = "Python is fun"

print(s1[0])
print(s1[-1])

print(s1[0:6])



#Concatenate two strings "Hello" and "World" with a space in between.

s1 = "Hello"
s2 = "World"

print(s1 + " " + s2)

#Reverse the string "abcdef" using slicing.

s1 = "abcdef"

print(s1[::-1])


#Convert "hello world" to uppercase and "PYTHON" to lowercase.

s1 = "hello world"
s2 = "PYTHON"

print(s1.upper())
print(s2.lower())

#Count the occurrences of "l" in "hello world".

s1 = "hello world"
print(s1.count("l"))