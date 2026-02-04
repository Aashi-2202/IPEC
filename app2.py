import streamlit as st

st.title("my age and city app")

age = st.slider("enter your age", 1, 100)
city = st.selectbox("select your city", ["mumbai", "delhi", "chennai", "kolkata"])

if st.button("show details"):
    st.write("your age is", age)
    st.write("you live in", city)

