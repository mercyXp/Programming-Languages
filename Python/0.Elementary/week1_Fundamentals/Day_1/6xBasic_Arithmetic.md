# ➕ Python Basic Arithmetic Operators

Python can do math just like a calculator using **arithmetic operators**.

---

## 🧮 List of Basic Operators

| Operator | Meaning           | Example     | Result |
|----------|-------------------|-------------|--------|
| `+`      | Addition          | `2 + 3`     | `5`    |
| `-`      | Subtraction       | `5 - 2`     | `3`    |
| `*`      | Multiplication    | `4 * 3`     | `12`   |
| `/`      | Division          | `10 / 2`    | `5.0`  |
| `//`     | Floor Division    | `7 // 2`    | `3`    |
| `%`      | Modulus (Remainder) | `7 % 2`  | `1`    |
| `**`     | Exponentiation    | `2 ** 3`    | `8`    |

---

## 🔢 Examples

### ➕ Addition
```python
x = 10 + 5
print(x)  # 15
````

### ➖ Subtraction

```python
x = 10 - 3
print(x)  # 7
```

### ✖️ Multiplication

```python
x = 6 * 4
print(x)  # 24
```

### ➗ Division

```python
x = 9 / 2
print(x)  # 4.5 (always returns float)
```

### ➗ Floor Division (whole number only)

```python
x = 9 // 2
print(x)  # 4 (cuts off decimal part)
```

### 🔁 Modulus (remainder)

```python
x = 10 % 3
print(x)  # 1 (because 3*3 = 9, remainder = 1)
```

### ⏫ Exponentiation (power)

```python
x = 2 ** 4
print(x)  # 16 (2^4)
```

---

## 🧠 Combine With Variables

```python
a = 5
b = 3

print(a + b)  # 8
print(a * b)  # 15
print(a % b)  # 2
```

---

## ⚠️ Division Always Returns Float

Even if the result is a whole number:

```python
print(6 / 2)  # 3.0 (not 3)
```

Use `//` if you want a whole number:

```python
print(6 // 2)  # 3
```

---

## 🧪 Operator Precedence (BODMAS)

Python follows **BODMAS** (Brackets, Orders, Division/Multiplication, Addition/Subtraction):

```python
x = 2 + 3 * 4  # 2 + (3*4) = 14
y = (2 + 3) * 4  # (2+3) * 4 = 20
```

---

## ✅ Summary

* Use `+`, `-`, `*`, `/` for basic math
* Use `//`, `%`, `**` for floor, remainder, powers
* Use parentheses `()` to control order of operations

---

Happy calculating! 🧮🐍


