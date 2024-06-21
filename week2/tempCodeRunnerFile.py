import datetime

print("devdom5222");
birthdate = input("What us your birthdate (MM/DD/YYYY)?");

month, day, year = birthdate.split("/");
bdate = datetime.datetime(int(year), int(month), int(day));
print(bdate);
