import datetime
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

def GoodbyeWorld():
    print("Goodbye World")

def CheckRange():
    number = int(input("Enter a number: "))
    if number >= 100:
        print(f"You entered the number {number}, and your entry is 100 or greater.")
    else:
        print(f"You entered the number {number}, and your entry is less than 100.")

def DaysTillGrad():
    grad_date_str = input("Enter your graduation date (YYYY-MM-DD): ")
    grad_date = datetime.datetime.strptime(grad_date_str, "%Y-%m-%d")
    current_date = datetime.datetime.now()
    days_until_grad = (grad_date - current_date).days
    print(f"It is currently {current_date}.")
    print(f"There are {days_until_grad} days until your graduation.")

def ReadWeb():
    url = "https://quotes.toscrape.com/page/3/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        quotes.append((text, author))
    for quote, author in quotes:
        print(f'"{quote}" - {author}')

def ReadPDF():
    pdf_file_path = "SimplePDF.pdf"
    with open(pdf_file_path, "rb") as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            print(page.extract_text())
