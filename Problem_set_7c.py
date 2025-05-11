#Working 9 to 5
import re

def main():
    try:
        inp = input('Hours: ').strip().lower()
        print(convert(inp))
    except ValueError:
        print('ValueError')
        
def convert(s):
    pattern = r'^(\d{1,2})(?::(\d{1,2}))? (am|pm) to (\d{1,2})(?::(\d{1,2}))? (am|pm)$'
    match = re.search(pattern, s)
    if not match:
        raise ValueError
        
    h1, m1, p1, h2, m2, p2 = match.groups()
    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    
    if h1>12 or h2>12 or m1>59 or m2>59:
        raise ValueError
        
    if p1 == 'pm' and h1 != 12:
        h1 += 12
    elif p1 == 'am' and h1 == 12:
        h1 = 0

    if p2 == 'pm' and h2 != 12:
        h2 += 12
    elif p2 == 'am' and h2 == 12:
        h2 = 0
        
    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

if __name__ == '__main__':
    main()