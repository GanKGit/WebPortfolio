import smtplib as smtp
import ssl
def send_mail(username, password, receiver, msg_content):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    print("Created context")
    with smtp.SMTP_SSL(host, port, context) as server:
        ret=server.login(username,password)
        print(ret)
        mail=server.sendmail(username, receiver,msg_content)
        print(f"Mail status = {mail}")

