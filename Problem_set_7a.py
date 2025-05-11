#NUMB3RS
import re
import sys

def main():
    print(validate(input('IPv4 Address: ')))
def validate(ip):
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    matches = re.search(pattern, ip)
    if matches:
        parts = ip.split('.')
        for part in parts:
            if not 0<=int(part)<=255:
                return False
        return True
    return False
    
if __name__ == '__main__':
    main()