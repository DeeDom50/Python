import requests
from bs4 import BeautifulSoup

print("devdom5222")

def readwebpage(url):
    response = requests.get(url)
    return response.text

def parsehtml(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        quotes.append((text, author))
    return quotes

def outputquotes(quotes):
    for quote, author in quotes:
        print(f'"{quote}" - {author}')

if __name__ == "__main__":
    url = "https://quotes.toscrape.com/page/2/"
    html_content = readwebpage(url)
    quotes = parsehtml(html_content)
    outputquotes(quotes)
