from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import pyperclip

# --- Configuration ---
# The text you want to find
SEARCH_TEXT = pyperclip.paste()
# The URL to navigate to (if you're opening a new page)
URL = "https://csmsmpscsc.mp.gov.in/rationmitra/EBS/RCMS/AddMember.aspx"

# --- Setup WebDriver ---
# Automatically download and manage the geckodriver executable
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Navigate to the page
    driver.get(URL)

    # Get all the visible text from the entire page body
    # Using By.XPATH, you can get the text content of the whole <html> element
    full_page_text = driver.find_element(By.TAG_NAME, "html").text

    # Use Python's string find() method to locate the text
    # find() returns the starting index if found, or -1 if not found
    text_position = full_page_text.find(SEARCH_TEXT)

    if text_position != -1:
        print(f"'{SEARCH_TEXT}' found in the page.")
        print(f"First occurrence starts at index: {text_position}")
    else:
        print(f"'{SEARCH_TEXT}' not found in the page.")

finally:
    # Always ensure the browser is closed after the script finishes
    driver.quit()
