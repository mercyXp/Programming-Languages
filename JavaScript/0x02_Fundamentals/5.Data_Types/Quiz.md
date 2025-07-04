# JavaScript Data Types Quiz

### 1. What is the correct way to create a BigInt?
A) `let big = 123L`  
B) `let big = BigInt(123)`  
C) `let big = 123n`  
D) Both B and C  

<details>
<summary><b>Answer</b></summary>
**D) Both B and C**  
BigInts can be created with either the `n` suffix or the `BigInt()` constructor.
</details>

---

### 2. What does `typeof null` return in JavaScript?
A) `"null"`  
B) `"object"`  
C) `"undefined"`  
D) `"number"`  

<details>
<summary><b>Answer</b></summary>
**B) `"object"`**  
This is a well-known historical bug in JavaScript that's maintained for backward compatibility.
</details>

---

### 3. Which of these is NOT a falsy value in JavaScript?
A) `0`  
B) `""`  
C) `[]`  
D) `null`  

<details>
<summary><b>Answer</b></summary>
**C) `[]`**  
Empty arrays are truthy values in JavaScript.
</details>

---

### 4. What will `console.log(0.1 + 0.2 === 0.3)` output?
A) `true`  
B) `false`  
C) `NaN`  
D) `undefined`  

<details>
<summary><b>Answer</b></summary>
**B) `false`**  
Due to floating-point precision issues, 0.1 + 0.2 equals approximately 0.30000000000000004.
</details>

---

### 5. Which type allows string interpolation?
A) Single-quoted strings  
B) Double-quoted strings  
C) Backtick strings  
D) All string types  

<details>
<summary><b>Answer</b></summary>
**C) Backtick strings**  
Only template literals (backticks) support `${expression}` interpolation.
</details>

---

### 6. What is the value of an uninitialized variable?
A) `null`  
B) `undefined`  
C) `NaN`  
D) `""`  

<details>
<summary><b>Answer</b></summary>
**B) `undefined`**  
Variables declared without assignment have the value `undefined`.
</details>

---

### 7. Which operation will NOT result in NaN?
A) `Number("text")`  
B) `0 / 0`  
C) `Math.sqrt(-1)`  
D) `1 / Infinity`  

<details>
<summary><b>Answer</b></summary>
**D) `1 / Infinity`**  
This results in 0, while the others produce NaN.
</details>

---

### 8. What's the key difference between `null` and `undefined`?
A) `null` is a type while `undefined` is a value  
B) `null` is assigned intentionally while `undefined` means no value assigned  
C) `undefined` is an object while `null` is primitive  
D) They are completely interchangeable  

<details>
<summary><b>Answer</b></summary>
**B) `null` is assigned intentionally while `undefined` means no value assigned**  
`null` represents deliberate absence of value, while `undefined` means a variable hasn't been assigned a value.
</details>

---

### 9. Which of these is a primitive type?
A) Array  
B) Object  
C) Function  
D) Symbol  

<details>
<summary><b>Answer</b></summary>
**D) Symbol**  
Symbol is one of JavaScript's 7 primitive types, while the others are objects.
</details>

---

### 10. What will `console.log(typeof typeof 42)` output?
A) `"number"`  
B) `"string"`  
C) `"type"`  
D) `"undefined"`  

<details>
<summary><b>Answer</b></summary>
**B) `"string"`**  
`typeof 42` returns `"number"` (a string), and `typeof "number"` returns `"string"`.
</details>

---

**Scoring Guide**:
- 9-10 correct: JavaScript Type Guru! 🏆
- 6-8 correct: Solid Understanding 👍
- ≤5 correct: Recommended to review data types 📚