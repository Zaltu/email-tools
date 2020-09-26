import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

SMTP = smtplib.SMTP()
SMTP.connect('localhost')


def simple_email(sender, recipient, subject, message):
    """
    Send a simple email. Easy to set up. For more advanced options use `send_email`.

    :param str sender: email address for sender
    :param str|list recipient: recipient email or list of recipient emails
    :param str subject: email subject
    :param str message: text message to send as email body
    """
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    SMTP.send_message(msg)
