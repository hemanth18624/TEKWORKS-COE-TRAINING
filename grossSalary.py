import streamlit as st

def calculate_gross_salary(basic_salary):
    if basic_salary < 0:
        st.error("Salary cannot be negative")
    else:
        if basic_salary < 10000:
            hra = (67 / 100) * basic_salary
            da = (73 / 100) * basic_salary
        elif basic_salary < 20000:
            hra = (69 / 100) * basic_salary
            da = (76 / 100) * basic_salary
        else:
            hra = (73 / 100) * basic_salary
            da = (89 / 100) * basic_salary
        gross_salary = basic_salary + hra + da
        st.success(f"The gross salary is: ₹ {gross_salary:.2f}")

# Streamlit app layout
st.title("Gross Salary Calculator")

# Accept basic salary as input
basic_salary = st.number_input("Enter the employee's basic salary (₹):", min_value=0, step=100)

# Button to calculate the gross salary
if st.button("Calculate Gross Salary"):
    calculate_gross_salary(basic_salary)

