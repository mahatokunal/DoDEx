from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Setup webdriver
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# Define the URL of the webpage
url = "https://www.defense.gov/News/Contracts/?Page=1"

# Navigate to the webpage
driver.get(url)

# Find all elements with tag name 'a'
elements = driver.find_elements(By.TAG_NAME, 'a')

# Filter out any elements that don't have text starting with 'Contracts For'
contracts_for_elements = [element for element in elements if element.text.startswith('Contracts For')]

# Extract the href attribute from each element
contracts_for_links = [element.get_attribute('href') for element in contracts_for_elements]

# Print the hyperlinks
for link in contracts_for_links:
    print(link)

# Close the browser
driver.quit()