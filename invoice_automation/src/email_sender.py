import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import json

def load_email_config():
    config_file = 'config/settings.json'
    
    if not os.path.exists(config_file):
        print(f"Error: Configuration file '{config_file}' not found.")
        return None

    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
            return config
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def send_email(client, invoice_path):
    # Load email configuration
    config = load_email_config()

    if config is None:
        print("Error: Email configuration not loaded.")
        return False
    
    # Now you can use `config` to access SMTP settings, like:
    smtp_server = config.get("smtp_server")
    port = config.get("port")
    sender_email = config.get("sender_email")
    sender_password = config.get("sender_password")
    receiver_email = client.get("Email")  # Using client data

    # Your code to send the email with the invoice attached
    # For example, using smtplib to connect and send an email
    # Make sure to handle any email sending logic here (not shown)
    
    print(f"Sending email to {receiver_email} via {smtp_server}...")
    
    # If email sent successfully
    return True

# Test the function
if __name__ == "__main__":
    test_client = {
        "Name": "John Doe",
        "Email": "johndoe@example.com",
    }
    send_email(test_client, "invoices/Invoice_JohnDoe.pdf")
