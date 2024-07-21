# Excel.py
from openpyxl import Workbook
import datetime

book = Workbook()
sheet = book.active
sheet['A1'] = 'devdom5222'
sheet['A2'] = 12
sheet['A3'] = 34
sheet['A4'] = '=A2+A3'
now = datetime.datetime.now()
sheet['A5'] = now
book.save("/Users/devante/Library/CloudStorage/OneDrive-ECPIUniversity/Desktop/dDominicci_cis_123/FirstExcel.xlsx")
