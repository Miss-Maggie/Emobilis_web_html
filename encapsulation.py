class BankAccount:
    def __init__(self, owner, balance):
        self.name = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("You cannot withdraw money, Insuffient amount")

    def get_balance(self):
        return self.balance

#object
account = BankAccount("John", 500)
account.deposit(100)
account.withdraw(550)
print("Balance", account.get_balance())
