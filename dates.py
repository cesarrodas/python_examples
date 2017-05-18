import re

listOfDates = ['Oct 7, 2009', 'Nov 10, 2009', 'Oct 22, 2009']
regex = re.compile(r'([a-zA-Z]{3}) ([0-9]+), ([0-9]+)')
result = regex.search(listOfDates[0])
#regex = re.search("([a-z]{3}) (1-9+), (0-9+)", listOfDates[0])

print(result.group(1))
print(result.group(2))
print(result.group(3))

def order_dates(dates):
    for index, date in enumerate(dates):
        regex = re.compile(r'([a-zA-Z]{3}) ([0-9]+), ([0-9]+)')
        result = regex.search(date);
        print(index)

print(order_dates(listOfDates))
