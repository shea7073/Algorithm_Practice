class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        b = self.balance + amount
        self.balance = b
        print(f"Your new balance is {self.balance}")
        return b

    def withdraw(self, amount):
        if amount > self.balance:
            return f"{amount} is more than you have nigga"
        else:
            b = self.balance - amount
            self.balance = b
        return b

    def __str__(self):
        return f"{self.owner} has {self.balance} in his account"


money = Account("Sean", 100)

print(money)
print(money.deposit(100))
print(money)
print(money.withdraw(250))
print(money.withdraw(75))
print(money)