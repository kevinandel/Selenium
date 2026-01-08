# python
"""Test the Google search input and submission for a sample query.

Steps:
- Open https://www.google.com/
- Locate the search input box on the Google homepage
- Enter the query "Best practices in software testing"
- Submit the search (press Enter or click the search button)

This module configures Chrome to remain open after the Python process ends
so the browser window stays visible for inspection.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configure Chrome to remain open after the Python process ends.
options = Options()
options.add_experimental_option("detach", True)

# Start Chrome WebDriver with the configured options.
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")

driver.find_element(By.ID, "APjFqb").send_keys("Best practices in software testing")
# driver.find_element(By.NAME,"btnK").click()
driver.find_element(By.CLASS_NAME,"gNO89b").submit()