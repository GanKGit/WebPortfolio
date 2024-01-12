import streamlit as st
import sendEmail as se
receiver_email = st.text_input("Enter your email :")
button=st.button("Press to receive help information", key="Submit")

print("Waiting for submit")

if button and len(receiver)!=0:
    print("Calling Send mail")
    se.send_mail("lgk09021984@gmail.com","kywbcshhwemnnjix", receiver_email, "Help text sent")
    st.write("Help emailed to the requested email id")