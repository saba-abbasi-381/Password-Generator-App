import streamlit as st

from random_password_generator import password_generator

st.title("Password Generator")
st.subheader("Generate a strong and secure password easily.")
password_length = st.number_input("Enter password length", min_value= 1, max_value=50, step=1)

use_symbols = st.checkbox("Include symbols")

if st.button("Generate Password"):
    response = password_generator(password_length, use_symbols)
    if "Sorry" in response:
        st.error(response)
    else:
        st.success(f"Your password: {response}")

