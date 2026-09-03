from datetime import datetime

def deposit_money(account, amount):

    if amount <= 0:
        return False

    success = account.deposit(amount)

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
                "Transaction: Deposit\n"
            )

            file.write(
                f"Amount: ₱{amount:.2f}\n\n"
            )

        return True

    return False



"""
######### Learning Signature ######### 
Programmed by: Arem Kein I. Maraño
Date Submitted: September 2, 2026
 
Program Description: This program simulates a simple ATM account system where users can deposit funds into their account.
Reflection: I learned how to implement basic banking operations using object-oriented programming in Python.
AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""






















