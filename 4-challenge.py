#! /usr/bin/env python3

# OBJECT ORIENTED PROGRAMMING CHALLENGE

# Create a bank account class that has two attributes:
# - owner
# - balance
# and two methods:
# - deposit
# - withdraw
# As an added requirement, withdrawals may not exceed
# the available balance.
# Instantiate your class, make several deposits and
# withdrawals, and test to make sure the account can't
# be overdrawn.

class Account:
    
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, added_amount):
        self.balance += added_amount
        print("Deposit Accepted")
        print(f"Current balance: ${self.balance}")
    
    def withdraw(self, deducted_amount):
        if deducted_amount <= self.balance:
            self.balance -= deducted_amount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")
        
        print(f"Current balance: ${self.balance}")
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

# 1. Instantiate the class
acct1 = Account("Jack", 100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

# =====================================================

# class Simple():
    
#     def __init__(self, value):
#         self.value = value
    
#     def add_to_value(self, amount):
#         self.value = self.value + amount

# myobj = Simple(300)
# myobj.value
# myobj.add_to_value(500)
# myobj.value