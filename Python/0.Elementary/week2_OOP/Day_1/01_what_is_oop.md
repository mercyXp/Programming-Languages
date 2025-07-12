# WHAT IS OOP?
**Object-Oriented Programming (OOP)** is a programming paradigm that organizes software design around **objects** rather than functions and logic. An object is a self-contained unit that consists of:
- **Data (Attributes/Properties)** – Variables that store information.
- **Behavior (Methods)** – Functions that perform actions on the data.

OOP helps in modeling real-world entities, making code more modular, reusable, and maintainable.

---

## 🏗️ Key Concepts in OOP

### 1. **Class**
- A **blueprint** or template for creating objects.
- Defines the structure (attributes & methods) that objects of the class will have.
- Example:
  ```python
  class Dog:  # Class definition
      def __init__(self, name, age):  # Constructor method
          self.name = name  # Attribute
          self.age = age    # Attribute
  ```

### 2. **Object (Instance)**
- A **specific instance** of a class.
- Created using the class constructor.
- Example:
  ```python
  my_dog = Dog("Buddy", 3)  # Creating an object
  ```

### 3. **Attribute**
- A variable that holds data associated with an object.
- Can be **instance attributes** (unique to each object) or **class attributes** (shared across all objects).
- Example:
  ```python
  print(my_dog.name)  # Output: "Buddy"
  print(my_dog.age)   # Output: 3
  ```

### 4. **Method**
- A function defined inside a class that operates on the object's data.
- Example:
  ```python
  class Dog:
      def bark(self):  # Method
          print("Woof! Woof!")
  
  my_dog.bark()  # Output: "Woof! Woof!"
  ```

---

## 🔧 The Four Pillars of OOP

### 1. **Encapsulation**
- Bundling data (attributes) and methods that operate on the data into a single unit (class).
- Restricts direct access to some components (using **private/protected attributes** in some languages).
- Example:
  ```python
  class Dog:
      def __init__(self, name):
          self.__name = name  # Private attribute
      
      def get_name(self):     # Getter method
          return self.__name
  ```

### 2. **Inheritance**
- A mechanism where a **child class** inherits attributes and methods from a **parent class**.
- Promotes **code reusability**.
- Example:
  ```python
  class Animal:  # Parent class
      def speak(self):
          print("Animal sound")

  class Dog(Animal):  # Child class
      def speak(self):  # Method overriding
          print("Woof!")
  ```

### 3. **Polymorphism**
- The ability of different classes to be treated as instances of the same class through inheritance.
- Achieved via **method overriding** and **method overloading**.
- Example:
  ```python
  def animal_sound(animal):
      animal.speak()  # Calls the appropriate speak() method

  animal_sound(Dog())  # Output: "Woof!"
  animal_sound(Cat())  # Output: "Meow!"
  ```

### 4. **Abstraction**
- Hiding complex implementation details and exposing only essential features.
- In Python, achieved using **abstract classes** and **interfaces** (via `abc` module).
- Example:
  ```python
  from abc import ABC, abstractmethod

  class Animal(ABC):
      @abstractmethod
      def speak(self):
          pass
  ```

---

## 🧪 Practical Example: `Dog` Class

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

    # Another method
    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# Creating an object
my_dog = Dog("Buddy", 3)

# Accessing attributes and methods
print(my_dog.name)       # Output: "Buddy"
my_dog.bark()            # Output: "Buddy says Woof!"
my_dog.describe()        # Output: "Buddy is 3 years old."
print(Dog.species)       # Output: "Canis familiaris"
```

---

## 📚 Best Practices in OOP
1. **Follow the Single Responsibility Principle (SRP)** – A class should have only one reason to change.
2. **Use meaningful names** for classes, methods, and attributes.
3. **Prefer composition over inheritance** where applicable.
4. **Use `__init__` for initialization** (constructor in Python).
5. **Document classes and methods** using docstrings.

---

## 🔗 Extra Resources
- [Real Python: OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [W3Schools OOP Tutorial](https://www.w3schools.com/python/python_classes.asp)
- [Python `abc` module (Abstraction)](https://docs.python.org/3/library/abc.html)
- [GeeksforGeeks: OOP Concepts](https://www.geeksforgeeks.org/python-oops-concepts/)
```

