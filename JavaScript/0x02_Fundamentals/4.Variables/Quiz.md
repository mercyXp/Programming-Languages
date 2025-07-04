# JavaScript Variables Quiz

### 1. Basic Declaration  
Which keyword is used to declare a block-scoped variable in modern JavaScript?  
A) `var`  
B) `let`  
C) `const`  
D) `variable`  

<details>
<summary><b>Answer</b></summary>
**B) `let`**  
`let` provides block-scoping, unlike `var`.
</details>

---

### 2. Constant Variables  
What happens when you run this?  
```javascript
const PI = 3.14;
PI = 3.14159;
```  
A) Value updates  
B) Silent failure  
C) `TypeError`  
D) Creates new variable  

<details>
<summary><b>Answer</b></summary>
**C) `TypeError`**  
`const` variables cannot be reassigned.
</details>

---

### 3. Variable Naming  
Which name follows JS naming conventions?  
A) `1stPlace`  
B) `user-name`  
C) `$price`  
D) `default`  

<details>
<summary><b>Answer</b></summary>
**C) `$price`**  
Valid names can include `$` and `_`, but not hyphens or reserved words.
</details>

---

### 4. Declaration Output  
What logs here?  
```javascript
let x;
console.log(x);
```  
A) `undefined`  
B) `null`  
C) `ReferenceError`  
D) `0`  

<details>
<summary><b>Answer</b></summary>
**A) `undefined`**  
Declared but unassigned variables hold `undefined`.
</details>

---

### 5. Multi-Line Style  
Which is the preferred way to declare multiple variables?  
A)  
```javascript
let a=1,b=2;
```  
B)  
```javascript
let a = 1,
    b = 2;
```  
C)  
```javascript
let a = 1;
let b = 2;
```  

<details>
<summary><b>Answer</b></summary>
**C) Separate lines**  
Best for readability and maintenance.
</details>

---

### 6. Uppercase Constants  
When should constants be uppercase?  
A) Always  
B) Never  
C) Only for hard-coded values  
D) Only in global scope  

<details>
<summary><b>Answer</b></summary>
**C) Only for hard-coded values**  
Like `COLOR_RED = "#F00"`, not runtime-calculated values.
</details>

---

### 7. Deprecated Practice  
Why should you avoid `var`?  
A) Function-scoping can cause bugs  
B) Allows redeclaration  
C) No block-scoping  
D) All of the above  

<details>
<summary><b>Answer</b></summary>
**D) All of the above**  
`let`/`const` fix all these issues.
</details>

---

### 8. Temporal Dead Zone  
What error occurs here?  
```javascript
console.log(y);
let y = 5;
```  
A) `ReferenceError`  
B) `undefined`  
C) `TypeError`  
D) No error  

<details>
<summary><b>Answer</b></summary>
**A) `ReferenceError`**  
`let` variables can't be accessed before declaration.
</details>

---

### 9. Object Constants  
What's the output?  
```javascript
const user = { name: "Alice" };
user.name = "Bob";
console.log(user.name);
```  
A) `Alice`  
B) `Bob`  
C) `TypeError`  

<details>
<summary><b>Answer</b></summary>
**B) `Bob`**  
`const` only prevents reassigning the variable, not modifying its properties.
</details>

---

### 10. Naming Best Practice  
Which name is most descriptive?  
A) `data`  
B) `userCart`  
C) `uc`  
D) `x`  

<details>
<summary><b>Answer</b></summary>
**B) `userCart`**  
Clear and follows camelCase convention.
</details>

---

**Scoring:**  
- 9-10: Variables Master! 💻  
- 6-8: Solid Understanding 👍  
- ≤5: Review Recommended 📚
```
