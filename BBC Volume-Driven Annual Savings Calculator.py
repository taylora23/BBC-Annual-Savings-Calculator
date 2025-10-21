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

loader_qty = st.number_input("", min_value=0, step=1, format="%d", key="loader_input")

result_1 = fixed_number_1 * loader_qty

st.markdown(
    '<p style="font-size:30px;">Enter the quantity of HGV driver workers:</p>',
    unsafe_allow_html=True
)

driver_qty = st.number_input("", min_value=0, step=1, format="%d", key="driver_input")

result_2 = fixed_number_2 * driver_qty

if st.button("Calculate Savings"):
    result_1 = fixed_number_1 * loader_qty
    result_2 = fixed_number_2 * driver_qty
    total_result = result_1 + result_2
    formatted_result = f"£{total_result:,.2f}"

    st.markdown(
        f"""
        <p style='color:red; font-size:40px; font-weight:bold; text-align:center;'>
            Total Annual Savings Achieved: {formatted_result}
        </p>
        """,
        unsafe_allow_html=True
    )







