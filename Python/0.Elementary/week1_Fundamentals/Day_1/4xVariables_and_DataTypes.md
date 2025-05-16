# 🐍 Python Variables and Data Types

## 🧠 What is a Variable?

A **variable** is like a container that stores data in your program.  
You give it a name and assign a value using the `=` sign.

```python
name = "Zara"
age = 18
````

---

## 🧪 Python Data Types

Python has different types of data. The most common are:

### 1. 🔢 `int` – Integer

Whole numbers without decimal points.

```python
age = 25
year = 2025
apples = -3

print(type(age))  # <class 'int'>
```

---

### 2. 🔣 `float` – Decimal Numbers

Numbers with a decimal point.

```python
height = 5.8
price = 99.99
temperature = -3.5

print(type(price))  # <class 'float'>
```

---

### 3. 📝 `str` – String (Text)

Anything inside quotes (single or double) is a **string**.

```python
name = "Zara"
greeting = 'Hello'
phone_number = "1234567890"  # Still a string

print(type(name))  # <class 'str'>
```

You can combine strings with `+`:

```python
first_name = "Zara"
last_name = "K"
full_name = first_name + " " + last_name
print(full_name)  # Zara K
```

---

### 4. ✅❌ `bool` – Boolean

Only has two values: `True` or `False`. Used for decisions and conditions.

```python
is_tall = True
is_student = False

print(type(is_tall))  # <class 'bool'>
```

You often get boolean results from comparisons:

```python
print(5 > 3)   # True
print(10 == 5) # False
```

---

## 📌 Summary Table

| Type    | Example Values        | Description            |
| ------- | --------------------- | ---------------------- |
| `int`   | `5`, `0`, `-23`       | Whole numbers          |
| `float` | `3.14`, `-2.5`, `0.0` | Decimal numbers        |
| `str`   | `"hello"`, `'Zara'`   | Text (inside quotes)   |
| `bool`  | `True`, `False`       | Logic (yes/no, on/off) |

---

## 🧪 Checking Data Type

Use `type()` to check what type a variable is:

```python
x = "123"
print(type(x))  # <class 'str'>
```

---

## 🛠️ Variable Naming Rules

* Must start with a letter or underscore (`_`)
* Cannot start with a number
* Can contain letters, numbers, and underscores
* Are **case-sensitive**

```python
Name = "Zara"  # Not the same as name
name_1 = "Ali"
_age = 20
```

---

Happy learning! 🐍✨


