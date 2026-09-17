class Container:

    def __init__(self, choice_number, name, price):
        self.choice_number = choice_number
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.choice_number}. {self.name} - ₱{self.price}"