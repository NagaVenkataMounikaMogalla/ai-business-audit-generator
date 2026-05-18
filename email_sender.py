import smtplib
from email.message import EmailMessage


def send_email(receiver_email, company_name, pdf_path):

    sender_email = "mounimogalla@gmail.com"

    app_password = "YOUR_GMAIL_APP_PASSWORD"

    try:

        msg = EmailMessage()

        msg["Subject"] = f"{company_name} AI Business Audit Report"

        msg["From"] = sender_email

        msg["To"] = receiver_email

        msg.set_content(
            f"""
Hello,

Please find attached your AI Business Audit Report for {company_name}.
"""
        )

        with open(pdf_path, "rb") as f:

            file_data = f.read()

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="pdf",
            filename=f"{company_name}_report.pdf"
        )

        server = smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465,
            timeout=10
        )

        server.login(
            sender_email,
            app_password
        )

        server.send_message(msg)

        server.quit()

        print("EMAIL SENT SUCCESSFULLY")

        return True

    except Exception as e:

        print("EMAIL ERROR:")
        print(str(e))

        return False