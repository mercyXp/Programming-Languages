# JavaScript Data Types

## Overview
JavaScript has 8 basic data types. Variables can hold any type and can change types dynamically.

JavaScript is a **dynamically typed** language. This means:

- Variables are not bound to a specific data type
- The same variable can hold different types of values over time
- Type checking happens at runtime rather than compile time

```javascript
let dynamicVariable = 'Hello';  // String
dynamicVariable = 42;           // Now a number
dynamicVariable = true;         // Now a boolean
```

**Key Characteristics:**
- No type declarations needed
- Types are associated with values, not variables
- Automatic type conversion (type coercion) in operations
- More flexible but requires careful type management

## Primitive Data Types

### 1. Number 
Represents both integer and floating-point numbers (64-bit IEEE 754 format)

```javascript
let integer = 42;
let float = 3.14159;
let scientific = 1.23e5;  // 123000
```

**Special Numeric Values:**
- `Infinity` and `-Infinity`
  ```javascript
  console.log(1 / 0);  // Infinity
  console.log(-1 / 0); // -Infinity
  ```
- `NaN` (Not a Number)
  ```javascript
  console.log('text' / 2);  // NaN
  console.log(NaN + 1);     // NaN (sticky property)
  ```

### 2. BigInt 
For integers larger than 2<sup>53</sup>-1 (Number.MAX_SAFE_INTEGER)

```javascript
const bigInt = 9007199254740991n;
const huge = 1234567890123456789012345678901234567890n;
```

**Key Points:**
- Created by appending `n`
- Can't mix with Number type without explicit conversion
- Not supported in JSON serialization

### 3. String 
Represents textual data with UTF-16 encoding

**Quotation Styles:**
```javascript
let single = 'Single quotes';
let double = "Double quotes";
let backticks = `Backticks support ${double} interpolation`;
```

**Special Features:**
- Template literals (backticks) allow:
  - Multi-line strings
  - Expression embedding (`${...}`)
  - Tagged templates

### 4. Boolean 
Logical values `true` or `false`

```javascript
let isTrue = true;
let isFalse = false;
let result = 5 > 3;  // true
```

**Truthy/Falsy Values:**
- Falsy: `false`, `0`, `""`, `null`, `undefined`, `NaN`
- All other values are truthy

### 5. Null Type
Special value representing intentional absence of any object value

```javascript
let empty = null;
```

**Important Notes:**
- `typeof null` returns `"object"` (historical bug)
- Represents "no value" or "unknown value"

### 6. Undefined 
Value given to uninitialized variables

```javascript
let x;
console.log(x);  // undefined

let obj = {};
console.log(obj.property);  // undefined
```

**Key Behaviors:**
- Default return value of functions
- Different from `null` (which is intentional absence)

### 7. Symbol 
Unique and immutable primitive for object property keys

```javascript
let id = Symbol('description');
let id2 = Symbol('description');

console.log(id === id2);  // false (always unique)
```

**Common Uses:**
- Creating unique property keys
- Implementing private properties
- Well-known symbols for metaprogramming

### 8. Object 
Collection of key-value pairs (non-primitive)

```javascript
let user = {
  name: 'Alice',
  age: 30,
  isAdmin: false
};
```

**Subtypes Include:**
- Plain objects (`{}`)
- Arrays (`[]`)
- Functions
- Dates
- Regular expressions

## Type Conversion and Coercion

### Explicit Conversion
```javascript
let str = '123';
let num = Number(str);  // 123 (number)
```

### Implicit Coercion
```javascript
console.log('5' - 3);  // 2 (number)
console.log('5' + 3);  // '53' (string)
```

## typeof Operator

Returns a string indicating the type of unevaluated operand

```javascript
typeof 42;          // "number"
typeof 'text';      // "string"
typeof true;        // "boolean"
typeof undefined;   // "undefined"
typeof null;        // "object" (historical bug)
typeof {};          // "object"
typeof [];          // "object"
typeof Symbol();    // "symbol"
typeof function(){};// "function"
```

## Type System Summary

| Type       | Category    | Mutable | Example                  |
|------------|-------------|---------|--------------------------|
| number     | Primitive   | No      | `42`, `3.14`             |
| bigint     | Primitive   | No      | `123n`                   |
| string     | Primitive   | No      | `"hello"`, `'world'`     |
| boolean    | Primitive   | No      | `true`, `false`          |
| null       | Primitive   | No      | `null`                   |
| undefined  | Primitive   | No      | `undefined`              |
| symbol     | Primitive   | No      | `Symbol('id')`           |
| object     | Non-primitive | Yes   | `{}`, `[]`, `function()` |
```