import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

hmtl = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "xxx"  # Add sender name
email["to"] = "email"  # Add here the email address you want to send TO
email["subject"] = "This is a test"

email.set_content(hmtl.substitute({"name": "TinTin"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Add bellow the email address where you send FROM and password.
    smtp.login("email", "password")
    smtp.send_message(email)
    print("Jobs Done!")
