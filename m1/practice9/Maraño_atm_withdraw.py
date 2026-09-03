from datetime import datetime
from Maraño_atm_account import Account

def withdraw_money(account, amount):

    if amount <= 0:
        return False

    success = account.withdraw(amount)

    if success:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open("transactions.txt", "a") as file:

            file.write(
                f"Timestamp: {timestamp}\n"
            )

            file.write(
                f"Account: {account.account_name}\n"
            )

            file.write(
                "Transaction: Withdraw\n"
            )

            file.write(
                f"Amount: ₱{amount:.2f}\n\n"
            )

        return True

    return False

account = Account("Arem Kein I. Maraño", 1000.0)
withdraw_money(account, 200.0)

"""
######### Learning Signature ######### 
Programmed by: Arem Kein I. Maraño
Date Submitted: September 3, 2026
 
Program Description: This program simulates a simple ATM account system where users can withdraw funds from their account.
Reflection: I learned how to implement basic banking operations using object-oriented programming in Python.
AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""