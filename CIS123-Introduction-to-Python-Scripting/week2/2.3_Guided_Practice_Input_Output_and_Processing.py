import datetime

print("devdom5222");
birthdate = input("What us your birthdate (MM/DD/YYYY)?");

month, day, year = birthdate.split("/");
bdate = datetime.datetime(int(year), int(month), int(day));
todays_date = datetime.datetime.now();
age = todays_date - bdate;

print("You are " + str(age.days/365.25) + " years old");

