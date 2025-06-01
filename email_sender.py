import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

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

    if html:
        msg.add_alternative(body, subtype='html')
    else:
        msg.set_content(body)

    # Add attachments
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

# Example usage
if __name__ == "__main__":
    send_email(
        subject="🚀 Python Automation Email",
        body="<h2>Hello from Python!</h2><p>This is an automated email.</p>",
        to_email="recipient@example.com",
        html=True,
        attachments=["assets/sample_output/news.csv"],
        cc="someone@example.com",
        bcc="hidden@example.com"
    )
