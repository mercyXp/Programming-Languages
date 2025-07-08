
# **Quiz**

#### **1. What does `alert("Hello")` do?**
- A) Opens a prompt for user input  
- B) Displays "Hello" in the console  
- C) Shows a modal with "Hello" and an OK button  
- D) Creates a popup window with "Hello"  

<details>
<summary><b>Show Answer</b></summary>
<p>

**Answer: C**  
`alert()` shows a **modal window** with the message and an OK button. It pauses script execution until dismissed.

</p>
</details>

---

#### **2. What does `prompt("Enter name")` return if the user clicks Cancel?**  
- A) `""` (empty string)  
- B) `undefined`  
- C) `null`  
- D) `false`  

<details>
<summary><b>Show Answer</b></summary>
<p>

**Answer: C**  
`prompt()` returns `null` if the user cancels or presses Esc. It only returns the input text if OK is clicked.

</p>
</details>

---

#### **3. How do you provide a default value in a `prompt`?**  
- A) `prompt(message, default)`  
- B) `prompt(message, "default")`  
- C) `prompt(default, message)`  
- D) `prompt(message).default("value")`  

<details>
<summary><b>Show Answer</b></summary>
<p>

**Answer: A**  
The syntax is `prompt(title, [default])`, where `default` is optional (e.g., `prompt("Age?", 100)`).

</p>
</details>

---

#### **4. What does `confirm("Are you sure?")` return if the user clicks OK?**  
- A) `"OK"`  
- B) `true`  
- C) `false`  
- D) `1`  

<details>
<summary><b>Show Answer</b></summary>
<p>

**Answer: B**  
`confirm()` returns `true` for OK and `false` for Cancel/Esc.

</p>
</details>

---

#### **5. Which of these is a limitation of `alert`, `prompt`, and `confirm`?**  
- A) They can be styled with CSS  
- B) They are non-blocking (async)  
- C) Their appearance depends on the browser  
- D) They work in Node.js  

<details>
<summary><b>Show Answer</b></summary>
<p>

**Answer: C**  
These methods are **modal** (blocking) and **browser-controlled** (cannot change their appearance/location).

</p>
</details>

---

