
---

## 🧠 **What Are Conditional Statements?**

Conditional statements allow your program to **make decisions**.

They evaluate **expressions** that result in either `True` or `False`, and then execute different blocks of code based on those results.

Think of it like asking a question:

> "Is it raining?"
> If yes → take an umbrella
> If no → go without it

---

## 🔹 **Basic Syntax: `if`, `elif`, `else`**

### ✅ **1. Simple `if` Statement**

```python
temperature = 30
if temperature > 25:
    print("It's hot today!")
```

**Explanation:**

* The `if` checks if the condition is `True` (`30 > 25`)
* Since it is, the message prints.

---

### ✅ **2. `if...else` Statement**

```python
is_raining = False
if is_raining:
    print("Take an umbrella.")
else:
    print("No umbrella needed.")
```

**Output:**

```
No umbrella needed.
```

**Why?** Because `is_raining` is `False`, so the `else` block runs.

---

### ✅ **3. `if...elif...else` Statement**

```python
age = 16

if age >= 18:
    print("You're an adult.")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a child.")
```

**Output:**

```
You're a teenager.
```

### 🔁 Flow:

* `age >= 18` → `False`
* `age >= 13` → `True` → This block runs
* `else` is skipped

---

## 🔹 **Comparison Operators in Python**

| Operator | Example  | Meaning                  | Result  |
| -------- | -------- | ------------------------ | ------- |
| `==`     | `5 == 5` | Equal to                 | `True`  |
| `!=`     | `5 != 3` | Not equal to             | `True`  |
| `>`      | `10 > 7` | Greater than             | `True`  |
| `<`      | `4 < 2`  | Less than                | `False` |
| `>=`     | `7 >= 7` | Greater than or equal to | `True`  |
| `<=`     | `3 <= 5` | Less than or equal to    | `True`  |

---

### ✅ **4. Multiple Conditions**

```python
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")
```

**Output:**

```
Grade: B
```

---

### ✅ **5. Nested `if` Statements**

```python
logged_in = True
is_admin = False

if logged_in:
    if is_admin:
        print("Welcome, admin!")
    else:
        print("Welcome, user!")
else:
    print("Please log in.")
```

**Output:**

```
Welcome, user!
```

Nested `if` statements are when one `if` is inside another, often used for more specific checks.

---

### ✅ **6. Using `and`, `or`, `not` with Conditions**

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("You may enter.")
else:
    print("Access denied.")
```

**Output:**

```
You may enter.
```

**Explanation:**

* Both conditions are `True`, so the `if` block runs.

---

### ✅ Real-World Mini Task

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Access granted!")
else:
    print("Invalid credentials.")
```

---


