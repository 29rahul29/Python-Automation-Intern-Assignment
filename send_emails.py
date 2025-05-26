import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_emails():
    df = pd.read_csv('custom_messages.csv')
    sender_email = 'burneremail0001000@gmail.com'
    sender_password = 'jqoq crao xfgr zvgf'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    for index, row in df.iterrows():
        recipient = row['email']
        message_text = row['message']
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = 'Thanks for Attending!' if 'thanks for joining' in message_text.lower() else 'We Missed You!'
        msg.attach(MIMEText(message_text, 'plain'))

        try:
            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Email sent to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}: {e}")

    server.quit()

if __name__ == '__main__':
    send_emails()
