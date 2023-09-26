from sys import argv
from date import check_date

if __name__ == '__main__':
    date = argv[1]
    print(check_date(date))