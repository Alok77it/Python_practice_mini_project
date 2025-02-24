#Use .join() to convert a list ["apple", "banana", "cherry"] into "apple, banana, cherry".

s1 = ["apple", "banana", "cherry"]

print(" ".join(s1))


#Extract all numbers from "The price is 500 and discount is 50" using regex.
import re

text = "The price is 500 and discount is 50"

digits = re.findall(r'\d+', text)
print(digits)

#Encode the string "Hello World" into UTF-8 and decode it back.

s1 = "Hello World"
encoded_s1 = s1.encode("utf-8")
print(encoded_s1)
print(encoded_s1.decode("utf-8")) 

#Use .partition() to split "Python is amazing" at "is".

s1 = "Python is amazing"

print(s1.partition("is"))