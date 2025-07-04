# Quiz

Test your understanding of statements, semicolons, and comments in JavaScript.

---

### Question 1 
What will be the output of the following code?
```javascript
alert('Hello');
alert('World');
```

1. Only "Hello" appears  
2. Only "World" appears  
3. Both "Hello" and "World" appear in sequence  
4. An error occurs  

<details>
<summary>Show Answer</summary>

**Answer: 3**  
Both alerts will execute sequentially because they are separate statements properly terminated with semicolons.
</details>

---

### Question 2 
Why does this code work without semicolons?
```javascript
alert('Hello')
alert('World')
```

1. JavaScript doesn't need semicolons at all  
2. Newlines automatically insert semicolons in most cases  
3. Parentheses automatically insert semicolons  
4. The code actually doesn't work  

<details>
<summary>Show Answer</summary>

**Answer: 2**  
JavaScript performs automatic semicolon insertion (ASI) when line breaks exist, though this isn't always reliable.
</details>

---

### Question 3
What happens when you run this code?
```javascript
alert("Hello")

[1, 2].forEach(alert)
```

1. Shows "Hello", then 1, then 2  
2. Only shows "Hello" with an error  
3. Shows nothing  
4. Shows 1 and 2 but not "Hello"  

<details>
<summary>Show Answer</summary>

**Answer: 2**  
Without the semicolon, JavaScript tries to read `alert("Hello")[1, 2]` as one statement, causing an error after the first alert.
</details>

---

### Question 4 
Which of these is a valid multiline comment?

1. `// Comment //`  
2. `<!-- Comment -->`  
3. `/* Comment */`  
4. `** Comment **`  

<details>
<summary>Show Answer</summary>

**Answer: 3**  
Only `/* */` creates multiline comments in JavaScript. Option 1 is for single-line comments, and option 2 is HTML syntax.
</details>

---

### Bonus Question 
Why does this code fail?
```javascript
/*
  /* nested comment */
*/
alert('World');
```

1. Nested comments are not supported in JavaScript  
2. Missing semicolon  
3. alert() cannot follow a comment  
4. The comment isn't closed properly  

<details>
<summary>Show Answer</summary>

**Answer: 1**  
JavaScript doesn't support nested `/* */` comments. The first `*/` closes the entire comment block.
</details>
```

