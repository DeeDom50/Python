import requests
from bs4 import BeautifulSoup

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

def main():
    print("devdom5222") 
    page_number = int(input("Enter the page number (1-10): "))
    url = f"https://quotes.toscrape.com/page/{page_number}/"
    html_content = readwebpage(url)
    quotes = parsehtml(html_content)
    outputquotes(quotes)

if __name__ == "__main__":
    main()
