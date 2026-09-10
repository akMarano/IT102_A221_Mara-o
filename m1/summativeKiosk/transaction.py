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

    