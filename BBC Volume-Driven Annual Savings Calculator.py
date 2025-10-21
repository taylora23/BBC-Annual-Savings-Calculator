# === Streamlit Calculator ===

import streamlit as st

st.set_page_config(page_title="BBC Loader and HGV Driver Volume-Driven Annual Savings Calculator", layout="wide")

st.image("Ambitions Public Sector Logo.png", width=240)
st.markdown(
    "<h1 style='font-size: 40px;'>BBC Loader and HGV Driver Volume-Driven Annual Savings Calculator</h1>",
    unsafe_allow_html=True
)

fixed_number_1 = 9469.21
fixed_number_2 = 10392.27

st.markdown(
    '<p style="font-size:30px;">Enter the quantity of loader workers:</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="font-size:30px;">Enter the quantity of HGV driver workers:</p>',
    unsafe_allow_html=True
)

user_input = st.number_input(
  "", min_value=1, step=1, format="%d")

result_1 = user_input * fixed_number_1
result_2 = user_input * fixed_number_2

total_result = result_1 + result_2

formatted_result = f"£{total_result:,.2f}"

st.markdown(
    f"""
    <p style='color:red; font-size:40px; font-weight:bold; text-align:center;'>
        Annual Savings Achieved: {formatted_result}
    </p>
    """,
    unsafe_allow_html=True
)