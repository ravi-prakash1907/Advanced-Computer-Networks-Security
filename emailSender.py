##########  Script to send E-Mails automatically  ##########

## for using smtp protocol for mail
import smtplib

## for email
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#########
senderMail = input("Enter the sender's e-mail address: ") # 'myMail@mail.com'

#########

server = smtplib.SMTP_SSL('smtp.gmail.com')
# server = smtplib.SMTP('smtp.example.com',25) ## (server service provider, port)

server.ehlo()

## login to own account from where the mail will be sent
with open('src/password.txt', 'r') as f:
    password = f.read()

server.login(senderMail,password)

#################################

## required I/P
receiverMail = input("Enter the receiver's e-mail address: ")


## created as msg
msg = MIMEMultipart()
msg['From'] = senderMail #'myMail@mail.com'
msg['To'] = receiverMail #'reciever@mail.com'
msg['Subject'] = 'A temp mail lol'

with open('src/message.txt', 'r') as f:
    message = f.read()

## attach method can be used to attatch things
msg.attach(MIMEText(message, 'plane'))

## attaching an image
picLoc = 'src/abstractArt.ppm'
## it'll be read in byte string
attatchment = open(picLoc,'rb')

## creating the payload with "octet-stream" to process the text data
payload = MIMEBase('application','octet-stream')
## it'll read the content of image
payload.set_payload(attatchment.read())

encoders.encode_base64(payload)
payload.add_header('Content-Disposition',f'attatchment; filename={filename}')

## finalizing the whole e-mail
msg.attach(payload)

## converting the whole msg in python string
text = msg.as_string()

###################

## sending the mail
server.sendmail(senderMail, receiverMail, text)