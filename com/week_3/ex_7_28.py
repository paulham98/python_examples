# sendMail.py
import smtplib
from email.mime.text import MIMEText
from email.header import Header

FROM = 'user_python@naver.com'
TO = 'user_python@naver.com'

#text = 'Hello, good morning!'.encode('ascii')
#msg = MIMEText(text, _charset= 'us-ascii')

#msg['Subject'] = Header('Test')
#msg['From'] = FROM
#msg['To'] = TO

text = '안녕 좋은아침'
msg = MIMEText(text, _charset= 'utf8')
msg['subject'] = Header('테스트','utf8')
msg['From'] = FROM
msg['To'] = TO
print(msg.as_string())

server = smtplib.SMTP_SSL("smtp.naver.com")
server.login("user_python", "python1234")
server.sendmail(FROM, TO, msg.as_string())
server.quit()
