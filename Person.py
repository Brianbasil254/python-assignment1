# Define the Person class
class Person:
    # Constructor to initialize name, age, and gender
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # Method to introduce the person
    def introduce(self):
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance of the Person class
person1 = Person("Brian Basil", 24, "Male")

# Call the introduce method
person1.introduce()
