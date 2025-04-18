import datetime

def calculate_days_between(date1, date2):
    date_format = "%Y-%m-%d"
    d1 = datetime.datetime.strptime(date1, date_format) 
    d2 = datetime.datetime.strptime(date2, date_format)
    difference = d2 - d1 
    return difference.days 

date1 = input()
date2 = input()
print(calculate_days_between(date1, date2))
