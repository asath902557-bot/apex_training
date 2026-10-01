# Create a class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Create an object
student1 = Student("kulam nabi asath", 18)

# Access the object's method
student1.display()
