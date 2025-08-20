import streamlit as st

st.title("ברוך הבא לאפליקציה שלי")
name = st.text_input("מה השם שלך?")
if st.button("הצג ברכה"):
    st.write(f"היי {name}, שמח לראות אותך!")
