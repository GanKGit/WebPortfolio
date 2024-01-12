import streamlit as st
import sendEmail as se
receiver_email = st.text_input("Enter your email :")
button=st.button("Press to receive help information", key="Submit")

sender_email ="lgk09021984@gmail.com"
password="kywbcshhwemnnjix"

Help_Text = f"""\
Subject: Help Information!
From: {sender_email}
Help text line1
Help text line2
Help text line3
"""
txt_update=st.text("")
if button and len(receiver_email)!=0:
    txt_update.text("Sending the email...")
    se.send_mail(sender_email,password, receiver_email, Help_Text)
    txt_update.text("Help emailed to the requested email id")