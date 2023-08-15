import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

msg = MIMEMultipart()
msg["Subject"] = "An Email Alert"
msg["From"] = "imangali.nurkamalov@nu.edu.kz"
msg["To"] = "anything@gmail.com"
body_part = MIMEText("Список ИИН/БИН", 'plain')
msg.attach(body_part)

filename = "for_storing.csv"

context = ssl.create_default_context()

with open("for_storing.csv",'rb') as file:
    msg.attach(MIMEApplication(file.read(), Name= "for_storing.csv"))

with smtplib.SMTP("smtp.gmail.com", port = 587) as smtp:
    smtp.starttls(context=context)
    smtp.login("imangali.nurkamalov@nu.edu.kz", "")
    smtp.sendmail("imangali.nurkamalov@nu.edu.kz", ["anything@gmail.com", "usedforproject15@gmail.com"], msg.as_string())