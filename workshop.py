import pandas as pd
import streamlit as st


st.title("My First Streamlit App")
st.header("Hello World 👏")
st.write("This is an example of a simple Streamlit app.")

df = pd.read_csv("datasets/1642645053.csv", encoding="tis-620")
st.write(df)

number = st.slider("Select a number", 0, 100, 50)
st.write("The current number is ", number)

rating = st.radio(
    "How would you rate this class?",
    ("1", "2", "3", "4", "5")
)
st.write(f"You selected {rating}")

# Button
button = st.button("Click Me")
if button: # button is True if clicked
    st.write("You clicked the button")

# Dropdown
fruit = st.selectbox("Select your favorite fruit:", ["Apple", "Banana", "Orange", "Grapes", "Mango"])
st.write(f"You selected: {fruit}")