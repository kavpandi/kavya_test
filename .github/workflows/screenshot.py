from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Google Sheets API credentials (replace with your own)
credentials = Credentials.from_authorized_user_file('credentials.json')
service = build('sheets', 'v4', credentials=credentials)

# Google Sheet ID and range
sheet_id = '1Z2mAgivd2qRQzkOBXS1dSveaazI_MgHlHbjOyTfpNww'
range_name = 'shopify_data!A1:K4'  # Example range, adjust as needed

# Export the Google Sheet as an image
request = service.spreadsheets().values().get(spreadsheetId=sheet_id, range=range_name)
response = request.execute()
print(response)  # Print the response to see the data

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(options=chrome_options)

# Load the exported image URL
image_url = 'https://example.com/exported_sheet_image.png'  # Replace with the actual exported image URL
driver.get(image_url)

# Take a screenshot
driver.save_screenshot('performance_data.png')

# Close the WebDriver
driver.quit()
