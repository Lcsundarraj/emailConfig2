import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(email_info):
    from_addr=email_info['sender']
    to_addr=[email_info['receiver'],email_info['cc'], email_info['bcc']]
    msg=MIMEMultipart()
    msg['From']=from_addr
    msg['To']=" ,".join(to_addr)
    msg['subject']=email_info['sub']
    
    body=email_info['Message']

    msg.attach(MIMEText(body,'plain'))

    email=' '
    password='Sundar1989'

    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(from_addr,password)
    text=msg.as_string()
    mail.sendmail(from_addr,to_addr,text)
    # mail.quit()
    