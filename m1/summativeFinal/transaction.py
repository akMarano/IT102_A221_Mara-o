class Transaction:
    def __init__(self):
        self.success = False
        self.message = ""
        self.container = None
        self.payment = 0
        self.change = 0
        self.breakdown = {}