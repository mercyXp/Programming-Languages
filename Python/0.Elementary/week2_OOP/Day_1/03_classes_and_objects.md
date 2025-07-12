
# 🏗️ Classes and Objects in Python

Object-Oriented Programming in Python starts with two fundamental building blocks: **Classes** and **Objects**.

---

## What is a Class?

A **class** is like a **blueprint or template** for creating objects — similar to a **cookie cutter** that shapes cookies.

### A class can contain:

- **Constructor (`__init__`)**: Special method to **initialize** object data.
- **Instance Methods**: Define object **behaviors** (actions).
- **Class Variables**: Variables **shared by all objects** of the class.

---

## 🧊 What is an Object?

An **object** is a **runtime instance** of a class — like the actual **cookie** made from the cutter.

- Each object has its own **copy of instance attributes**.
- Objects **occupy memory** during program execution.

---

## Example: Student Class

```python
class Student:
    # Class Variable (shared across all instances)
    school_name = "XYZ University"

    def __init__(self, name, gpa):
        self.name = name        # Instance Variable
        self.gpa = gpa          # Instance Variable

    def get_grade(self):
        return "A" if self.gpa >= 3.5 else "B"

# Creating objects
alice = Student("Alice", 3.7)
bob = Student("Bob", 3.2)

# Accessing object data
print(f"{alice.name}: {alice.get_grade()}")  # Output: "Alice: A"
print(f"{bob.name}: {bob.get_grade()}")      # Output: "Bob: B"

# Accessing class variable
print(Student.school_name)  # Output: "XYZ University"
````

---

## 🔍 Key Observations

* `self` refers to the **current instance** of the class.
* Class variables can be accessed using either:

  * `Student.school_name` (preferred)
  * `self.school_name` (works, but not preferred for shared data)
* Each object (`alice`, `bob`) has its **own copy of `name` and `gpa`**, but **shares `school_name`**.

---

## 🎯 Summary Table

| Concept        | Description                      |
| -------------- | -------------------------------- |
| `class`        | Defines the structure of objects |
| `__init__`     | Initializes object attributes    |
| `self`         | Refers to the current object     |
| Class Variable | Shared among all instances       |
| Object         | Instance of a class              |

---

## 🧠 Quick Practice Task

1. Create a class `Book` with attributes: `title`, `author`, and `pages`.
2. Add a method `is_long()` that returns `True` if pages > 300.
3. Create two `Book` objects and test the method.

---

## 📚 Extra Resources

* 🔗 [W3Schools – Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)
* 🔗 [Programiz – Python OOP: Classes and Objects](https://www.programiz.com/python-programming/class)
* 📺 [Corey Schafer – Python Classes and Objects (YouTube)](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)




