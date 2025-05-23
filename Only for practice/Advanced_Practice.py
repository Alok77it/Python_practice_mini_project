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




#### Intermediate Level #####
# 1. Create a class `Point2D` that can store x and y coordinates.
#    Add a method to display the point as (x, y).

# 2. Add a method to `Point2D` to calculate the distance from the point to the origin (0,0).

# 3. Add a method to `Point2D` that takes another `Point2D` object and returns the distance between the two points.

# 4. Create a class `Rectangle` initialized with two `Point2D` objects representing opposite corners.
#    Add methods to calculate the area and perimeter.

# 5. Create a class `Circle` with a center (Point2D) and radius.
#    Add methods to calculate the circumference and area.

# 6. Implement a `Vector2D` class with vector addition, subtraction, and scalar multiplication methods.

# 7. Create a `Polygon` class that takes a list of `Point2D` vertices.
#    Add a method to calculate the polygon's perimeter.

# 8. Create a `Line` class defined by two `Point2D` points.
#    Add methods to calculate the slope and check if another line is parallel.

# 9. Implement a `Triangle` class with three vertices (Point2D).
#    Add methods to calculate the area using Heron's formula.

# 10. Extend the `Point2D` class to support vector dot product and cross product with another point.

# 11. Create a `Matrix2x2` class with methods to perform matrix addition, multiplication, and determinant calculation.

# 12. Implement a `ComplexNumber` class with real and imaginary parts.
#     Add methods for addition, multiplication, and magnitude calculation.

# 13. Create a `Polygon` class that can check if it is convex or concave based on its vertices.

# 14. Implement a `Circle` class with a method that checks whether a given `Point2D` lies inside the circle.

# 15. Create a `Point3D` class extending `Point2D` by adding a z-coordinate.
#     Add distance methods between two 3D points and from origin.

# 16. Design a `Shape` base class and have `Circle`, `Rectangle`, and `Triangle` inherit from it.
#     Each subclass should implement methods `area()` and `perimeter()`.

# 17. Create a class `LineSegment` with two endpoints (Point2D).
#     Add a method to check if two line segments intersect.

# 18. Implement a class `Polygon` with a method to determine if a given point is inside the polygon (point-in-polygon test).

# 19. Implement a `BezierCurve` class defined by control points (list of Point2D).
#     Add a method to compute the point on the curve at a parameter t (0 <= t <= 1).

# 20. LeetCode-style: Implement a `RectangleArea` class which takes multiple rectangles as input.
#     Add a method to calculate the total area covered by these rectangles (handle overlaps).

# Additional patterns and ideas for advanced practice:

# 21. Implement operator overloading in `Point2D` for +, -, and ==.

# 22. Implement a method in `Polygon` to compute the centroid of the polygon.

# 23. Implement a `Circle` class method to find the intersection points of two circles.

# 24. Implement a `ShapeCollection` class that can hold multiple shapes and calculate the total area.

# 25. Design a `Graph` class to store points as nodes and distances as edges.
#     Implement a method to find the shortest path between two points using Dijkstra's algorithm.

# 26. LeetCode-style: Implement a `MovingAverage` class that calculates the moving average of points coordinates' distances from origin over the last N points.

# 27. Implement a `Path` class that holds a list of points and methods to calculate total path length and add smoothing.

# 28. Create a `Transform` class to apply translation, rotation, and scaling transformations to points.

# 29. Design a `Quadtree` spatial data structure to efficiently query points within a region.

# 30. LeetCode-style: Given a list of points, implement a method to find the k closest points to the origin.

# 31. Implement a class `BezierSpline` composed of multiple `BezierCurve` segments with a method to get the spline length.

# 32. Implement `__str__` and `__repr__` methods for all your shape classes for better debugging.

# 33. Add serialization and deserialization methods (to/from JSON) for your geometric objects.

# 34. Create a `BoundingBox` class to find the minimal rectangle that contains a list of points.

# 35. Implement a class method to generate a regular polygon given the number of sides and radius.



###Pattern Based###

# 1. Implement a Singleton class in Python to ensure only one instance is created.

# 2. Create a Factory class that returns different types of shapes (Circle, Rectangle, Triangle) based on input.

# 3. Design a Decorator pattern for a Shape class to add border or fill color functionality dynamically.

# 4. Implement a Strategy pattern for sorting a list of Point2D objects by distance from origin or by x-coordinate.

# 5. Create an Observer pattern where multiple listeners get notified when a Point2D moves.

# 6. Implement a Command pattern that records and executes operations on a Shape object (e.g., move, resize).

# 7. Design a Builder pattern for constructing complex polygons step-by-step.

# 8. Create a Prototype pattern that allows cloning of complex shape objects.

# 9. Implement the Adapter pattern to allow legacy code using tuples (x, y) to work with your Point2D class.

# 10. Create a Composite pattern to handle groups of shapes as a single shape (e.g., group of Circles and Rectangles).

# 11. Implement a Flyweight pattern to reduce memory usage when creating many identical Point2D objects.

# 12. Design a Mediator class to manage interactions between multiple shapes on a canvas.

# 13. Implement a State pattern where a Shape object can be in different states (e.g., Selected, Hidden, Visible) with different behavior.

# 14. Create a Chain of Responsibility pattern for processing geometric transformations (e.g., scale, rotate, translate).

# 15. Design a Template Method pattern where the base Shape class defines the algorithm structure for drawing,
#     and subclasses implement specific drawing steps.

# 16. Implement a Visitor pattern to add new operations to shape classes without modifying them (e.g., export to SVG).

# 17. Create an Iterator pattern for traversing points in a Polygon or vertices in a ShapeCollection.

# 18. Implement a Proxy pattern to delay expensive computation of a shape’s area until needed.

# 19. Design a Null Object pattern for a Shape class that does nothing but avoids null checks.

# 20. Implement a Multiton pattern for managing a limited set of named Color objects used by shapes.

# Bonus Pattern Challenge (LeetCode style):

# 21. Implement a Command Queue using Command pattern to support undo and redo operations on a drawing canvas.

# 22. Design a Shape Factory with caching (Flyweight + Factory) to return existing shapes when possible.

# 23. Create a Shape Decorator that logs each method call and its parameters (Decorator + Proxy).

# 24. Implement a dynamic plugin system (Strategy + Factory) to add new shape types at runtime.

# 25. Design a Shape Repository (Singleton + Mediator) to store and manage all shape objects in an application.

