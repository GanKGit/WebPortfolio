import streamlit as st
import sendEmail

receiver = st.text_input("Enter your email :")
st.button("Press to receive help information")
sendEmail.send_mail("lgk09021984@gmail.com","kywbcshhwemnnjix", receiver, "Help text sent")