import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = '********@hotmail.fr'
PASSWORD = '*********'

def sendEmail(newOffer):
    host = "smtp.live.com"
    email = "*********@edhec.com"

    # set up the SMTP server
    s = smtplib.SMTP(host=host, port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = "There is a new offer: {}. You better have your resume ready! ".format(newOffer)

    # setup the parameters of the message
    msg['From'] = MY_ADDRESS
    msg['To'] = email
    msg['Subject'] = "VIE BOT, new offer."
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
