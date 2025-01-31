import pandas as pd

def load_client_data(csv_file):
    """
    Reads client data from a CSV file and returns a list of dictionaries.
    
    Args:
        csv_file (str): Path to the CSV file.

    Returns:
        list: A list of dictionaries containing client details.
    """
    try:
        df = pd.read_csv(csv_file)
        clients = df.to_dict(orient="records")  # Convert to a list of dictionaries
        return clients
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

# Test the function
if __name__ == "__main__":
    clients = load_client_data("../data/clients.csv")
    print(clients)
