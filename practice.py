class Parent:
    def display(self):
        print("This is parent classes")
        
class Child(Parent):
    pass

obj = Child()
obj.display()