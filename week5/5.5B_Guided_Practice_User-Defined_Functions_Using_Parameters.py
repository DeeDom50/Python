# Student ID: devdom5222
# Date: 2023-07-21

def leapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return 1
        else:
            return 0
    else:
        if year % 4 == 0:
            return 1
        else:
            return 0

# Main program
print("Enter a year.")
year = int(input())
answer = leapYear(year)
if answer == 1:
    print("The year you chose is a leap year.")
else:
    print("The year you chose is not a leap year.")
