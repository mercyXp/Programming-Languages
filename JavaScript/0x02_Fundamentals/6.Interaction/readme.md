
# Browser Interaction Methods: `alert`, `prompt`, and `confirm`

This document explains three browser-specific functions for user interaction: `alert`, `prompt`, and `confirm`.

## `alert`

Displays a message and waits for the user to press "OK".

**Syntax:**
```javascript
alert(message);
```

**Example:**
```javascript
alert("Hello");
```

**Key Points:**
- Shows a modal window (blocks interaction with the page until dismissed)
- Only has an "OK" button
- Window appearance and position are browser-determined

## `prompt`

Displays a message, an input field, and OK/Cancel buttons.

**Syntax:**
```javascript
result = prompt(title, [default]);
```

**Parameters:**
- `title`: Text to display to the user
- `default` (optional): Initial value for the input field

**Returns:**
- The entered text if OK is pressed
- `null` if Cancel is pressed or Esc is hit

**Example:**
```javascript
let age = prompt('How old are you?', 100);
alert(`You are ${age} years old!`);
```

**Internet Explorer Note:**
Always provide a default value in IE to avoid "undefined" appearing in the prompt:
```javascript
let test = prompt("Test", ''); // Recommended for IE compatibility
```

## `confirm`

Displays a message with OK and Cancel buttons.

**Syntax:**
```javascript
result = confirm(question);
```

**Returns:**
- `true` if OK is pressed
- `false` if Cancel is pressed or Esc is hit

**Example:**
```javascript
let isBoss = confirm("Are you the boss?");
alert(isBoss); // true or false
```

## Summary Table

| Method    | Purpose | Returns | Modal |
|-----------|---------|---------|-------|
| `alert`   | Show message | - | Yes |
| `prompt`  | Get text input | String or `null` | Yes |
| `confirm` | Get yes/no answer | Boolean | Yes |

## Limitations

1. **Appearance Control:**
   - Window location is browser-determined (usually centered)
   - Visual styling depends on the browser

2. **Modal Behavior:**
   - Pauses script execution
   - Blocks page interaction until dismissed

These methods provide simple but limited interaction. For more sophisticated UI, consider custom modal dialogs.
```

