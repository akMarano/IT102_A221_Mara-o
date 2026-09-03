def view_history():
    try:
        with open("transactions.txt", "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return []
for line in view_history():
    print(line.strip())

"""
######### Learning Signature ######### 
Programmed by: Arem Kein I. Maraño
Date Submitted: September 3, 2026
 
Program Description: This program simulates a simple ATM account system where users can view their transaction history.
Reflection: I learned how to implement basic banking operations using object-oriented programming in Python.
AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""