import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extracted_data(url, element_class):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    element = soup.find(class_=element_class)
    return element.text if element else None

# Setup webdriver with headless option
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Setup webdriver
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

for i in range(1, 5):
    # Define the URL of the webpage
    url = f"https://www.defense.gov/News/Contracts/?Page={i}"

    # Navigate to the webpage
    driver.get(url)

    # Find all elements with tag name 'a'
    elements = driver.find_elements(By.TAG_NAME, 'a')

    # Filter out any elements that don't have text starting with 'Contracts For'
    contracts_for_elements = [element for element in elements if element.text.startswith('Contracts For')]

    # # Print the text of each element
    # for element in contracts_for_elements:
    #     print(element.text)

    # Extract the href attribute from each element
    contracts_for_links = [element.get_attribute('href') for element in contracts_for_elements]

    # # Print the hyperlinks
    # for link in contracts_for_links:
    #     print(extracted_data(link, 'content content-wrap'))

    data = {}
    for element in contracts_for_elements:
        date = element.text.split('Contracts For ')[1].split('\n')[0]  # Extract the date from the text
        link = element.get_attribute('href')
        extracted = extracted_data(link, 'content content-wrap')
        if extracted:
            data[date] = extracted

    # Write the data to a JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f)

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(list(data.items()), columns=['article_date', 'data_on_articleDatePage'])

    # Write the DataFrame to a .csv file
    df.to_csv('data.csv', index=False)

    # Write the DataFrame to a .xlsx file
    df.to_excel('data.xlsx', index=False)

# Close the browser
driver.quit()