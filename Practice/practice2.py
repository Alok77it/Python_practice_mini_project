name = "ALok"

nameshort = name[0:2] #start from 0 and go upto 2

print(nameshort)


print(name[-4:-1])

s1 = "Alok"

s2 = "Trivedi"

s3 = s1 + " " + s2

print(s3.lower())
print(s3.upper())
print(s3.strip())
print(s3.replace("Alok", "Python"))
print(s3.split())

s = "hello world"

print(s.capitalize())  # 'Hello world'
print(s.title())       # 'Hello World'
print(s.count('l'))    # 3 (Count occurrences of 'l')
print(s.startswith('hello'))  # True
print(s.endswith('d'))        # True
print(s.find('world'))        # 6 (Index where 'world' starts)
print(s.index('o'))           # 4 (First occurrence of 'o')
