# Tasks for practice

###  Task 1
In this challenge, you'll implement a banking system. You'll create a `BankAccount` class in one file and use it in another file, demonstrating how to organize your code for better maintainability.

You need to work with two files:

`bank_account.py`: Where you'll define your BankAccount class.
`driver.py`: Where you'll import the class, create an account, and perform transactions.

Create a BankAccount class in `bank_account.py` with:

- A class attribute bank_name set to "Python National Bank"
- A method deposit that takes an amount and adds it to the account's balance
- A method withdraw that takes an amount and subtracts it from the balance
- A method get_balance that returns the current balance
- Then in driver.py, import your BankAccount class, create an account, deposit `$100`, withdraw `$30`, and print the balance with format: `f"Current balance: ${my_account.get_balance()}`"

### Task 2
You are given Python files (`book.py` and `driver.py`) to implement a book management system. In this challenge, you'll define a Book class in one file that will be imported and used in another.

Your task is to:

- Complete the Book class in `book.py` with an `__init__ ` method that initializes title, author, and pages attributes
- The `driver.py` file will import and use your Book class to create a book object for "Harry Potter" by "J.K. Rowling" with 400 pages

### Task 3
### Calculator Project

Your Calculator class in `calculator.py` should:

- Have a constructor that initializes a `result` attribute to 0  
- Include methods for `add`, `subtract`, `multiply`, and `divide` that each:
  - Take a number as an argument  
  - Perform the operation between the current `result` and the number  
  - Update the `result` attribute  
  - Return the new result  
- Include a `clear` method that resets the result to 0  
- Include a `get_result` method that returns the current result  

For the `divide` method, you must handle division by zero by:
- Checking if the provided number equals 0  
- If it is zero, print exactly: `"Error: Division by zero"`  
- Leave the `result` attribute unchanged in this case  
- Return the unchanged result value  

The `driver.py` file will import your Calculator class and test it with code similar to this:

```python
from calculator import Calculator

calc = Calculator()
calc.add(5)       # result becomes 5
calc.multiply(3)  # result becomes 15
calc.subtract(2)  # result becomes 13
calc.divide(0)    # prints "Error: Division by zero", result remains 13
calc.divide(2)    # result becomes 6.5
calc.clear()      # result becomes 0
