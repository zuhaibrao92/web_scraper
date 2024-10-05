import requests
from bs4 import BeautifulSoup
import pandas as pd


# Specify the URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/IBM'


# Send an HTTP GET request to the webpage
respons = requests.get(url)

# Store the HTML content in a variable
html_content = respons.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')


# Display a snippet of the HTML content
print(html_content[:500])
links = soup.find_all('a')
for the_link in links:
    print(the_link.text)
df= pd.DataFrame(the_link)
print(df)