import requests
import csv
import time
from bs4 import BeautifulSoup4

# using the old reddit format and url since its easier to extract data
url = "https://old.reddit.com/r/WasabiWallet/"
# this mimics a browser visit
headers = {'User-Agent': 'Mozilla/5.0'}

# gives us a requests.models.Response object - raw HTML for page
page = requests.get(url, headers=headers)

#beautifulsoup object 
soup = BeautifulSoup(page.text, 'html.parser')
