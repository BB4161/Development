import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element containing the stock price
stock_price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text

# Print the stock price
print(f"Apple stock price: {stock_price}")