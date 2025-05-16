# 🔄 Python Type Conversion

## 📘 What is Type Conversion?

**Type conversion** means changing one data type to another.  
For example, turning a string into a number, or a float into an integer.

---

## 🔹 Two Types of Conversion

### 1. **Implicit Conversion** (done by Python automatically)
Python automatically changes the type when needed.

```python
x = 5        # int
y = 2.0      # float

result = x + y  # Python converts x to float
print(result)   # 7.0
print(type(result))  # <class 'float'>
````

---

### 2. **Explicit Conversion** (you do it yourself)

You use functions to convert between types:

| Function  | Converts to... |
| --------- | -------------- |
| `int()`   | Integer        |
| `float()` | Float          |
| `str()`   | String         |
| `bool()`  | Boolean        |

---

## 📌 Examples of Explicit Type Conversion

### 🔢 `str` ➡️ `int`

```python
num_str = "10"
num = int(num_str)
print(num + 5)  # 15
```

### 🔢 `str` ➡️ `float`

```python
price_str = "99.99"
price = float(price_str)
print(price + 0.01)  # 100.0
```

### 🔢 `int` ➡️ `str`

```python
age = 20
age_str = str(age)
print("I am " + age_str + " years old.")
```

### 🔢 `float` ➡️ `int`

Cuts off decimal part (does **not** round).

```python
height = 5.9
height_int = int(height)
print(height_int)  # 5
```

### ✅ `int` or `str` ➡️ `bool`

```python
print(bool(0))      # False
print(bool(10))     # True
print(bool(""))     # False
print(bool("Hi"))   # True
```

---

## ⚠️ Important Notes

* You **can’t** convert letters to numbers directly:

  ```python
  int("hello")  # ❌ Error!
  ```
* Always make sure the string **looks like** a number:

  ```python
  int("25")     # ✅ OK
  int("25.5")   # ❌ Error! Use float()
  ```

---

## ✅ Quick Practice

```python
a = "100"
b = int(a)
c = float(b)
d = str(c)

print(type(a))  # str
print(type(b))  # int
print(type(c))  # float
print(type(d))  # str
```

---

## 🧠 Summary Table

| From ➡️ To   | Function  | Example         | Result  |
| ------------ | --------- | --------------- | ------- |
| str ➡️ int   | `int()`   | `int("42")`     | `42`    |
| str ➡️ float | `float()` | `float("3.14")` | `3.14`  |
| int ➡️ str   | `str()`   | `str(7)`        | `"7"`   |
| float ➡️ int | `int()`   | `int(5.9)`      | `5`     |
| int ➡️ bool  | `bool()`  | `bool(0)`       | `False` |
| str ➡️ bool  | `bool()`  | `bool("hello")` | `True`  |

---

Happy converting! 🧪✨


