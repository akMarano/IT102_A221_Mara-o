import streamlit as st
from transaction import Transaction


st.title("Snack Kiosk")
 
st.subheader("Select an item")
col1, col2, col3 = st.columns(3)
water = col1.button("Water\n₱20", use_container_width=True)
soda = col2.button("Soda\n₱25", use_container_width=True)
chips = col3.button("Chips\n₱30", use_container_width=True)
 
if water:
    st.session_state.item = "Water"
    st.session_state.price = 20
elif soda:
    st.session_state.item = "Soda"
    st.session_state.price = 25
elif chips:
    st.session_state.item = "Chips"
    st.session_state.price = 30
 
if "item" in st.session_state:
    st.write(f"Selected: {st.session_state.item} (₱{st.session_state.price})")
 
    money = st.number_input("Enter amount of money (₱)", min_value=0, step=1)
 
    if st.button("Process Transaction"):
        transaction = Transaction(st.session_state.item, st.session_state.price, money)
 
        st.write(f"Item: {transaction.get_item()}")
        st.write(f"Price: ₱{transaction.get_item_price()}")
 
        if transaction.get_money() < transaction.get_item_price():
            st.error("Insufficient payment.")
        else:
            st.success(f"Change: ₱{transaction.get_change()}")
 

