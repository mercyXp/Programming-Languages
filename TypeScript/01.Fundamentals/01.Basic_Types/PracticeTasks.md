# Basic Types – Practice Tasks


## 🟢 **Easy Tasks (1–10)**

### **1. Boolean Variable**

Create a variable `isOnline` with a boolean type and assign it `true`.

### **2. Number Types**

Create two number variables: `age` and `price`. Assign any values.

### **3. String Template Literal**

Create a string template that says: `My age is (insert age) years.`

### **4. String vs Number Error**

Try assigning a number to a string variable and observe the TypeScript error.

### **5. Simple Array**

Create an array of numbers: `[2, 4, 6, 8]`.

### **6. Array Using Generic Syntax**

Create the same array using `Array<number>`.

### **7. Tuple Basics**

Create a tuple representing a person: `["Mercy", 22]`.

### **8. Enum Basics**

Create an enum named `Role` with values `Admin`, `User`, `Guest`.

### **9. Unknown Type**

Create a variable `value: unknown` and assign different types to it.

### **10. Any Type**

Create a variable `random: any` and set it to different values.

---

## 🟡 **Medium Tasks (11–18)**

### **11. Tuple Error Handling**

Create a tuple `[string, number]` and attempt to assign `[number, string]`.

### **12. Using Enums in Variables**

Create a variable `currentRole: Role` and assign it a value from your enum.

### **13. Unknown Type Narrowing**

Write an if-statement that checks if `value` (from task 9) is a string, then logs its length.

### **14. Any Type Danger**

Assign an object to `random: any` and access a property that does not exist.

### **15. Void Function**

Create a function `logMessage()` that returns nothing.

### **16. Null & Undefined Types**

Create variables:

* `emptyValue: null`
* `nothingHere: undefined`

### **17. Union Type Practice**

Create a variable `response: string | null`.

### **18. Object Type**

Create an object type variable:

```ts
let user: object = { name: "Mercy", age: 22 };
```

---

## 🔴 **Hard Tasks (19–25)**

### **19. Never Type Function**

Create a function `throwError()` that always throws an error.

### **20. Never for Infinite Loop**

Create a function `loopForever()` with a `while(true)` loop.

### **21. Enum Reverse Lookup**

Given your `Role` enum, log the string name of the value `1`.

### **22. Type Assertion (as Syntax)**

Convert an `unknown` variable to a string using `as string`.

### **23. Angle Bracket Assertion**

Convert an `unknown` variable to a number using `<number>`.

### **24. Complex Tuple**

Create a tuple with:

* string
* number
* boolean
* array of numbers
  Example: `["Mercy", 22, true, [1,2,3]]`.

### **25. Combining All Types**

Create a function that:

* Accepts a parameter of type `unknown`.
* Narrows it into `string`, `number`, or `boolean`.
* Throws an error (`never`) if it’s none of these.

---

