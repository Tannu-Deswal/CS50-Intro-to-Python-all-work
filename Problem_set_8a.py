#Seasons of Love
import inflect
p = inflect.engine()
import sys
from datetime import date, timedelta
def main():
    try:
        dob = parse_date(input('Date of Birth: ').strip())
        print(convert(dob))
    except Error as e:
        print(e)
        sys.exit(1)

def parse_date(dob_str):
    try:
        y, m, d = map(int, dob_str.split('-'))
        dob = date(y, m, d) 
        if dob>date.today():
            raise ValueError('Date of Birth cannot be in future.')
        return dob    
    except Exception:
        raise ValueError("Invalid date")
        
def convert(dob):
    delta = date.today()-dob
    minutes = delta.days*24*60
    min_word = p.number_to_words(minutes, andword = '')
    return f'{min_word.capitalize()} minutes'
    
if __name__ == '__main__':
    main()