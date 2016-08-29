import smtplib
import sys
from email.mime.text import MIMEText
from datetime import datetime

def sendEmail(message, emailaddress):
    msg = MIMEText( 'ALERT AT ' + str(datetime.now()))
    me = emailaddress
    you = emailaddress
    msg['Subject'] = message
    msg['From'] = me
    msg['To'] = you
    s = smtplib.SMTP('localhost')
    s.sendmail(me, [me], msg.as_string())
    s.quit()