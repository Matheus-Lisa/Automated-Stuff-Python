from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_invoice(client, output_dir="invoices"):
    """
    Generates a PDF invoice for a given client.

    Args:
        client (dict): A dictionary containing client details.
        output_dir (str): Directory where invoices will be saved.

    Returns:
        str: Path to the generated invoice.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create invoices folder if it doesn't exist

    invoice_number = f"Invoice_{client['Name'].replace(' ', '')}.pdf"
    file_path = os.path.join(output_dir, invoice_number)

    c = canvas.Canvas(file_path, pagesize=letter)
    
    # Invoice Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Company Name")
    c.setFont("Helvetica", 12)
    c.drawString(200, 730, "123 Business St, City, Country")
    c.drawString(200, 710, "Email: contact@company.com")

    # Client Info
    c.drawString(100, 670, f"Client: {client['Name']}")
    c.drawString(100, 650, f"Email: {client['Email']}")

    # Invoice Items
    y_position = 620
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y_position, "Items Purchased:")
    y_position -= 20

    for item in client['InvoiceItems'].split(','):
        c.setFont("Helvetica", 12)
        c.drawString(120, y_position, f"- {item.strip()}")
        y_position -= 20

    # Total Amount
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y_position - 20, f"Total Amount Due: ${client['Amount']}")

    # Save PDF
    c.save()
    return file_path

# Test the function
if __name__ == "__main__":
    sample_client = {
        "Name": "John Doe",
        "Email": "johndoe@example.com",
        "InvoiceItems": "Product A, Product B",
        "Amount": "150.00"
    }
    pdf_path = create_invoice(sample_client)
    print(f"Invoice saved at: {pdf_path}")
