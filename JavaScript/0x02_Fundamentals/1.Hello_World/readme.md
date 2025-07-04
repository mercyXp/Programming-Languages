# 🟨 Getting Started with JavaScript (No Experience Needed)

Welcome! In this quick guide, you’ll write your first JavaScript program using **VS Code** or any text editor — no experience required!

---
## What Is JavaScript?
JavaScript is a programming language used to make websites interactive (e.g. buttons, pop-ups, games). It can also run outside the browser using tools like **Node.js**.

---
## What You Need
- A code editor like **[VS Code](https://code.visualstudio.com/)**
- A modern web browser (e.g. Chrome, Firefox)
- Optional: **Node.js** if you want to run JS without a browser
---

## Writing Your First JavaScript in a Webpage
1. **Create a new file** and name it:  
   `index.html`
2. **Add this code:**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Hello JavaScript</title>
  </head>
  <body>
    <h1>My First JavaScript Program</h1>

    <script>
      alert("Hello, world!");
    </script>
  </body>
</html>
```` 
3. **Open the file in your browser**

- Right-click `index.html` → Open with → Chrome or any browser  
- You should see a pop-up that says: `Hello, world!`

🎉 Congratulations — you just wrote your first JavaScript!

---

## 📂 Writing JavaScript in a Separate File

Instead of writing code inside the HTML file, you can also write it in a **separate `.js` file**.

1. Create a new file:  
   `script.js`

2. Add this code:

```javascript
alert("Hello from script.js!");

Update your index.html like this:

````html
<!DOCTYPE html>
<html>
  <head>
    <title>External Script</title>
  </head>
  <body>
    <h1>JavaScript from a File</h1>

    <script src="script.js"></script>
  </body>
</html>
````
Now, when you open the page, the JavaScript from script.js will run.

## ❌ Outdated Stuff to Ignore
You might see these in old tutorials, but you don't need them:

type="text/javascript" → not needed

language="javascript" → obsolete

<!-- --> inside <script> → very outdated

## Key Takeaways
JavaScript runs in the browser using the <script> tag.

You can write JS inside your HTML or in a separate .js file.

Keep your JS in a separate file as your code grows.


