#Scourgify
import sys
import csv
def main():
    try:
        if len(sys.argv)<3:
            print('Too few command-line arguments')
            sys.exit(1)
        elif len(sys.argv)>3:
            print('Too many command-line arguments')
            sys.exit(1)
        else:
            if sys.argv[1].endswith('.csv') and sys.argv[2].endswith('csv'):
                scourgify(sys.argv[1], sys.argv[2])
            else:
                print('Not a CSV file')
    except:
        sys.exit(1)
def scourgify(before, after):
    try:
        with open(before) as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                last, first = row['name'].strip().split(',')
                data.append({'first_name': first, 'last_name': last, 'house': row['house']})
        with open(after, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = ['first_name', 'last_name', 'house'])
            writer.writeheader()
            writer.writerows(data)
            return file
    except FileNotFoundError:
        print(f'Could not read {before}')
        return None
if __name__ == '__main__':
    main()