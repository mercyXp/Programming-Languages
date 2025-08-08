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