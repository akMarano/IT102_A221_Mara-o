import m1.practice10.Maraño_bank_storage as Maraño_bank_storage
import m1.practice10.Maraño_bank_transactions as Maraño_bank_transactions
import m1.practice10.Maraño_bank_utils as Maraño_bank_utils


# Feature: Money Transfer
#
# Moves funds from the logged-in account to another
# existing account on file. Reuses the account's own
# deposit()/withdraw() methods so encapsulation is
# respected, and reuses the existing storage and
# transaction modules instead of duplicating logic.

def transfer_funds(
    sender_account,
    recipient_account_number,
    amount
):

    recipient_account_number = (
        recipient_account_number.strip()
    )

    if recipient_account_number == "":

        return False, (
            "Please enter a recipient "
            "account number."
        )

    if (
        recipient_account_number
        == sender_account.account_number
    ):

        return False, (
            "You cannot transfer funds "
            "to your own account."
        )

    if not Maraño_bank_utils.is_valid_amount(
        amount
    ):

        return False, "Invalid transfer amount."

    if amount > sender_account.check_balance():

        return False, "Insufficient balance."

    recipient_account = (
        Maraño_bank_storage.find_account(
            recipient_account_number
        )
    )

    if recipient_account is None:

        return False, (
            "Recipient account not found."
        )

    withdrawn = sender_account.withdraw(amount)

    if not withdrawn:

        return False, (
            "Transfer failed. Please try again."
        )

    recipient_account.deposit(amount)

    Maraño_bank_storage.update_account(
        sender_account
    )

    Maraño_bank_storage.update_account(
        recipient_account
    )

    Maraño_bank_transactions.record_transaction(
        sender_account,
        f"Transfer Out (to {recipient_account_number})",
        amount
    )

    Maraño_bank_transactions.record_transaction(
        recipient_account,
        f"Transfer In (from {sender_account.account_number})",
        amount
    )

    return True, (
        f"Successfully transferred "
        f"{Maraño_bank_utils.format_currency(amount)} "
        f"to {recipient_account.account_name}."
    )


"""
######### Learning Signature ######### 
Programmed by: Arem Kein I. Maraño
Date Submitted: September 6, 2026

Program Description: New feature module for Money Transfer. Reuses the existing BankAccount.deposit()/withdraw() methods, the storage module's
                     find_account()/update_account(), and the transactions module's record_transaction() instead of writing new file I/O logic.

Reflection: Building this feature on top of the existing modules confirmed why the original code was split into account/storage/transactions/utils in the
            first place: a brand-new feature only needed one new file, and it could still call into every existing safeguard (encapsulated balance updates,
            duplicate-free persistence, and consistent transaction logging).
AI Usage
[ ] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[/] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""
