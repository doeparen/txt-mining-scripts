from selenium import webdriver
from bs4 import BeautifulSoup
import re

# URL to webpage
url = "http://uu.diva-portal.org/smash/record.jsf?pid=diva2%3A1829272&dswid=543"

# Create a webdriver
driver = webdriver.Chrome()

# Open the URL and scrape its content
driver.get(url)
content = driver.page_source

# Close the webdriver
driver.quit()

# Create a BeautifulSoup object and extract all text from the URL
soup = BeautifulSoup(content, 'html.parser')
text = soup.get_text()

# Create a file name and save the text in a txt file
filename = re.sub(r'\W+', '_', url) + ".txt"
with open(filename, 'w', encoding='utf-8') as file:
    file.write(text)

print(f"The text data from the give URL is save in the file called: {filename}")
