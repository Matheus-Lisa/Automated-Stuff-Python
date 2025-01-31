import os

def log_invoice(client, status):
    """
    Logs invoice sending details.

    Args:
        client (dict): Client details (name, email).
        status (str): Status message (Success/Failure).
    """
    log_file = "logs/email_log.txt"
    if not os.path.exists("logs"):
        os.makedirs("logs")

    with open(log_file, "a") as f:
        f.write(f"{client['Name']}, {client['Email']}, {status}\n")

    print(f"Logged: {client['Name']} - {status}")

# Test
if __name__ == "__main__":
    test_client = {"Name": "John Doe", "Email": "johndoe@example.com"}
    log_invoice(test_client, "Success")
