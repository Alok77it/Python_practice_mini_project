language = "Python"
lst = list(language)
print(lst)

lst = [i for i in language]
print(lst)

numbers = [i for i in range(11)]
print(numbers)

squares = [i * i for i in range(11)]
print(squares)

numbers = [(i, i * i) for i in range(11)]
print(numbers) # Error

even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

add_two_numbers = lambda a, b: a + b
print(add_two_numbers(3, 5))

print((lambda a, b: a + b)(3, 2))


def power(x):
    return lambda n: x ** n

cude = power(2)(3)
print(cude)