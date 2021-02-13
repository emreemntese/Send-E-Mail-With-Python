import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # for text - html- hyperlink message
import sys

#more informations for  send image or other file operations 
#More information:  https://docs.python.org/3/library/email.html#module-email
# Examples: https://docs.python.org/3/library/email.examples.html
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

    # The html content you want 
    body = f'<a href="www.instagram.com/emre_mentese"> MyProfile </a>'

    #Don't forget "html" string !
    body_text = MIMEText(body, "html")
    mail.attach(body_text)
    mailserver.sendmail(mail["sender"], mail["receiver"], mail.as_string())
    print("Mail has been successfully sent. ")
    mailserver.close()

except Exception as error:
    print(error)

#----------------------------------------------------------------------------------------------