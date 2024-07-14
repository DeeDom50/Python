import requests
from bs4 import BeautifulSoup

print("devdom522")  


def readwebpage(url):
    output = requests.get(url)
    return output.text

def parsehtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def outputquotes(parsed):
    quotes = parsed.find_all('span', class_='text')
    for quote in quotes:
        print(quote.text)

url = "http://quotes.toscrape.com"
html = readwebpage(url)
parsed = parsehtml(html)
outputquotes(parsed)



