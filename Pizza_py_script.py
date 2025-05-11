#Pizza Py
import sys
import csv
from tabulate import tabulate
def main():
    try:
        if len(sys.argv)<2:
            print('Too few command-line arguments')
            sys.exit(1)
        elif len(sys.argv)>2:
            print('Too many command-line arguments')
            sys.exit(1)
        else:
            if sys.argv[1].endswith('.csv'):
                table = pinocchio(sys.argv[1])
                print(table)
            else:
                print('Not a CSV file')
    except:
        sys.exit(1)
def pinocchio(file):
    try:
        with open(file) as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return tabulate(data, headers = 'keys', tablefmt = 'grid')
    except FileNotFoundError:
        print('File does not exist')
        return None
if __name__ == '__main__':
    main()