#Re-requesting a Vanity Plate
import string
def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def num_there(s):
    return any(i.isdigit() for i in s)

def is_valid(s):
    if not(2<=len(s)<=6):
        return False
    if not(s[:2].isalpha()):
        return False
    num_found = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0' and not num_found:
                return False
            num_found = True
        elif num_found:
            return False
    for char in s:
        if char in string.punctuation:
            return False
    return True
if __name__ == '__main__':
    main()