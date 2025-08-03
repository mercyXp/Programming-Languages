
# Errors and Exception Handling in Python

This guide equips you with the knowledge to identify, handle, and prevent errors in your Python programs. You’ll learn about common errors, exception handling mechanisms, and how to write robust, fault-tolerant code.

---

## 📘 Concept Overview

### Topics Covered:
- Understanding Python Errors
- Mastering Exception Handling

### Learning Objectives:
- Differentiate between syntax errors and exceptions.
- Identify common Python exceptions and their causes.
- Utilize `try`, `except`, `else`, and `finally` blocks for exception handling.
- Raise exceptions using `raise` and create custom exceptions.
- Write code that anticipates and gracefully handles potential errors.

---

## 🧠 Introduction

Errors are inevitable in programming. Python errors can be broadly categorized into two main types:

### 1. **Syntax Errors**
These occur when the code violates Python’s grammar rules. They are detected during compilation and prevent the program from running.

### 2. **Exceptions**
These are runtime errors that arise during execution, indicating unexpected conditions. They can be handled programmatically to avoid crashes.

---

## 🔍 Detailed Explanation

### 🔴 Understanding Python Errors

#### Common Syntax Errors:
- Missing colons (`:`) after statements
- Incorrect indentation
- Unmatched parentheses or brackets
- Typos in variable or function names

#### Common Exceptions:
| Exception        | Cause                                                                 |
|------------------|-----------------------------------------------------------------------|
| `NameError`      | Variable/function used before definition                              |
| `TypeError`      | Operation on incompatible data types                                  |
| `IndexError`     | Accessing index outside list/sequence range                           |
| `ZeroDivisionError` | Attempting to divide by zero                                     |
| `ValueError`     | Invalid value passed to a function or operation                       |

---

### 🛡️ Mastering Exception Handling

Python provides a powerful exception-handling mechanism using `try`, `except`, `else`, and `finally` blocks:

```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
else:
    # Executes if no exception occurs
finally:
    # Always executes, regardless of exceptions
````

#### Explanation:

* `try`: Code that may raise an exception.
* `except`: Catches specific exceptions.
* `else`: Executes if the try block has no exceptions.
* `finally`: Executes regardless of what happens above (used for cleanup tasks).

#### Example with `raise`:

```python
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return x / y
```

---

## 🧩 Custom Exceptions

### ✅ What are Custom Exceptions?

User-defined exception classes used for handling specific application errors. Inherit from the base `Exception` class.

### ✅ Why Use Them?

* **Specificity**: Handle unique errors more clearly.
* **Readability**: Improve error messages and understanding.
* **Modularity**: Keep related error-handling logic organized.

### ✅ Creating a Custom Exception:

```python
class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."
```

#### Sample Inventory:

```python
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,
    "grapes": 3
}
```

### ✅ Function to Simulate Purchase:

```python
def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")
```

### ✅ Testing the Custom Exception:

```python
try:
    purchase_item("apple", 3)         # ✅ Success
    purchase_item("orange", 1)        # ❌ Raises OutOfStockError
    purchase_item("watermelon", 1)    # ❌ KeyError for unavailable item
except OutOfStockError as e:
    print(e)
```

---

## 📝 Practice Exercises

### Exercise 1: `ZeroDivisionError`

Write a program that:

* Takes two numbers as input.
* Divides the first by the second.
* Handles division by zero gracefully.

---

### Exercise 2: `FileNotFoundError`

Write a program that:

* Accepts a filename from the user.
* Tries to open and read the file.
* Handles the error if the file doesn’t exist.

---

### Exercise 3: Custom Exception `ValueTooHighError`

* Create a custom exception class `ValueTooHighError`.
* Write a program that takes a number input.
* Raise the exception if the number is greater than 100.

---

## 📚 Additional Resources

* [Python Official Docs: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Python Exception Handling (W3Schools)](https://www.w3schools.com/python/python_try_except.asp)
* [Python Tutorial for Beginners – Exception Handling (YouTube)](https://www.youtube.com/watch?v=NIWwJbo-9_8)
* [Guide to Python Exception](https://realpython.com/python-exceptions/)



