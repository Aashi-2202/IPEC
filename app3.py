import streamlit as st

st.title("basic calculator app")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

operation = st.selectbox("select operation:", ["Add", "Subs", "Multiply", "Divide"])

if st.button("calculator"):
    if operation == "Add":
        st.write(num1+num2)
    elif operation == "Subs":
        st.write(num1-num2)
    elif operation == "Multiply":
        st.write(num1*num2)
    elif operation == "Divide":
        if num2 !=0:
            st.write(num1/num2)
        else:
            st.error("division is not allowed")