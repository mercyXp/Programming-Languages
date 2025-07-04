## Strict Mode Quiz

### 1. Basic Syntax
What is the correct way to enable strict mode?
A) `strict mode;`  
B) `"use strict";`  
C) `enable strict;`  

<details>
<summary><b>Answer</b></summary>
**B) `"use strict";`**  
Must be written exactly as a string literal.
</details>

---

### 2. Placement Importance
Where must "use strict" be placed to work?
A) Anywhere in the file  
B) After some code  
C) At the very top  

<details>
<summary><b>Answer</b></summary>
**C) At the very top**  
Only comments can appear above it.
</details>

---

### 3. Scope Application
Can strict mode be enabled for just one function?
A) No, only whole scripts  
B) Yes, by placing it inside the function  
C) Only in arrow functions  

<details>
<summary><b>Answer</b></summary>
**B) Yes, by placing it inside the function**  
It's function-scoped when used inside a function body.
</details>

---

### 4. Modern JavaScript
When is "use strict" automatically enabled?
A) In all ES6+ code  
B) Only in classes and modules  
C) Never, must always declare it  

<details>
<summary><b>Answer</b></summary>
**B) Only in classes and modules**  
Modern features enable it implicitly.
</details>

---

### 5. Console Behavior
Why might strict mode fail in browser consoles?
A) Consoles always use strict  
B) Consoles ignore it completely  
C) It's not default and requires special setup  

<details>
<summary><b>Answer</b></summary>
**C) It's not default and requires special setup**  
Either use Shift+Enter or IIFE wrapper.
</details>

---

### 6. Compatibility
What happens to old code when strict mode is enabled?
A) It breaks immediately  
B) Runs normally if no strict-mode violations  
C) Runs 50% slower  

<details>
<summary><b>Answer</b></summary>
**B) Runs normally if no strict-mode violations**  
Only code with strict-mode errors will break.
</details>

---

**Score Guide**:
- 6 Correct: Strict Mode Expert 🎯
- 4-5 Correct: Solid Understanding 👍
- ≤3 Correct: Review Recommended 📘