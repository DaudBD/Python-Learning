
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, acc_no, acc_holder, balance=0):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_balance(self):
        print(f"Account: {self.acc_no} | Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, acc_no, acc_holder, balance=0, interest_rate=0.05):
        super().__init__(acc_no, acc_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")


# ব্যবহার:
acc = SavingsAccount("ACC101", "Rahim", 5000)
acc.deposit(2000)
acc.withdraw(1500)
acc.show_balance()