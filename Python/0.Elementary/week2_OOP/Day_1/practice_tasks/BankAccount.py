class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.__balance = initial_balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f} to {self.owner_name}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.owner_name}'s account.")

    def show_balance(self):
        print(f"{self.owner_name}'s current balance: ${self.__balance:.2f}")

account = BankAccount("Alice", 100)
account.show_balance()       
account.deposit(50)           
account.withdraw(30)          
account.show_balance()        
