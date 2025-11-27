class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.account_balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        elif amount > self.account_balance:
            return False
        else:
            return False
    
    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")

#class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.account_balance = initial_balance
    
#     def deposit(self, amount):
#         self.account_balance += amount
    
#     def withdraw(self, amount):
#         self.account_balance -= amount
    
#     def display_balance(self):
#         print(f"Current Balance: ${self.account_balance}")