class Account:

    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance
 
    def check_balance(self):
        print(f"Current Balance: ₱{self._balance:.2f}")
 
    def deposit(self, amount):

        if amount > 0:
            self._balance += amount
            return True
        else:
            print("Invalid deposit amount.")
            return False
    
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False  

account = Account("Arem Kein I. Maraño", 1000.00)
"""
######### Learning Signature ######### 
Programmed by: Arem Kein I. Maraño
Date Submitted: September 2, 2026
 
Program Description: This program simulates a simple ATM account system where users can check their balance, deposit funds, and withdraw funds.
Reflection: I learned how to implement basic banking operations using object-oriented programming in Python.
AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""
