class BankAccount:
    initial_balance = 500
        
    def deposit(self,owner_name, _balance):
        self.owner_name = owner_name
        self._balance = _balance

        