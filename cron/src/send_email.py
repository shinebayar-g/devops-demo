import smtplib
from email.message import EmailMessage

import settings

def SendEmail():
    msg = EmailMessage()
    # TODO: Use more dynamic template
    msg['Subject'] = 'Database backup complete.'
    msg['From'] = settings.EMAIL_FROM
    msg['To'] = settings.EMAIL_TO
    msg.set_content(f'Successfully uploaded database to S3')
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html lang="en">
    <body>
        <h1 style="color:SlateGray;">Successfully uploaded database to S3</h1>
    </body>
    </html>
    """, subtype='html')

    try:
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(settings.SMTP_USER, settings.SMTP_PASS)
            smtp.send_message(msg)
        print(f"Sent success email to: {settings.EMAIL_TO}")
    except Exception as e:
        print("Error happened. See below:")
        print(e)

def SendErrorEmail():
    msg = EmailMessage()
    # TODO: Use more dynamic template
    msg['Subject'] = "Database backup error."
    msg['From'] = settings.EMAIL_FROM
    msg['To'] = settings.EMAIL_TO
    msg.set_content(f'There was an error when backing up database, please check script logs for more details.')
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html lang="en">
    <body>
        <h1 style="color:SlateGray;">There was an error when backing up database, please check script logs for more details.</h1>
    </body>
    </html>
    """, subtype='html')

    try:
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(settings.SMTP_USER, settings.SMTP_PASS)
            smtp.send_message(msg)
        print(f"Sent error email to: {settings.EMAIL_TO}")
    except Exception as e:
        print("Error happened. See below:")
        print(e)
