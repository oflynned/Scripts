import datetime
import os
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_time_between_dates():
    today = datetime.datetime.now()
    letter_date = datetime.date(2018, 2, 9)
    today_date = datetime.date(today.year, today.month, today.day)

    return (today_date - letter_date).days


def generate_email_body():
    days_since = get_time_between_dates()
    return "Hi {0},\n\n" \
           "I notice my owed salary still hasn't been lodged into my bank account.\n\n" \
           "I'd like to remind you that it's been {1} days since your letter of owed salary.\n\n" \
           "{2}".format("Recipient", "Sender", days_since)


def send_email():
    recipient = "oflynned@tcd.ie"
    sender = "<email>@gmail.com"
    password = "<password>"

    message = MIMEMultipart('alternative')
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = "<Subject>"

    plain_text_content = MIMEText(generate_email_body(), 'plain')
    message.attach(plain_text_content)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, recipient, message.as_string())
    server.close()


def main():
    send_email()


if __name__ == '__main__':
    main()
