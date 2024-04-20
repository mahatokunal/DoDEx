import requests
from bs4 import BeautifulSoup

def get_content_by_class(url, element_class):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    element = soup.find(class_=element_class)
    return element.text if element else None

# Test the function
print(get_content_by_class('https://www.defense.gov/News/Contracts/Contract/Article/3741857/', 'content content-wrap'))