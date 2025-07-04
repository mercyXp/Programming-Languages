# The Modern Mode: "use strict"

For a long time, JavaScript evolved without compatibility issues. New features were added to the language while old functionality didn’t change.

That had the benefit of never breaking existing code. But the downside was that any mistake or an imperfect decision made by JavaScript’s creators got stuck in the language forever.

This was the case until 2009 when ECMAScript 5 (ES5) appeared. It added new features to the language and modified some of the existing ones. To keep the old code working, most such modifications are off by default. You need to explicitly enable them with a special directive: "use strict".

### Using Strict Mode
```javascript
"use strict";

// This code works in modern way
// ...
```

### Key Points:
1. **Placement Matters**:
   - Must be at the **top** of scripts/functions
   - Below code ignores it:
     ```javascript
     alert("code");
     "use strict"; // Ignored (not at top)
     ```

2. **Scope**:
   - Can be used for entire scripts or individual functions
   - Modules and classes enable it automatically

3. **No Going Back**:
   - Once enabled, cannot be canceled
   - No counterpart like `"no use strict"`

4. **Browser Console**:
   - Doesn't use strict by default
   - Workarounds:
     ```javascript
     'use strict'; <Shift+Enter>
     // Your code
     ```
     Or:
     ```javascript
     (function() {
       'use strict';
       // Your code
     })()
     ```


