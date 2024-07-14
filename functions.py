def HelloWorld():
    print("Hello World, my namie is Devante")
    print("I am a student at ECPI University")
    print("I have nevr programmed a computer before")
    print("This is great")

def CheckEven():
    number = input("Enter a number: ")
    number = int(number)

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

def Birthday():
    import datetime

    birthdate = input("What is your birthday (MM/DD/YYYY): ")
    
    month, day, year = birthdate.split("/")
    bdate = datetime.datetime(int(year), int(month), int(day))
    todays_date = datetime.datetime.now()
    age = todays_date - bdate

    print("you are " + str(age.days/365.25) + " years old")

def NumberSort(numbers):
    sorted_numbers = sorted(numbers)
    print("Sorted numbers:", sorted_numbers)

def ReadNames(file_path):
    with open(file_path, 'r') as file:
        names = file.readlines()
        for name in names:
            print(name.strip())

def ReadWebPage(url):
    import requests
    response = requests.get(url)
    print(response.text)

def PullPDF(url):
    import requests
    response = requests.get(url)
    with open('downloaded.pdf', 'wb') as file:
        file.write(response.content)
    print("PDF downloaded successfully.")
