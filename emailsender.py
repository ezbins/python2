#!/usr/bin/env python3

import smtplib
import getpass
from email.mime.text import MIMEText
from email.header import Header
import datetime

host = "mail.caretek.com.tw"
port = 587
username = "dennis.peng@caretek.com.tw"
#passwd = getpass.getpass()
passwd = "99999ibm"
from_email = username
to_email = ['ty3627@gmail.com']

message = MIMEText('Python郵件測試')
message['From'] = Header("dennis.peng@caretek.com.tw")
for one_mail in to_email:
    message['To'] =  Header(one_mail)

message['Subject'] = Header("Python郵件測試")
#current = datetime.datetime.now()
message['Date'] = Header("Wed, 21 Dec 2016 16:01:15 +0800")
email_conn = smtplib.SMTP(host, port)
print(email_conn.ehlo())
print(email_conn.starttls())
email_conn.login(username, passwd)
email_conn.sendmail(from_email,to_email,message.as_string())
email_conn.quit()