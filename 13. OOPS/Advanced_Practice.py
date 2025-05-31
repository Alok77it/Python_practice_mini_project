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

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_details(self):
        print(f"Employee name: {self.name}")
        print(f"Salary: {self.salary}")
        
obj = Employee("Alok", 2300)
obj.display_details()


# 4. Create a class `ComplexNumber` with real and imaginary parts.
#    - Implement magic methods: __add__, __sub__and __str__ to operate on two complex numbers.

class ComplexNumber:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, -2)


print("c1 + c2 =", c1 + c2)
print("c1 - c2 =", c1 - c2)


# 5. Create a class `Student` with default age = 18.
#    - Accept name and age from the user (via constructor).
#    - Print name and age using a method.
name = input("Enter the name: ")
age = int(input("Enter the age: "))
if age > 18:
    class Student:
        def __init__(self,name,age):
            self.name = name
            self.age = age
        
        def printDetails(self):
            print(f"Name: {self.name}, Age: {self.age}")
    
    s1 = Student(name, age)
    s2 = Student(name, age)

else:
    print("Invalid age")
        
        

# 6. Create a class `BankAccount` with private variable `__balance`.
#    - Add deposit and withdraw methods with validation.
#    - Print balance using a method.

class BankAccount:
    def __init__(self,initial_balance=0):
        self.__balance = initial_balance
        
    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
        else:
            print("Enter the amount more than zero")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Enter the amount more than zero")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            
    def print_balance(self):
        print(f"Current Balance: ₹{self.__balance}")

account = BankAccount(1000)
account.deposit(500)         # Deposit ₹500
account.withdraw(300)        # Withdraw ₹300
account.print_balance()

           # Accessing private (not recommended, just to show it exists):
print(account._BankAccount__balance)  # Output: 1200
    
# 7. Create a class `Laptop` with brand and price.
#    - Add a discount method that applies a discount percent (method overloading using default argument).

class Laptop:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    
    def discount_percent(self,discount = 10):
        discount_price = self.price - (self.price * discount / 100)
        print(f"Price after {discount}% discount: {discount_price}")
        
item = Laptop("Dell", 50000)
item.discount_percent()
item.discount_percent(20)


# 8. Create a class `Point` to represent coordinates x and y.
#    - Implement __str__ and __truediv__ to divide coordinates of one point by another (with validation for zero).

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __truediv__(self,other):
        if other.x == 0 or other.y == 0:
            raise ZeroDivisionError("Cannot divide by zero in coordinates.")
        new_x = self.x / other.x
        new_y = self.y / other.y
        return Point(new_x,new_y)
    
p1 = Point(10, 20)
p2 = Point(2, 4)
result = p1 / p2
print("Result:", result) 



# 9. Create a base class `Vehicle` with method start_engine().
#    - Create a derived class `Car` that overrides start_engine() to show car-specific behavior.
#    - Demonstrate both methods using objects.

class Vehicle:
    def start_engine(self):
        print("Engine Started")
        
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

v1 = Vehicle()
v1.start_engine()

c1 = Car()
c1.start_engine()


# ===============================
# 📘 OOPs Intermediate Questions (35 Questions)
# ===============================

# 1. Create a class `BankAccount` with deposit and withdraw methods. Add balance validation.
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
            
    def deposite(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print("Deposite successful")
    
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful")
            
    def get_balance(self):
        print(self.balance)

obj = BankAccount(1000)
obj.deposite(100)
obj.withdraw(1000)
obj.get_balance()

# 2. Implement a class `Library` with methods to add and issue books.
class Library:
    def __init__(self):
        self.book = {}
    
    def add_book(self, book_name, quantity=1):
        if book_name in self.book:
            self.book[book_name] += quantity
        else:
            self.book[book_name] = quantity
            print(f'Book "{book_name}" added successfully. Total copies: {self.book[book_name]}')

    def issue_book(self,book_name):
        if book_name not in self.book:
            print("Book are not available")
        elif self.book[book_name] == 0:
            print(f'Book "{book_name}" is out of stock.')
        else:
            self.book[book_name] -= 1
            print(f'Book "{book_name}" issued successfully. Remaining copies: {self.book[book_name]}')
            
library = Library()

library.add_book("Harry Potter", 3)
library.add_book("Python Programming", 2)

library.issue_book("Harry Potter")
library.issue_book("Python Programming")
library.issue_book("The Alchemist")  # Not in library

library.issue_book("Python Programming")
library.issue_book("Python Programming")  # Out of stock now


            
# 3. Create a `Car` class with instance variables for model, year, and brand.
class Car:
    def __init__(self, model, year, brand):
        self.model = model
        self.year = year
        self.brand = brand
        
    def __str__(self):
        return f"Car model is {self.model}, year {self.year} and brand is {self.brand}"

obj1 = Car("M4", 2002, "honda")
print(obj1)

# 4. Build a `Student` class with default and parameterized constructors.
class Student:
    def __init__(self, name="unknown", age=12):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
student1 = Student()
student1.display()

print("---------")

student2 = Student("alok",21)
student2.display()
        

# 5. Add a class variable to count number of active instances of a class.


# 6. Use `@staticmethod` to define a utility method in a class.


# 7. Use `@classmethod` to create objects in alternative ways (e.g., from a string).


# 8. Create a class `Shape` and subclass `Circle`, `Rectangle` with area methods.


# 9. Demonstrate method overriding using a base and derived class.


# 10. Demonstrate multiple inheritance with proper constructor calls.


# 11. Use `super()` in child class to call parent constructor.


# 12. Build a `Logger` class with a singleton pattern.


# 13. Use dunder methods like `__str__`, `__eq__`, and `__repr__` for a `Product` class.


# 14. Write a class that implements custom sorting using `__lt__`.


# 15. Create a class with private variables and methods.


# 16. Define a `Calculator` class and implement chaining of operations.


# 17. Create a class `Timer` with start, stop, and elapsed time functionality.


# 18. Implement a class `User` with validation for email format using regex.


# 19. Create a class `Matrix` and overload `+`, `-`, and `*` operators (no 2D list).


# 20. Build a class `NotificationManager` to handle sending emails/SMS.


# 21. Implement a `MusicPlayer` class with a playlist (no nested lists).


# 22. Define a `FileManager` class that reads/writes from a file.


# 23. Create a class with context manager support using `__enter__` and `__exit__`.


# 24. Write a class with class-level cache/memoization.


# 25. Design a `QueueManager` class using OOP principles.


# 26. Create a base class `Employee` and subclasses `Developer`, `Manager`.


# 27. Implement an abstract class `Device` with abstract methods.


# 28. Demonstrate polymorphism using a method `start()` in various classes.


# 29. Define a `Game` class and use encapsulated score tracking.


# 30. Implement a plugin system using inheritance.


# 31. Build a `PasswordManager` with encapsulation and file-based persistence.


# 32. Create a `SearchEngine` class that indexes and searches strings.


# 33. Build a class `Logger` that writes logs with timestamps.


# 34. Implement a simple observer pattern using OOP.


# 35. Design a `PaymentGateway` class supporting different payment modes.


# ===============================
# 🔐 Encapsulation Practice Questions (20 Questions)
# ===============================

# 1. Create a class with private variables and provide getter and setter methods.


# 2. Build a `UserProfile` class with encapsulated data and validation on setters.


# 3. Implement a `SecureVault` class that denies access without authentication.


# 4. Create an `Account` class with private balance and deposit/withdraw with limits.


# 5. Design a `Settings` class where some fields cannot be accessed externally.


# 6. Use name mangling to prevent access to critical fields.


# 7. Write a class `Mobile` with private model number and price with validation.


# 8. Implement encapsulation in a `Flight` class to manage seat booking.


# 9. Create a class `EmailService` with private configuration settings.


# 10. Design a class that encrypts stored values using encapsulation.


# 11. Implement encapsulation in a class managing employee salaries.


# 12. Build a `ShoppingCart` class with encapsulated cart and methods to update it.


# 13. Create a `Loan` class with private interest rate and calculation logic.


# 14. Build a `PatientRecord` class where sensitive info is private.


# 15. Encapsulate a class that tracks API usage and rate limits.


# 16. Make a `SecureNote` class with methods to unlock and view notes.


# 17. Build a `TaskManager` class where task details are private.


# 18. Encapsulate a `Sensor` class with private readings and public interface.


# 19. Create a class `BankLocker` which uses OTP-based private access.


# 20. Write a class `Transaction` with private sender, receiver, and amount details.


# ===============================
# 🧩 Aggregation Practice Questions (10–15 Questions)
# ===============================

# 1. Create a `Department` class that aggregates multiple `Employee` objects.


# 2. Build a `Library` class that contains multiple `Book` instances.


# 3. Make a `Team` class that holds a list of `Player` objects (use list, not 2D).


# 4. Create a `School` class that aggregates `Student`, `Teacher`, and `Classroom`.


# 5. Design a `University` class with colleges and each college has departments.


# 6. Build a `Computer` class with `CPU`, `RAM`, and `Storage` as components.


# 7. Create a `Restaurant` class with menu items aggregated as objects.


# 8. Write a `Project` class that includes multiple `Task` objects.


# 9. Build a `CarRental` class that contains multiple `Car` instances.


# 10. Make a `Company` class that aggregates `HR`, `Finance`, and `Tech` departments.


# 11. Design a `Course` class that aggregates multiple `Lesson` objects.


# 12. Create a `Schedule` class that aggregates `Meeting` objects with time slots.


# 13. Implement a `Blog` class that aggregates `Post`, `Comment`, and `Author` objects.


# 14. Build a `Marketplace` with `Seller`, `Buyer`, and `Product` aggregation.


# 15. Design a `Building` class with aggregated `Floor`, `Room`, and `Person` classes.


# ===============================
# 🔄 Combination Practice: Encapsulation + Aggregation (10–15 Questions)
# ===============================

# 1. Create a `Bank` class with multiple `Customer` objects (encapsulated info).


# 2. Build a `Hospital` class where `Patient` data is private and managed through classes.


# 3. Make a `Company` class that includes `Employee` with salary as private data.


# 4. Design an `ECommerce` system with `User`, `Order`, and `Cart` (all encapsulated).


# 5. Write a `LearningPlatform` class that contains `Course` objects with private ratings.


# 6. Create a `SmartHome` class managing encapsulated devices like `Light`, `Thermostat`.


# 7. Build a `MovieTheater` system with `Movie`, `Seat`, and private booking info.


# 8. Make a `Warehouse` class with private `Inventory` data and multiple `Product` entries.


# 9. Create a `BankingSystem` where accounts are private and transactions are aggregated.


# 10. Implement a `Conference` class aggregating `Session` objects with private schedule.


# 11. Create a `VehicleServiceCenter` with `Customer`, `Vehicle`, and service details.


# 12. Build a `Hotel` class that has `Room` and `Guest` classes with private booking status.


# 13. Make an `EventManager` class where events aggregate `Attendee` with private access.


# 14. Develop a `Clinic` that aggregates `Doctor` and `Patient` classes with private data.


# 15. Write a `CourseManagement` system with encapsulated `Instructor` and `Student` objects.



# 🐍 Inheritance basic 

# 1. Write a program to check whether a number is even or odd.

# 2. Write a program to find the largest of three numbers.

# 3. Write a program to count the number of vowels in a given string.

# 4. Write a program to reverse a string without using built-in functions.

# 5. Write a function that returns the factorial of a number using recursion.

# 6. Write a program to check if a given string is a palindrome.

# 7. Write a program to print the Fibonacci sequence up to n terms.

# 8. Write a program to find all the prime numbers between 1 and 100.

# 9. Write a function that takes a list and returns the second largest element.

# 10. Write a program to remove all duplicates from a list.

# 11. Write a program to count the frequency of each word in a sentence.

# 12. Write a program to check if a number is an Armstrong number.

# 13. Write a program to sort a list without using the built-in sort() function.

# 14. Write a function that accepts a string and returns a dictionary with characters as keys and their counts as values.

# 15. Write a program to find the sum of digits of a number using a loop.


# 🐍 Getter-setter basic 

# Q1: Create a class `Person` with a private variable `_age`.
# Write a getter method `get_age()` and setter method `set_age()`.
# Ensure that age cannot be negative (add validation in setter).

# Q2: Create a class `BankAccount` with private variable `_balance`.
# Add getter and setter methods.
# Make sure balance cannot be set to a non-numeric value or negative number.

# Q3: Create a class `Student` with private variables `_name` and `_grade`.
# Write appropriate getter and setter methods.
# Ensure grade is between 0 and 100 in setter.

# Q4: Create a class `Product` with private variables `_name`, `_price`.
# Add getter/setter methods and ensure price is a float and non-negative.

# Q5: Create a class `Car` with private variables `_speed`, `_engine_status`.
# Write getter and setter for both.
# Prevent setting speed above 300, and engine_status must be either "on" or "off".

# Q6: Create a class `Temperature` with a private variable `_celsius`.
# Write getter and setter for Celsius.
# Add a getter `get_fahrenheit()` that returns converted value in Fahrenheit.

# Q7: Create a class `Rectangle` with private `_length` and `_width`.
# Add setters with validation (must be > 0).
# Add a getter method to return area.

# Q8: Create a class `Employee` with `_name`, `_salary`.
# Ensure salary cannot be below 10000.
# Add getter and setter methods for both attributes.

# Q9: Create a class `Laptop` with private variables `_brand`, `_ram`.
# Add getter and setter methods.
# Ensure RAM is an integer and must be one of [4, 8, 16, 32].

# Q10: Create a class `Movie` with private `_title`, `_rating`.
# Add getter/setter methods.
# Make sure rating is between 1.0 and 10.0.

# Q11: Create a class `User` with `_username`, `_password`.
# Write getter and setter.
# Ensure password is at least 8 characters long.

# Q12: Create a class `Circle` with private `_radius`.
# Add setter with validation (radius > 0).
# Add getter for radius and method to calculate circumference and area.

# Q13: Create a class `Book` with `_title`, `_author`, and `_pages`.
# Ensure pages is an integer > 0.
# Add appropriate getter and setter methods.

# Q14: Create a class `Mobile` with `_model`, `_price`.
# Ensure price is a number > 0.
# Use `@property` and `@price.setter` decorators instead of traditional methods.

# Q15: Create a class `Account` with `_account_number`, `_balance`.
# Balance can be set only if account number is valid (must be 10 digits).
# Add validation logic in setters.
