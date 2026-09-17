import streamlit as st
from vendoMachine import VendoMachine

def main():
    st.set_page_config(page_title="Water Refilling Vendo", page_icon="💧")
    st.title("Water Refilling Vendo Machine")

    if "vendo" not in st.session_state:
        st.session_state.vendo = VendoMachine()

    vendo = st.session_state.vendo

    st.subheader("Available Containers")
    for c in vendo.containers.values():
        st.write(str(c))

    st.subheader("Make a Transaction")

    choice_labels = {
        0: "-- Select a container --",
        1: "1. 500 mL Bottle (₱10)",
        2: "2. 1 Liter Bottle (₱15)",
        3: "3. 5 Liter Container (₱40)",
    }

    choice = st.selectbox(
        "Choose a container:",
        options=list(choice_labels.keys()),
        format_func=lambda x: choice_labels[x],
    )

    payment = st.number_input("Enter payment amount (₱):", min_value=0, step=1)

    if st.button("Process Transaction"):
        if choice == 0:
            st.warning("Please select a container first.")
        else:
            result = vendo.process_transaction(choice, int(payment))
            st.divider()

            if not result.success:
                if result.container is not None:
                    st.write(f"**Container:** {result.container.name}")
                    st.write(f"**Price:** ₱{result.container.price}")
                st.error(result.message)
            else:
                st.write(f"**Container:** {result.container.name}")
                st.write(f"**Price:** ₱{result.container.price}")
                st.success(f"Change: ₱{result.change}")

                st.write("**Denomination Breakdown:**")
                for bill, count in result.breakdown.items():
                    st.write(f"₱{bill}: {count}")

    st.divider()
    if st.button("Exit"):
        st.write("Thank you for using the Water Refilling Vendo Machine!")
        st.stop()


if __name__ == "__main__":
    main()