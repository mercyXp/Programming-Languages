class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def introduction(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
