from datetime import datetime

from m1.practice10 import Maraño_bank_utils


TRANSACTIONS_FILE = "transactions.txt"


def record_transaction(
    account,
    transaction_type,
    amount
):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        TRANSACTIONS_FILE,
        "a"
    ) as file:

        file.write(
            f"Timestamp: {timestamp}\n"
        )

        file.write(
            f"Account Number: "
            f"{account.account_number}\n"
        )

        file.write(
            f"Account: "
            f"{account.account_name}\n"
        )

        file.write(
            f"Account Type: "
            f"{account.get_account_type()}\n"
        )

        file.write(
            f"Transaction: "
            f"{transaction_type}\n"
        )

        file.write(
            f"Amount: "
            f"{Maraño_bank_utils.format_currency(amount)}\n"
        )

        file.write(
            f"Balance After: "
            f"{Maraño_bank_utils.format_currency(account.check_balance())}\n"
        )

        file.write("\n")

def get_transactions():

    transactions = []

    try:

        with open(
            TRANSACTIONS_FILE,
            "r"
        ) as file:

            lines = file.readlines()

    except FileNotFoundError:

        return transactions

    current = {}

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("Timestamp:"):

            current["timestamp"] = (
                line
                .replace(
                    "Timestamp:",
                    ""
                )
                .strip()
            )

        elif line.startswith("Account Number:"):

            current["account_number"] = (
                line
                .replace(
                    "Account Number:",
                    ""
                )
                .strip()
            )

        elif line.startswith("Account:"):

            current["account"] = (
                line
                .replace(
                    "Account:",
                    ""
                )
                .strip()
            )

        elif line.startswith("Account Type:"):

            current["account_type"] = (
                line
                .replace(
                    "Account Type:",
                    ""
                )
                .strip()
            )

        elif line.startswith("Transaction:"):

            current["transaction"] = (
                line
                .replace(
                    "Transaction:",
                    ""
                )
                .strip()
            )

        elif line.startswith("Amount:"):

            amount_text = (
                line
                .replace(
                    "Amount: ₱",
                    ""
                )
                .replace(
                    ",",
                    ""
                )
                .strip()
            )

            try:

                current["amount"] = float(
                    amount_text
                )

            except ValueError:

                current["amount"] = 0.0

        elif line.startswith("Balance After:"):

            balance_text = (
                line
                .replace(
                    "Balance After: ₱",
                    ""
                )
                .replace(
                    ",",
                    ""
                )
                .strip()
            )

            try:

                current["balance_after"] = (
                    float(balance_text)
                )

            except ValueError:

                current["balance_after"] = 0.0

            if (
                "timestamp" in current
                and
                "account_number" in current
                and
                "transaction" in current
                and
                "amount" in current
            ):

                transactions.append(
                    current.copy()
                )

            current = {}

    return transactions

"""
######### Learning Signature ######### 
Programmed by: Arem Kein I. Maraño
Date Submitted: September 5, 2026

Program Description: I changed the hand-written f'₱{amount:.2f}' formatting in record_transaction() to 
                      call Maraño_bank_utils.format_currency(amount) instead, reusing the same helper the 
                      rest of the app already relies on.
                      
Reflection: I learned that duplicating formatting logic across files creates a maintenance risk,
            if the currency format ever needs to change, relying on one shared function means I'd 
            only have to update it in a single place.
AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""