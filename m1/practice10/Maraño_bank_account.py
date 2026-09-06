"""
OOP Pillar        | Definition & Usage
------------------|---------------------------------------------------------------
Encapsulation     | Defined: self._pin / self._balance kept private in BankAccount, accessed only via check_balance(), deposit(),
                  | withdraw(), verify_pin(), change_pin().
                  |
                  | Usage: Maraño_bank_storage.py never touches account._balance or account._pin directly, it reads/writes only through
                  | account.get_pin() and account.check_balance(). 
------------------|---------------------------------------------------------------
Abstraction       | Defined: BankAccount(ABC) with @abstractmethod get_account_type() defines a required behavior without
                  | implementing it.
                  |  
                  | Usage: Maraño_bank_transfer.py and Maraño_bank_statement.py only call sender_account.withdraw(), recipient_account.deposit(), 
                  | and account.check_balance(), never knowing or caring how balance/PIN are stored internally.
------------------|---------------------------------------------------------------
Inheritance       | Defined: class SavingsAccount(BankAccount) and class StudentAccount(BankAccount) inherit shared logic from BankAccount.
------------------|---------------------------------------------------------------
Polymorphism      | Defined: Each subclass overrides get_account_type() to return its own string, so account.get_account_type()
                  | behaves differently per object type.
                  |
                  | Usage: Maraño_bank_app.py, Maraño_bank_storage.py, Maraño_bank_statement.py, and Maraño_bank_transactions.py
                  | all call account.get_account_type() on whatever account object they're given, without checking whether it's a
                  | SavingsAccount or StudentAccount first.
"""

from abc import ABC, abstractmethod
class BankAccount(ABC):

    def __init__(
        self,
        account_number,
        name,
        pin,
        starting_balance
    ):
        self.account_number = account_number
        self.account_name = name

        # Encapsulation
        self._pin = pin
        self._balance = starting_balance

    # Encapsulation
    def check_balance(self):
        return self._balance

    def deposit(self, amount):

        if amount <= 0:
            return False

        self._balance += amount

        return True

    def withdraw(self, amount):

        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount

        return True

    def verify_pin(self, pin):

        return self._pin == pin

    def get_pin(self):

        return self._pin

    def change_pin(self, old_pin, new_pin):

        if self._pin != old_pin:
            return False

        self._pin = new_pin

        return True

    # Abstraction
    @abstractmethod
    def get_account_type(self):
        pass


# Inheritance
class SavingsAccount(BankAccount):

    # Polymorphism
    def get_account_type(self):

        return "Savings Account"


# Inheritance
class StudentAccount(BankAccount):

    # Polymorphism
    def get_account_type(self):

        return "Student Account"