import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # for text - html- hyperlink message
from email.mime.image import MIMEImage # for image 
import sys

#----------------------------------------------------------------------------------------------
''' Connect Gmail Email Server '''
try:
    #connect
    mailserver = smtplib.SMTP("smtp.gmail.com",587)
    mailserver.ehlo()
    mailserver.starttls()
    #e-mail & Password login
    mailserver.login("example@gmail.com","password")
    mail = MIMEMultipart()
    
    # Mail - Sender, Receiver, Subject
    mail["sender"] = "example@gmail.com"       #sender
    mail["receiver"] = "toexample@gmail.com"   #receiver
    mail["Subject"] = "Example"                  #Subject

except Exception as error:
    print(error)

#----------------------------------------------------------------------------------------------
''' Send a Message '''
try:

    body = """
    Hello World !
    """

    body_text = MIMEText(body, "plain")
    mail.attach(body_text)

    mailserver.sendmail(mail["sender"], mail["receiver"], mail.as_string())
    print("Mail has been successfully sent. ")
    mailserver.close()

except Exception as error:
    print(error)
#----------------------------------------------------------------------------------------------
''' Sen a HTML and Hyperlink '''
try:

    body = """
    Hello World !
    """

    body_text = MIMEText(body, "html")
    mail.attach(body_text)

    mailserver.sendmail(mail["sender"], mail["receiver"], mail.as_string())
    print("Mail has been successfully sent. ")
    mailserver.close()

except Exception as error:
    print(error)

#----------------------------------------------------------------------------------------------
''' Send an Image '''
try:
    pass

except Exception as error:
    print(error)

