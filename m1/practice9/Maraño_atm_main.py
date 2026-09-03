"""
######### Learning Signature ######### 
Programmed by: Arem Kein I. Maraño
Date Submitted: September 3, 2026
 
Program Description: This program creates a simple ATM interface using Streamlit, with options for check balance, 
                     deposit, withdraw, view transaction history, and analyze transactions.
Reflection: I learned how to use Streamlit to create a user-friendly interface for a banking application, integrating 
            various functionalities like balance checking, deposits, withdrawals, and transaction analysis.
AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""
import streamlit as st

from Maraño_atm_account import Account
import Maraño_atm_balance
import Maraño_atm_deposit
import Maraño_atm_withdraw
import Maraño_atm_history
import Maraño_atm_analysis

account = Account("Arem Kein I. Maraño",10000.00)

st.set_page_config(
    page_title="Python ATM",
    page_icon="🏦",
    layout="wide"
)

st.title("PYTHON ATM")

st.write(
    f"Welcome, **{account.account_name}**!"
)

st.divider()
st.sidebar.title("ATM MENU")

choice = st.sidebar.radio(
    "Select an option:",
    [
        "Check Balance",
        "Deposit",
        "Withdraw",
        "View History",
        "Analyze Transactions"
    ]
)

if choice == "Check Balance":

    st.header("Check Balance")

    balance = Maraño_atm_balance.check_balance(account)
    st.metric("Current Balance", f"₱{balance:,.2f}")

elif choice == "Deposit":

    st.header("Deposit Money")

    amount = st.number_input(
        "Enter deposit amount",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Deposit Money"):

        if amount <= 0:

            st.error("Invalid deposit amount.")

        else:

            success = (
                Maraño_atm_deposit.deposit_money(account,amount)
            )

            if success:

                st.success("Deposit successful.")

                st.metric("New Balance",f"₱{account.check_balance():,.2f}")

