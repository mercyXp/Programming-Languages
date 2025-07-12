#  The `__init__` Constructor in Python

## Purpose of `__init__`

- The `__init__` method is a **special method** in Python classes.
- It is **automatically called** when you create a new object.
- Its main role is to **initialize instance attributes** (i.e., assign initial values).
- Similar to "constructors" in other programming languages like Java, C++, etc.

---

## 🧪 Example: Book Class

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_checked_out = False  # Default value

    def check_out(self):
        self.is_checked_out = True

# Usage
book = Book("The Hobbit", "J.R.R. Tolkien", 310)
book.check_out()
print(book.is_checked_out)  # Output: True
````

### Explanation

* `__init__` takes `self` and other parameters like `title`, `author`, `pages`.
* `self.title = title` sets the object's attribute to the provided value.
* `self.is_checked_out = False` sets a **default** value for every new `Book` object.

---

## 🛠️ Practice Exercise Solution

### Create a `Car` class and initialize its attributes

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Test
my_car = Car("Ford", "Mustang", 2022)
my_car.display_info()  # Output: "2022 Ford Mustang"
```

###  What’s Happening Here?

* We define three attributes: `make`, `model`, and `year`.
* When `my_car = Car(...)` is called, Python runs `__init__` and sets up the object.
* The `display_info()` method prints a formatted description of the car.

---

## 💡 Tips

* `__init__` is not required in every class, but it’s very useful for setting up initial state.
* You can give **default values** to parameters inside `__init__` just like any function.
* You should **never return a value** from `__init__`; it must return `None` implicitly.

---

## 📚 Extra Resources

* 🔗 [Real Python – Python Classes and `__init__`](https://realpython.com/python3-object-oriented-programming/#classes-and-instances)
* 🔗 [GeeksforGeeks – OOP vs Procedural Programming](https://www.geeksforgeeks.org/difference-between-procedural-and-object-oriented-programming/)

---

## 🧠 Quick Practice Task

1. Create a class `Laptop` with attributes: `brand`, `processor`, `ram_size`.
2. Add a method `specs()` that prints all these attributes.
3. Create two `Laptop` objects and print their specs.
