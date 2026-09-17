from container import Container
from transaction import Transaction

class VendoMachine:
    denominations = [20, 10, 5, 1]

    def __init__(self):
        self.containers = {
            1: Container(1, "500 mL Bottle", 10),
            2: Container(2, "1 Liter Bottle", 15),
            3: Container(3, "5 Liter Container", 40),
        }

    def get_container(self, choice):
        return self.containers.get(choice)

    def compute_breakdown(self, change):
        breakdown = {}
        remaining = change
        for bill in self.denominations:
            count = remaining // bill
            breakdown[bill] = count
            remaining -= count * bill
        return breakdown

    def process_transaction(self, choice, payment):

        result = Transaction()
        container = self.get_container(choice)

        if container is None:
            result.success = False
            result.message = "Invalid selection."
            return result

        result.container = container
        result.payment = payment

        if payment < container.price:
            result.success = False
            result.message = "Insufficient payment."
            return result
            
        change = payment - container.price
        result.success = True
        result.change = change
        result.breakdown = self.compute_breakdown(change)
        return result