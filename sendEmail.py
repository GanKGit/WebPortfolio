import smtplib as smtp
import ssl
def send_mail(sender_email, password, receiver_email, msg_content):
    host = "smtp.gmail.com"
    port = 587 #465
    context = ssl.create_default_context()
    print("Created context")

    try:
        server = smtp.SMTP(host , port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        mail = server.sendmail(sender_email, receiver_email, msg_content)
    except Exception as e:
        # Print any error messages to stdout
        print("Exception caught")
        print(e)
    finally:
        server.quit()

