from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def capture_google_sheet_screenshot(url, output_file):
    # Set up Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Load the Google Sheet URL
    driver.get(url)

    # Take a screenshot
    driver.save_screenshot(output_file)

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    google_sheet_url = 'https://docs.google.com/spreadsheets/d/1Z2mAgivd2qRQzkOBXS1dSveaazI_MgHlHbjOyTfpNww/edit'  # Replace with the URL of your Google Sheet
    screenshot_file = 'performance_data.png'  # Output screenshot file

    capture_google_sheet_screenshot(google_sheet_url, screenshot_file)
