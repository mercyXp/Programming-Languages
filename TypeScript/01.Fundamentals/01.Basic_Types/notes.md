# TypeScript Basics: Understanding Types

This guide covers the fundamental data types in TypeScript — the building blocks you need to write safe, predictable, and scalable JavaScript applications.

---

## 1. Boolean
Represents true/false values.

```ts
let isDone: boolean = false;
````

---

## 2. Number

TypeScript uses `number` for all floating point numbers and supports:

* decimal
* hex
* binary
* octal
* bigint

```ts
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
let big: bigint = 100n;
```

---

## 3. String

Used for text. You can use:

* single quotes
* double quotes
* template strings

```ts
let color: string = "blue";
color = 'red';

let fullName: string = `Bob Bobbington`;
let age: number = 37;

let sentence: string = `Hello, my name is ${fullName}.
I'll be ${age + 1} years old next month.`;
```

---

## 4. Array

Two ways to declare an array of numbers:

```ts
let list: number[] = [1, 2, 3];
let list2: Array<number> = [1, 2, 3];
```

---

## 5. Tuple

A tuple is a fixed-length array with specific types at each index.

```ts
let x: [string, number];
x = ["hello", 10]; // OK
// x = [10, "hello"]; ❌ Error
```

Accessing tuple items:

```ts
console.log(x[0].substring(1)); // OK
// x[1].substring(1); ❌ Error (number has no substring)
```

---

##  6. Enum

Enums give friendly names to numeric values.

```ts
enum Color {
  Red,
  Green,
  Blue,
}

let c: Color = Color.Green;
```

Custom numbering:

```ts
enum Color {
  Red = 1,
  Green,
  Blue,
}
```

Reverse lookup:

```ts
let colorName: string = Color[2]; // "Green"
```

---

## 7. Unknown

Represents a value whose type is not known at compile time.

```ts
let notSure: unknown = 4;
notSure = "maybe a string";
notSure = false;
```

Type narrowing is required:

```ts
declare const maybe: unknown;

if (typeof maybe === "string") {
  let str: string = maybe;
}
```

---

##  8. Any

The `any` type disables type checking.

```ts
declare function getValue(key: string): any;

const str: string = getValue("myString");
```

⚠️ **Avoid using `any` unless necessary** — it removes TypeScript's safety features.

---

## 9. Void

Used mostly for functions that return nothing.

```ts
function warnUser(): void {
  console.log("This is a warning");
}

let unusable: void = undefined;
```

---

## 10. Null & Undefined

Their own types:

```ts
let u: undefined = undefined;
let n: null = null;
```

With `strictNullChecks` OFF → assignable to all types
With `strictNullChecks` ON → only assignable to specific types

---

## 11. Never

Represents a value that never occurs.

Used for functions that never return:

```ts
function error(message: string): never {
  throw new Error(message);
}

function infiniteLoop(): never {
  while (true) {}
}
```

---

## 12. Object

Represents anything that is **not**:

* number
* string
* boolean
* symbol
* null
* undefined

```ts
declare function create(o: object | null): void;

create({ prop: 0 }); // OK
create(null);        // OK
create(42);          // ❌ Error
```

---

##  13. Type Assertions

Tell TypeScript "I know more than you".

Two forms:

### `as` syntax:

```ts
let someValue: unknown = "this is a string";
let strLength: number = (someValue as string).length;
```

### Angle bracket syntax:

```ts
let strLength: number = (<string>someValue).length;
```

Use `as` when working with JSX.

---

##  14. Note About `let`

TypeScript (and modern JavaScript) encourages using:

* `let` (block scoped)
* `const` (constant)

Avoid `var` because it has confusing scoping rules.

---

##  15. Capitalized vs Lowercase Types

❌ Do NOT use:

* `Number`
* `String`
* `Boolean`
* `Symbol`
* `Object`

These refer to *wrapper objects*.

 Use:

* `number`
* `string`
* `boolean`
* `symbol`
* `object`

```ts
function reverse(s: string): string {
  return s.split("").reverse().join("");
}
```

---

##  Summary

| Type             | Purpose                           |
| ---------------- | --------------------------------- |
| boolean          | true/false                        |
| number           | all numeric values                |
| string           | text                              |
| array            | list of values                    |
| tuple            | fixed-length, typed array         |
| enum             | friendly names for numeric values |
| unknown          | safe "any" type                   |
| any              | opt-out of type checking          |
| void             | no return value                   |
| null / undefined | empty values                      |
| never            | function never returns            |
| object           | non-primitive types               |
| type assertion   | manually force a type             |

---


