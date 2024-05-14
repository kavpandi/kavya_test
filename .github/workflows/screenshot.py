import time
import pyautogui

# Delay before taking the screenshot to give time for Excel to open (adjust as needed)
time.sleep(5)

# Capture screenshot of the entire screen
screenshot = pyautogui.screenshot()

# Save the screenshot
screenshot.save('excel_screenshot.png')

print("Screenshot captured and saved as 'excel_screenshot.png'")
