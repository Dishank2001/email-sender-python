from cgitb import html
from email import message
import pandas as p
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

data=p.read_excel("path of a file")
email_col=data.get("EMAIL")
list_of_email=list(email_col)
print(list_of_email)

try:
    server=sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("xyz1234@gmail.com","dfkeslc")#password
    from_ ="xyz1234@gmail.com"
    to_=list_of_email
    message=MIMEMultipart("alternative")
    message['Subject']="your subject"
    message["from"]="xyz1234.com"

    html='''
    <html>
    <head>

    </head>
    <body>
    write html

    <h1> content  </h1>
    <button> sumbit </button>
    </body>

    </html>
    '''

    part2=MIMEText(html,"html")
    message.attach(part2)
    server.sendmail(from_,to_,message.as_string())
    print("message has been sent")
except Exception as e:
    print(e)    