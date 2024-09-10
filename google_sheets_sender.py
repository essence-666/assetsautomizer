import gspread
from google.oauth2.service_account import Credentials

def fill_cell (val : float, cel : str) -> None:
    # Path to your service account key file
    service_account_file = "./cred.json"

    # Define the scope
    scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Authenticate and create a client
    creds = Credentials.from_service_account_file(service_account_file, scopes=scopes)
    client = gspread.authorize(creds)

    # Open the Google Sheet by its name or URL
    sheet = client.open("myassets").sheet1  # Use sheet1, or the sheet index you want to modify

    # Update a specific cell
    cell = cel  # Specify the cell (like 'A1')
    value = val  # The value to be inserted
    sheet.update(cell, [[value]])

    print(f"Updated cell {cell} with value: {value}")
