# Class Definition
class Car:
    # Constructor to initialize attributes
    def __init__(self, brand, model):
        self.brand = brand  # Attribute 1
        self.model = model  # Attribute 2

    # Method to display car details
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

    # Method to start the car
    def start_engine(self):
        print(f"The {self.brand} {self.model} engine has started.")

# Creating Objects (Instances)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing Attributes
print(car1.brand)  # Output: Toyota
print(car2.model)  # Output: Civic

# Calling Methods
car1.display_info()    # Output: Car: Toyota Corolla
car2.start_engine()    # Output: The Honda Civic engine has started.
