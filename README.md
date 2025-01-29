# Automated Invoice Generator & Email Sender

Project Overview
This project will automatically generate invoices in PDF format using client data from a CSV or database and send them via email to respective clients. It will also store a record of sent invoices.

Key Features
Read Client Data from a CSV or database (Name, Email, Invoice Items, Amount).
Generate Invoices dynamically in PDF format using reportlab or pdfkit.
Send Emails with invoices attached via smtplib and email.message.
Log Sent Invoices in a local database (SQLite or a simple log file).
Error Handling & Retry Mechanism in case of failed email delivery.
Tools & Libraries Required
pandas (for reading CSV data)
reportlab or pdfkit (for PDF generation)
smtplib and email.mime (for email sending)
sqlite3 (for storing records)
schedule (to run the script automatically at a set time)
Steps to Build
Extract Data: Read the client details from a CSV file.
Generate Invoice: Create a formatted invoice in PDF.
Send Email: Attach and send the invoice via SMTP.
Log Transactions: Store details of sent invoices in a database.
Schedule Automation: Run the script daily/weekly using schedule or cron.
