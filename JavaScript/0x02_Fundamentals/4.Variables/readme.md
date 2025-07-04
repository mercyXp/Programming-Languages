
# JavaScript Variables

## Introduction to Variables
Most applications need to work with information. Examples:
- **Online shop**: Goods, shopping cart data
- **Chat app**: Users, messages, etc.

Variables store this information.

## What is a Variable?
A "named storage" for data. Created using the `let` keyword:

```javascript
let message; // declaration
message = 'Hello'; // assignment
```

Access stored data using the variable name:

```javascript
alert(message); // Shows 'Hello'
```

## Variable Declaration
Combine declaration and assignment:

```javascript
let message = 'Hello!'; // Recommended single-line style
```

Multiple variables (less readable):

```javascript
let user = 'John', age = 25, message = 'Hello';
```

Preferred multi-line style:

```javascript
let user = 'John';
let age = 25;
let message = 'Hello';
```

## `var` vs `let`
Older scripts use `var`:

```javascript
var message = 'Hello'; // Old-school (avoid in modern code)
```

## Variable Analogy
Think of variables as labeled boxes:
- Name = box label
- Value = box content
- Values can be changed:

```javascript
let message = 'Hello';
message = 'World!'; // Value replaced
```

## Copying Variables
```javascript
let hello = 'Hello world';
let message = hello; // Copy value
```

## Declaration Rules
- Declare only once:
```javascript
let message = "This";
let message = "That"; // Error!
```

## Naming Conventions
### Valid Names:
```javascript
let userName;
let test123;
let $ = 1;
let _ = 2;
```

### Invalid Names:
```javascript
let 1a; // No leading digits
let my-name; // No hyphens
```

### Best Practices:
- Use `camelCase`
- Avoid non-Latin characters
- Make names descriptive (e.g., `shoppingCart` not `data`)

## Constants
Use `const` for unchanging values:
```javascript
const MY_BIRTHDAY = '18.04.1982';
MY_BIRTHDAY = '01.01.2001'; // Error!
```

### Uppercase Constants
For hard-coded values:
```javascript
const COLOR_RED = "#F00";
let color = COLOR_RED;
```

## Good Naming Practices
1. Be descriptive (`userName` not `a`)
2. Avoid abbreviations
3. Agree on team terminology
4. Don't reuse variables unnecessarily

## Summary
| Keyword | Usage | Reassignable |
|---------|-------|--------------|
| `let`   | Modern variable | Yes |
| `var`   | Legacy (avoid) | Yes |
| `const` | Constant values | No |

**Remember**: Good variable names make code self-documenting!
```

