import streamlit as st

# Title of the app
st.title("Name Personality Checker")

# Input field for the user's name
name = st.text_input("Enter your name:")

# Logic to display personalized message
if name:
    if name == "Jitesh":
        st.success("You are a true hero")
    elif name == "Jyotika":
        st.warning("You have a devil in your heart")
    elif name == "Jeshika":
        st.error("You are too stubborn, always trying to pick a fight with others!!!!")
    else:
        st.info("You are always right")
