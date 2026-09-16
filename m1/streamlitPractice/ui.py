import streamlit as st

st.title("My Streamlit App")
st.header("Welcome to my app!")
st.subheader("This is a subheader")
st.write("Here is some text that explains what my app does.")
st.write("Feel free to explore the different features of this app!")





col1, col2 = st.columns(2)
with col1:
    st.write("Left column")
    agree = st.checkbox("I agree to the terms")
    if agree:
        a = 1 + 2
        st.write("Thanks for agreeing! The result of 1 + 2 is:", a)
with col2:
    st.write("Right column")
    if st.button("Calculate BMI"):
        st.write("Button was clicked!")
        weight = st.number_input("Enter your weight (kg):", min_value=0.0, step=0.1)
        height = st.number_input("Enter your height (m):", min_value=0.0, step=0.01)
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.write("Your BMI is:", bmi)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
