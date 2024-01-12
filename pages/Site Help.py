import streamlit as st
import sendEmail as se
receiver = st.text_input("Enter your email :")
button=st.button("Press to receive help information", key="Submit")

print("Waiting for submit")

if button:
    se.send_mail("lgk09021984@gmail.com","kywbcshhwemnnjix", receiver, "Help text sent")