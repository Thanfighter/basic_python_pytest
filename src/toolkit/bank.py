class InsufficientFundsError(Exception):
    """Raised when you try to withdraw more than the balance."""


class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Starting balance cannot be negative")
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough money in the account")
        self.balance -= amount