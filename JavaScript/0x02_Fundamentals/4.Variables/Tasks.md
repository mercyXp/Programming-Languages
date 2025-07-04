
# Tasks

## Task 1: Working with variables
**Importance: 2**

1. Declare two variables: `admin` and `name`.
2. Assign the value `"John"` to `name`.
3. Copy the value from `name` to `admin`.
4. Show the value of `admin` using `alert` (must output "John").

---

## Task 2: Giving the right name
**Importance: 3**

1. Create a variable with the name of our planet. How would you name such a variable?
2. Create a variable to store the name of a current visitor to a website. How would you name that variable?

---

## Task 3: Uppercase const?
**Importance: 4**

Examine the following code:

```javascript
const birthday = '18.04.1982';
const age = someCode(birthday);
```

Here we have:
- A constant `birthday` for the date
- A constant `age` calculated from `birthday` using `someCode()` (a function that calculates age)

**Questions:**
1. Would it be right to use upper case for `birthday`?
2. Would it be right to use upper case for `age`?
3. Should both be uppercase?

Example alternative:
```javascript
const BIRTHDAY = '18.04.1982'; // make birthday uppercase?
const AGE = someCode(BIRTHDAY); // make age uppercase?
```

Consider the conventions for naming constants in your answer.
```
