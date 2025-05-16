# 🐍 Python Basics: `print()` and `input()` Functions

## 📤 `print()` – Display Output

### ✅ Purpose
The `print()` function is used to display text or variables on the screen.

### 📌 Syntax
```python
print(object(s), sep=' ', end='\n', file=sys.stdout, flush=False)
````

### 💡 Examples

```python
print("Hello, world!")  # Outputs: Hello, world!

name = "Mercy"
print("My name is", name)  # Outputs: My name is Mercy
```

### 🧩 Key Parameters

* **`sep`**: Separator between multiple values (default is a space).

  ```python
  print("Python", "3.10", sep="-")  # Outputs: Python-3.10
  ```
* **`end`**: What to print at the end (default is a newline `\n`).

  ```python
  print("Loading...", end="")  # No newline
  ```

---

## 📥 `input()` – Get User Input

### ✅ Purpose

The `input()` function lets you collect input from the user via the keyboard.

### 📌 Syntax

```python
input(prompt)
```

### 💡 Example

```python
name = input("What is your name? ")
print("Hello,", name)
```

> 📝 The `input()` function **always returns a string**. Convert it if needed:

```python
age = input("Enter your age: ")
age = int(age)  # Convert from string to integer
```

---

## ⚠️ Quick Tips

* Always **convert** input when doing math or logic.
* You can **combine** `print()` and `input()`:

  ```python
  print("Welcome,", input("Enter your name: "))
  ```

---

## ✅ Summary Table

| Function  | Use                    | Returns | Notes                               |
| --------- | ---------------------- | ------- | ----------------------------------- |
| `print()` | Shows output on screen | `None`  | Accepts multiple items              |
| `input()` | Gets text from user    | `str`   | Use `int()` or `float()` to convert |

---

Happy coding! 🎉


