from src.data_loader import load_client_data
from src.invoice_generator import create_invoice
from src.email_sender import send_email
from src.logger import log_invoice

clients = load_client_data("data/clients.csv")

for client in clients:
    print("Client data:", client)
    invoice_path = create_invoice(client)
    email_status = send_email(client, invoice_path)
    log_invoice(client, "Success" if email_status else "Failed")
    
print("All invoices processed!")