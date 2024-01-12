import smtplib as smtp
import ssl


def send_mail(username, password, receiver,msg_content):
    host = "smtp.gmail.com"
    port = 465
    username = "lgk09021984@gmail.com"
    passwd = "kywbcshhwemnnjix"
    context = ssl.create_default_context()
       with smtp.SMTP_SSL(host, port, context) as server
        server.sendmail(username, receiver,msg_content)


