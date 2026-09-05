"""
######### Learning Signature ######### 
Programmed by: Arem Kein I. Maraño
Date Submitted: September 5, 2026
 
Program Description: Removed the sidebar and replaced it with a dashboard page that has Quick Action buttons (Deposit, Withdraw, History,
                     Analysis) and a Back button to return. Moved all colors and fonts into config.toml instead of styling each widget.

Reflection: I learned that config.toml is where app-wide colors and fonts should go, and that using session_state to track the current 
            page is a simpler way to handle navigation than a sidebar menu.
AI Usage
[ ] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[/] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""

import streamlit as st

import m1.practice10.Maraño_bank_auth as Maraño_bank_auth
import m1.practice10.Maraño_bank_storage as Maraño_bank_storage
import m1.practice10.Maraño_bank_transactions as Maraño_bank_transactions
import m1.practice10.Maraño_bank_analysis as Maraño_bank_analysis
import m1.practice10.Maraño_bank_utils as Maraño_bank_utils


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Maraño Bank",
    page_icon=":bank:",
    layout="wide"
)


# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "account" not in st.session_state:

    st.session_state.account = None


if "page" not in st.session_state:

    st.session_state.page = "Dashboard"


# ==========================================
# BANK HEADER
# ==========================================

with st.container():

    header_left, header_right = st.columns(
        [4, 1],
        vertical_alignment="center"
    )

    with header_left:

        st.title("Maraño Bank")

        st.caption(
            "Secure Digital Banking System"
        )

    with header_right:

        if st.session_state.logged_in:

            if st.button(
                "Logout",
                use_container_width=True
            ):

                st.session_state.logged_in = False

                st.session_state.account = None

                st.session_state.page = "Dashboard"

                st.rerun()

st.write("")


# ==========================================
# LOGIN / REGISTRATION
# ==========================================

if not st.session_state.logged_in:

    center_left, center, center_right = st.columns(
        [1, 2, 1]
    )

    with center:

        with st.container(border=True):

            login_tab, register_tab = st.tabs(
                [
                    "Login",
                    "Register"
                ]
            )

            # ======================================
            # LOGIN
            # ======================================

            with login_tab:

                st.subheader(
                    "Welcome Back"
                )

                st.caption(
                    "Enter your credentials to access your account."
                )

                with st.form(
                    "login_form",
                    border=False
                ):

                    account_number = st.text_input(
                        "Account Number",
                        key="login_account",
                        placeholder="e.g. 000123456"
                    )

                    pin = st.text_input(
                        "PIN",
                        type="password",
                        key="login_pin",
                        placeholder="4-digit PIN"
                    )

                    st.write("")

                    login_submitted = st.form_submit_button(
                        "Login",
                        use_container_width=True,
                        type="primary"
                    )

                if login_submitted:

                    with st.spinner("Verifying credentials..."):

                        account, message = (
                            Maraño_bank_auth
                            .login_account(
                                account_number,
                                pin
                            )
                        )

                    if account is not None:

                        st.session_state.logged_in = True

                        st.session_state.account = (
                            account
                        )

                        st.session_state.page = "Dashboard"

                        st.toast(message)

                        st.rerun()

                    else:

                        st.error(message)

            # ======================================
            # REGISTRATION
            # ======================================

            with register_tab:

                st.subheader(
                    "Create Your Maraño Bank Account"
                )

                st.caption(
                    "Fill in the details below to open a new account."
                )

                with st.form(
                    "register_form",
                    border=False
                ):

                    name = st.text_input(
                        "Full Name",
                        key="register_name",
                        placeholder="Juan Dela Cruz"
                    )

                    reg_col1, reg_col2 = st.columns(2)

                    with reg_col1:

                        account_number = st.text_input(
                            "Account Number",
                            key="register_account",
                            placeholder="e.g. 000123456"
                        )

                        pin = st.text_input(
                            "Create 4-Digit PIN",
                            type="password",
                            key="register_pin"
                        )

                    with reg_col2:

                        account_type = st.selectbox(
                            "Account Type",
                            [
                                "Savings Account",
                                "Student Account"
                            ]
                        )

                        confirm_pin = st.text_input(
                            "Confirm PIN",
                            type="password",
                            key="register_confirm_pin"
                        )

                    starting_balance = st.number_input(
                        "Starting Balance",
                        min_value=0.0,
                        step=100.0,
                        format="%.2f"
                    )

                    st.write("")

                    register_submitted = st.form_submit_button(
                        "Create Account",
                        use_container_width=True,
                        type="primary"
                    )

                if register_submitted:

                    with st.spinner("Creating your account..."):

                        account, message = (
                            Maraño_bank_auth
                            .register_account(
                                name,
                                account_number,
                                pin,
                                confirm_pin,
                                account_type,
                                starting_balance
                            )
                        )

                    if account is not None:

                        st.success(message)

                        st.info(
                            "Your account has been created. "
                            "Please use the Login tab."
                        )

                    else:

                        st.error(message)


# ==========================================
# LOGGED-IN BANKING APPLICATION
# ==========================================

else:

    account = (
        st.session_state.account
    )

    page = st.session_state.page


    # ======================================
    # DASHBOARD (HUB)
    # ======================================

    if page == "Dashboard":

        st.header(
            f"Welcome, {account.account_name}"
        )

        st.caption(
            "Here's a quick overview of your account."
        )

        st.write("")


        # ==================================
        # PROFILE
        # ==================================

        with st.container(border=True):

            profile_col1, profile_col2 = st.columns(2)

            with profile_col1:

                st.metric(
                    "Account Type",
                    account.get_account_type()
                )

            with profile_col2:

                st.metric(
                    "Account Number",
                    account.account_number
                )

        st.write("")


        # ==================================
        # BALANCE
        # ==================================

        with st.container(border=True):

            st.metric(
                "Current Balance",
                Maraño_bank_utils
                .format_currency(
                    account.check_balance()
                )
            )

        st.write("")


        # ==================================
        # QUICK ACTIONS
        # ==================================

        action_col1, action_col2, action_col3, action_col4 = st.columns(4)

        with action_col1:

            if st.button(
                "Deposit",
                use_container_width=True,
                type="primary"
            ):

                st.session_state.page = "Deposit"

                st.rerun()

        with action_col2:

            if st.button(
                "Withdraw",
                use_container_width=True,
                type="primary"
            ):

                st.session_state.page = "Withdraw"

                st.rerun()

        with action_col3:

            if st.button(
                "Transaction History",
                use_container_width=True
            ):

                st.session_state.page = "Transaction History"

                st.rerun()

        with action_col4:

            if st.button(
                "Transaction Analysis",
                use_container_width=True
            ):

                st.session_state.page = "Transaction Analysis"

                st.rerun()


    # ======================================
    # NON-DASHBOARD PAGES
    # ======================================

    else:

        if st.button("← Back to Dashboard"):

            st.session_state.page = "Dashboard"

            st.rerun()

        st.write("")


        # ==================================
        # DEPOSIT
        # ==================================

        if page == "Deposit":

            st.header("Deposit Money")

            left, right = st.columns([2, 1])

            with right:

                with st.container(border=True):

                    st.caption("Current Balance")

                    st.subheader(
                        Maraño_bank_utils.format_currency(
                            account.check_balance()
                        )
                    )

            with left:

                with st.container(border=True):

                    with st.form("deposit_form", border=False):

                        amount = st.number_input(
                            "Deposit Amount",
                            min_value=0.0,
                            step=100.0,
                            format="%.2f"
                        )

                        deposit_submitted = st.form_submit_button(
                            "Confirm Deposit",
                            use_container_width=True,
                            type="primary"
                        )

                    if deposit_submitted:

                        if not Maraño_bank_utils.is_valid_amount(
                            amount
                        ):

                            st.error("Invalid deposit amount.")

                        else:

                            success = account.deposit(
                                amount
                            )

                            if success:

                                Maraño_bank_storage.update_account(
                                    account
                                )

                                Maraño_bank_transactions.record_transaction(
                                    account,
                                    "Deposit",
                                    amount
                                )

                                st.success("Deposit successful.")

                                st.metric(
                                    "New Balance",
                                    Maraño_bank_utils
                                    .format_currency(
                                        account.check_balance()
                                    )
                                )


        # ==================================
        # WITHDRAW
        # ==================================

        elif page == "Withdraw":

            st.header("Withdraw Money")

            left, right = st.columns([2, 1])

            with right:

                with st.container(border=True):

                    st.caption("Available Balance")

                    st.subheader(
                        Maraño_bank_utils.format_currency(
                            account.check_balance()
                        )
                    )

            with left:

                with st.container(border=True):

                    with st.form("withdraw_form", border=False):

                        amount = st.number_input(
                            "Withdrawal Amount",
                            min_value=0.0,
                            step=100.0,
                            format="%.2f"
                        )

                        withdraw_submitted = st.form_submit_button(
                            "Confirm Withdrawal",
                            use_container_width=True,
                            type="primary"
                        )

                    if withdraw_submitted:

                        if not Maraño_bank_utils.is_valid_amount(
                            amount
                        ):

                            st.error("Invalid withdrawal amount.")

                        elif amount > account.check_balance():

                            st.error("Insufficient balance.")

                        else:

                            success = account.withdraw(
                                amount
                            )

                            if success:

                                Maraño_bank_storage.update_account(
                                    account
                                )

                                Maraño_bank_transactions.record_transaction(
                                    account,
                                    "Withdraw",
                                    amount
                                )

                                st.success("Withdrawal successful.")

                                st.metric(
                                    "New Balance",
                                    Maraño_bank_utils
                                    .format_currency(
                                        account.check_balance()
                                    )
                                )


        # ==================================
        # TRANSACTION HISTORY
        # ==================================

        elif page == "Transaction History":

            st.header("Transaction History")

            transactions = (
                Maraño_bank_transactions
                .get_transactions()
            )


            # Show only transactions
            # belonging to the logged-in user.

            transactions = [
                transaction
                for transaction in transactions
                if transaction.get(
                    "account_number"
                ) == account.account_number
            ]


            if transactions:

                st.caption(
                    f"Showing {len(transactions)} transaction(s) "
                    f"for this account."
                )

                display_data = []

                for transaction in transactions:

                    display_data.append({

                        "Timestamp":
                            transaction.get(
                                "timestamp",
                                "N/A"
                            ),

                        "Transaction":
                            transaction.get(
                                "transaction",
                                "N/A"
                            ),

                        "Amount":
                            Maraño_bank_utils
                            .format_currency(
                                transaction.get(
                                    "amount",
                                    0
                                )
                            ),

                        "Balance After":
                            Maraño_bank_utils
                            .format_currency(
                                transaction.get(
                                    "balance_after",
                                    0
                                )
                            )
                    })


                st.dataframe(
                    display_data,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info("No transaction history available.")


        # ==================================
        # TRANSACTION ANALYSIS
        # ==================================

        elif page == "Transaction Analysis":

            st.header("Transaction Analysis")

            result = (
                Maraño_bank_analysis
                .analyze_transactions(
                    account.account_number
                )
            )


            # ==============================
            # ANALYSIS 1
            # TRANSACTION SUMMARY
            # ==============================

            st.subheader("1. Transaction Summary")

            with st.container(border=True):

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Total Transactions",
                    result[
                        "total_transactions"
                    ]
                )

                col2.metric(
                    "Deposits",
                    result[
                        "deposits"
                    ]
                )

                col3.metric(
                    "Withdrawals",
                    result[
                        "withdrawals"
                    ]
                )

            st.write("")


            # ==============================
            # ANALYSIS 2
            # MONEY FLOW
            # ==============================

            st.subheader("2. Money Flow Analysis")

            with st.container(border=True):

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Total Deposited",
                    Maraño_bank_utils
                    .format_currency(
                        result[
                            "total_deposited"
                        ]
                    )
                )

                col2.metric(
                    "Total Withdrawn",
                    Maraño_bank_utils
                    .format_currency(
                        result[
                            "total_withdrawn"
                        ]
                    )
                )

                col3.metric(
                    "Net Cash Flow",
                    Maraño_bank_utils
                    .format_currency(
                        result[
                            "net_cash_flow"
                        ]
                    )
                )

            st.write("")


            # ==============================
            # ANALYSIS 3
            # ACCOUNT ACTIVITY
            # ==============================

            st.subheader("3. Account Activity Analysis")
 
            with st.container(border=True):
 
                col1, col2, col3 = st.columns(3)
 
                col1.metric(
                    "Largest Transaction",
                    Maraño_bank_utils
                    .format_currency(
                        result[
                            "largest_transaction"
                        ]
                    )
                )
 
                col2.metric(
                    "Average Transaction",
                    Maraño_bank_utils
                    .format_currency(
                        result[
                            "average_transaction"
                        ]
                    )
                )
 
                col3.metric(
                    "Latest Transaction",
                    result[
                        "latest_transaction"
                    ]
                )
 
                st.caption(
                    f"Latest Activity: "
                    f"{result['latest_timestamp']}"
                )


