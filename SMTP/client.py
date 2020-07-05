import smtplib
import ssl
import email.utils
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.text import MIMEText

arg=sys.argv

#sending mails using gmail server
if len(arg)==6 :
    port = 465  # For SSL
    password = arg[2]

    # Create a secure SSL context
    context = ssl.create_default_context()
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = arg[1]
    message['To'] = arg[3]
    message['Subject'] = arg[4]
    #The body and the attachments for the mail
    message.attach(MIMEText(arg[5], 'plain'))
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(arg[1], password)
        server.sendmail(arg[1], arg[3], message.as_string())



#for sending mails at custom server
# Create the message
msg = MIMEText(arg[4])
msg['To'] = email.utils.formataddr(('Recipient', arg[2]))
msg['From'] = email.utils.formataddr(('Author', arg[1]))
msg['Subject'] = arg[3]

server = smtplib.SMTP('127.0.0.1', 1025)
server.set_debuglevel(True) # show communication with the server
try:
    server.sendmail(arg[1], [arg[2]], msg.as_string())
finally:
    server.quit()