class Transaction:

    def __init__(self, item, price, money):
        self.item = item
        self.itemPrice = price
        self.money = money

    def get_item(self):
        return self.item

    def get_item_price(self):
        return self.itemPrice

    def get_money(self):
        return self.money

    def get_change(self):
        return self.money - self.itemPrice

"""
######### Learning Signature ######### 
Programmed by: Arem Kein I. Maraño
Date Submitted: September 10, 2026
 
Program Description: This is a the class that handles the transactions for the snack kiosk application. 
                     It takes the selected item, its price, and the amount of money provided by the user, 
                     and provides methods to retrieve these values as well as calculate any change due.

Reflection: I applied the knowledge I gained from the previous lessons to create a class that encapsulates 
            the transaction logic for the snack kiosk application.
            
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""