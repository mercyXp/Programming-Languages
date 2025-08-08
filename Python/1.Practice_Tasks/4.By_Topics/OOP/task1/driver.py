from bank_account import BankAccount

my_account = BankAccount()
my_account.balance = 0

my_account.deposit(100)
my_account.withdraw(30)

print(f"Current balance: ${my_account.get_balance()}")
