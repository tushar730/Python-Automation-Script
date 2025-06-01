import smtplib
import os
import argparse
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_email(subject, body, to_email, html=False, attachments=None, cc=None, bcc=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = os.getenv("EMAIL_USER")
    msg['To'] = to_email
    if cc:
        msg['Cc'] = cc
    if bcc:
        msg['Bcc'] = bcc

    # Adding the email body (HTML or plain text)
    if html:
        msg.add_alternative(body, subtype='html')
    else:
        msg.set_content(body)

    # Adding attachments (if any)
    if attachments:
        for file_path in attachments:
            try:
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(file_path)
                    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
            except Exception as e:
                print(f"⚠️ Failed to attach {file_path}: {e}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            smtp.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def main():
    parser = argparse.ArgumentParser(description="Send an email using Gmail's SMTP server.")
    parser.add_argument("to", help="Recipient's email address")
    parser.add_argument("subj_
