"""
Simple Selenium script to open the demo site in Chrome.

- Keeps the browser open after the script exits using the Chrome 'detach' option.
- Requires a matching ChromeDriver available via PATH or configured externally.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome to remain open after the Python process ends.
options = Options()
options.add_experimental_option("detach", True)

# Start Chrome WebDriver with the configured options.
driver = webdriver.Chrome(options=options)

# Navigate to the demo site.
driver.get("https://demo.itlearn360.com/")
