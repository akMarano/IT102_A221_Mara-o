from datetime import datetime

import m1.practice10.Maraño_bank_transactions as Maraño_bank_transactions
import m1.practice10.Maraño_bank_utils as Maraño_bank_utils


# Feature: Account Statement Export
#
# Builds a plain-text statement of an account's transactions
# within a chosen date range, with a money-in/money-out summary,
# so it can be shown on screen or downloaded as a file. Reuses
# the existing transactions module instead of reading any file
# directly.

def generate_statement(
    account,
    start_date,
    end_date
):

    if start_date > end_date:

        return False, (
            "Start date cannot be "
            "after end date."
        ), ""

    all_transactions = (
        Maraño_bank_transactions
        .get_transactions()
    )

    account_transactions = [
        transaction
        for transaction in all_transactions
        if transaction.get(
            "account_number"
        ) == account.account_number
    ]

    filtered_transactions = []

    for transaction in account_transactions:

        timestamp_text = transaction.get(
            "timestamp",
            ""
        )

        try:

            transaction_date = datetime.strptime(
                timestamp_text,
                "%Y-%m-%d %H:%M:%S"
            ).date()

        except ValueError:

            continue

        if start_date <= transaction_date <= end_date:

            filtered_transactions.append(
                transaction
            )

    if not filtered_transactions:

        return False, (
            "No transactions found "
            "in the selected date range."
        ), ""

    total_in = 0.0
    total_out = 0.0

    for transaction in filtered_transactions:

        transaction_type = transaction.get(
            "transaction",
            ""
        )

        amount = transaction.get(
            "amount",
            0.0
        )

        if (
            transaction_type.startswith("Deposit")
            or
            transaction_type.startswith("Transfer In")
        ):

            total_in += amount

        elif (
            transaction_type.startswith("Withdraw")
            or
            transaction_type.startswith("Transfer Out")
        ):

            total_out += amount

    statement_lines = [
        "========================================",
        "      MARAÑO BANK ACCOUNT STATEMENT",
        "========================================",
        f"Account Name:   {account.account_name}",
        f"Account Number: {account.account_number}",
        f"Account Type:   {account.get_account_type()}",
        f"Period:         "
        f"{start_date.strftime('%Y-%m-%d')} to "
        f"{end_date.strftime('%Y-%m-%d')}",
        "----------------------------------------",
    ]

    for transaction in filtered_transactions:

        statement_lines.append(
            f"{transaction.get('timestamp', 'N/A')}  "
            f"{transaction.get('transaction', 'N/A')}  "
            f"{Maraño_bank_utils.format_currency(transaction.get('amount', 0.0))}"
        )

    statement_lines.append(
        "----------------------------------------"
    )

    statement_lines.append(
        f"Total Transactions: "
        f"{len(filtered_transactions)}"
    )

    statement_lines.append(
        f"Total Money In:     "
        f"{Maraño_bank_utils.format_currency(total_in)}"
    )

    statement_lines.append(
        f"Total Money Out:    "
        f"{Maraño_bank_utils.format_currency(total_out)}"
    )

    statement_lines.append(
        f"Net Change:         "
        f"{Maraño_bank_utils.format_currency(total_in - total_out)}"
    )

    statement_lines.append(
        f"Ending Balance:     "
        f"{Maraño_bank_utils.format_currency(account.check_balance())}"
    )

    statement_lines.append(
        "========================================"
    )

    statement_text = "\n".join(statement_lines)

    return True, "Statement generated successfully.", statement_text


"""
######### Learning Signature ######### 
Programmed by: Arem Kein I. Maraño
Date Submitted: September 6, 2026

Program Description: New feature module for Account Statement Export. Filters the
                    account's transactions to a chosen date range using the
                    existing transactions module, tallies money in vs. money out,
                    and formats everything into a downloadable plain-text
                    statement.

Reflection: This feature didn't need any new persistence or changes to the account
            object, since transaction history is already logged; it only needed
            to read, filter, and format data the rest of the app already collects,
            the same way the analysis module summarizes transactions without
            touching storage.
AI Usage
[ ] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[/] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""
