from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import smtplib
import sys
import os
import imghdr

#Set up working directory
print(os.path.dirname(os.path.realpath('__file__')))

#Set up the SMTP server info
#TODO add response for username password and store info locally
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = "587"
SMTP_USERNAME = "geocircle.services@gmail.com"
SMTP_PASSWORD = "geocircle123"


#Fill out To/From/Subject fields
with open("receiver_list.txt", "r") as recipient:
    EMAIL_TO = [line.rstrip('\n') for line in recipient]
EMAIL_FROM = "geocircle.services@gmail.com"
EMAIL_SUBJECT = "Hello & Greetings"

#attachment
files = ["GeoCircle.jpg","python-logo.png"]


#TODO remember what the hell this line does
EMAIL_SPACE = "; "


#Send email function using smtplib
def send_email(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    msg.attach(MIMEText("Selamat datang di Geocircle"))
    
    image = MIMEImage(img_data, name=os.path.basename("GeoCircle.jpg"))
    msg.attach(image)
    
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

#main
if __name__=='__main__':
    send_email("GeoCircle.jpg")
    
#Source : https://docs.python.org/3.8/library/email.mime.html ; https://stackoverflow.com/questions/918154/relative-paths-in-python ; https://stackoverflow.com/questions/13070038/attachment-image-to-send-by-mail-using-python ; https://www.code-learner.com/python-send-html-image-and-attachment-email-example/
