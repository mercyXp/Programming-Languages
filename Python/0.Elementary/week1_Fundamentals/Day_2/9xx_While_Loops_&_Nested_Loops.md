
# 🔁 While Loops and Nested Loops

Ready to venture beyond fixed iterations? `while` loops and nested loops introduce more flexibility for controlling program flow in Python. This concept page equips you with `while` loops (ideal for repetitive tasks based on conditions) and explores the power of nested loops for creating more intricate program logic.

---

## 📚 Concept Overview

### Topics

- **While Loops**: Master `while` loops, which execute a block of code repeatedly as long as a specific condition remains `True`.
- **Nested Loops**: Take your looping skills to the next level with nested loops. Imagine placing one loop inside another!

---

## 🎯 Learning Objectives

- Learn to use `while` loops for executing code as long as a condition is true.
- Understand how to implement nested loops and when they are useful.

---

## 🔄 Overview of While Loops

While `for` loops excel at iterating over a predetermined sequence, what if the number of repetitions depends on a condition? Enter `while` loops!

### 🧾 Syntax

```python
while condition:
    # Code block to be executed as long as the condition is True
````

* **condition**: This is an expression that evaluates to `True` or `False`.
* **code block**: This indented block of code runs as long as the condition is `True`.

### 🔍 Key Differences from `for` Loops

* **Iteration Control**:

  * `for` loops have a fixed number of iterations.
  * `while` loops keep running until a condition becomes `False`.

* **Predictability**:

  * `for` loops are predictable based on sequence length.
  * `while` loops are flexible but potentially infinite if not handled properly.

### 🧠 Use Cases

* Use `for` loops for sequences (`lists`, `ranges`, etc.)
* Use `while` loops when you don’t know the number of iterations in advance (e.g., user input validation, games, or breaking conditions).

---

## 🛠️ Practical Examples: While Loops

### 1. User Input Validation

```python
age = 0

while age < 18:
    age = int(input("Enter your age (must be 18 or older): "))

print("You are old enough to proceed.")
```

---

### 2. Guessing Game

```python
secret_number = 7

guess_count = 0
guess = 0

while guess != secret_number:
    guess_count += 1
    guess = int(input("Guess a number between 1 and 10: "))

print(f"You guessed it in {guess_count} tries!")
```

---

### 3. Iterating Until a Condition

```python
shopping_list = ["apples", "bread", "milk", "cheese"]
item_found = False

while not item_found:
    item = input("Search for an item in your list (or 'q' to quit): ")
    if item.lower() == "q":
        break
    if item in shopping_list:
        item_found = True
        print(f"{item} is on your shopping list.")
    else:
        print(f"{item} is not on your list.")
```

---

## 🎥 Here's a video on the subject:

*(Embed video link here)*

---

## 🔁 Nested Loops: Power Up Your Loops!

Nested loops involve putting one loop inside another. This powerful technique is essential for working with multidimensional data or generating patterns.

---

### 🧮 Countdown Using Nested `while` Loops

```python
outer_count = 5

while outer_count > 0:
    inner_count = 1
    while inner_count <= outer_count:
        print(inner_count, end=" ")
        inner_count += 1
    print()
    outer_count -= 1
```

---

### 🔢 Multiplication Table with Nested `for` Loops

```python
for i in range(1, 11):
    for j in range(1, 11):
        product = i * j
        print(f"{i} x {j} = {product}", end="\t")
    print()
```

---

### 🎨 Triangle Pattern with Asterisks

```python
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
```

---

## 🎥 Here's a video on the subject:

*(Embed video link here)*

---

## 🎯 Challenge: Nested Loop Art!

Let’s create some text-based art using nested loops!

### Objective:

Use nested `while` loops to print a pyramid pattern of asterisks (`*`).

### Example Output (for `rows = 5`):

```
    *
   ***
  *****
 *******
*********
```

### Steps:

1. Define the height:

   ```python
   rows = 5
   ```

2. Use a nested `while` loop:

   * Outer loop controls rows.
   * Inner loop prints spaces and then asterisks.
   * Adjust spaces and stars for each row.

---

## 📘 Additional Resources

* [Loops and Iterations - W3Schools](https://www.w3schools.com/python/python_while_loops.asp)
* [While Loop - GeeksForGeeks](https://www.geeksforgeeks.org/python-while-loops/)
* [Python while Loop - Official Docs](https://docs.python.org/3/tutorial/controlflow.html#the-while-statement)

Feel free to use any other resource to achieve the objectives!



