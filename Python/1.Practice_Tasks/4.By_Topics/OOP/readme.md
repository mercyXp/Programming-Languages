# Tasks for practice

### 1. Task 1
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