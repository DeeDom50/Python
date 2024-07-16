import PAfunctions
import requests
from bs4 import BeautifulSoup

# Print student ID
print("devdom522225")

# Call the functions from PAfunctions.py
PAfunctions.GoodbyeWorld()
PAfunctions.CheckRange()
PAfunctions.DaysTillGrad()

# Function to read the webpage
def readwebpage():
    url = "https://quotes.toscrape.com/page/2/"
    response = requests.get(url)
    return response.text

# Function to parse data from the webpage
def parsedata(html):
    soup = BeautifulSoup(html, 'html.parser')
    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        quotes.append((text, author))
    return quotes

# Function to output the quotes and authors
def outputdata(quotes):
    for quote, author in quotes:
        print(f'"{quote}" - {author}')

# Call the readwebpage function
html = readwebpage()

# Call the parsedata function
quotes = parsedata(html)

# Call the outputdata function
outputdata(quotes)
