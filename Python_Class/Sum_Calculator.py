# Sum_Calculator.py

import streamlit as st
import pandas as pd

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Streamlit App UI
st.set_page_config(page_title="Sum Calculator", layout="centered")
st.title("🔢 Sum Calculator")
st.write("Enter a number `n` to find the sum from 1 to `n`.")

n = st.number_input("Enter a positive integer", min_value=1, step=1)

if st.button("Calculate"):
    # Calculate sum
    result = calculate_sum(n)
    st.success(f"✅ The sum from 1 to {n} is: {result}")
    
    # Generate data for chart
    data = pd.DataFrame({
        "Number": list(range(1, n + 1)),
        "Value": list(range(1, n + 1))
    })

    # Visual Representation
    st.subheader("📊 Visual Representation")
    st.write("Each bar below represents the value being added from 1 to n.")
    st.bar_chart(data.set_index("Number"))
