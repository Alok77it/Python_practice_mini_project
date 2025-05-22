# 1. Create a class called `Book` with attributes: title, author, and pages.
#    - Initialize them using a constructor.
#    - Create an object and print the details using a custom __str__() method.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Total pages: {self.pages}"

b = Book("Welcome", "Alok", 22)
print(b)


# 2. Create a class `Rectangle` with attributes: length and width.
#    - Add a method to calculate the area.
#    - Create two objects and compare which one has a larger area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def __ge__(self, other):
        return self.area() >= self.area()
        
obj1 = Rectangle(22, 23)
obj2 = Rectangle(45, 23)


if obj1 >= obj2:
    print("Obj1 have larger area than obj2")
else:
    print("Obj2 have larger area")
    


# 3. Create a class `Employee` with name and salary.
#    - Add a method to display details.
#    - Demonstrate the use of `self` clearly by printing object's id.

# Your code here


# 4. Create a class `ComplexNumber` with real and imaginary parts.
#    - Implement magic methods: __add__, __sub__, __mul__, and __str__ to operate on two complex numbers.

# Your code here


# 5. Create a class `Student` with default age = 18.
#    - Accept name and optional age from the user (via constructor).
#    - Print name and age using a method.

# Your code here


# 6. Create a class `BankAccount` with private variable `__balance`.
#    - Add deposit and withdraw methods with validation.
#    - Print balance using a method.

# Your code here


# 7. Create a class `Laptop` with brand and price.
#    - Add a discount method that applies a discount percent (method overloading using default argument).

# Your code here


# 8. Create a class `Point` to represent coordinates x and y.
#    - Implement __str__ and __truediv__ to divide coordinates of one point by another (with validation for zero).

# Your code here


# 9. Create a base class `Vehicle` with method start_engine().
#    - Create a derived class `Car` that overrides start_engine() to show car-specific behavior.
#    - Demonstrate both methods using objects.

# Your code here


# 10. Create a class `Matrix` with a 2D list as data.
#     - Implement __add__ and __str__ to support addition and printing of matrix.
#     - Ensure both matrices are same size for addition.

# Your code here
