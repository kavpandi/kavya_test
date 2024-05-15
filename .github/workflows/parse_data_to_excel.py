import gspread
from oauth2client.service_account import ServiceAccountCredentials

def inject_data_to_google_sheet(sheet_id, sheet_name, columns_data):
    # Define the scope of access
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # Load credentials from JSON file
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    # Authorize using credentials
    gc = gspread.authorize(credentials)

    # Open the Google Sheets spreadsheet
    try:
        sh = gc.open_by_key(sheet_id)
    except gspread.exceptions.APIError as e:
        print(f"Failed to open spreadsheet with ID '{sheet_id}': {e}")
        return

    # Open the worksheet by name
    try:
        worksheet = sh.worksheet(sheet_name)
    except gspread.exceptions.WorksheetNotFound as e:
        print(f"Worksheet '{sheet_name}' not found in spreadsheet '{sheet_id}': {e}")
        return

    # Inject data into the corresponding columns
    for column, data_file in columns_data.items():
        # Read data from text file
        try:
            with open(data_file, 'r') as f:
                data = f.readlines()
        except FileNotFoundError as e:
            print(f"File '{data_file}' not found: {e}")
            continue

        # Write data to the corresponding column in the Google Sheets spreadsheet
        try:
            worksheet.update_column(column, data)
            print(f"Data injected into column {column} from file '{data_file}'.")
        except gspread.exceptions.APIError as e:
            print(f"Failed to update column {column}: {e}")

if __name__ == "__main__":
    sheet_id = '1Z2mAgivd2qRQzkOBXS1dSveaazI_MgHlHbjOyTfpNww'  # Replace with the ID of your Google Sheets spreadsheet
    sheet_name = 'shopify_data'  # Replace with the name of the worksheet in your spreadsheet
    columns_data = {
        1: 'date.txt',  # Column 1: Text file containing values
        2: 'sessions.txt',  # Column 2: Text file containing values
        4: 'revenue.txt',  # Column 4: Text file containing values
        6: 'orders.txt',  # Column 6: Text file containing values
        8: 'conv_rate.txt',  # Column 8: Text file containing values
        10: 'aov.txt',  # Column 10: Text file containing values
        # Add more entries for additional columns and respective text files
    }

    inject_data_to_google_sheet(sheet_id, sheet_name, columns_data)
