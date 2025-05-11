#Refueling
def main():
    try:
        frac = input('Fraction: ').strip()
        fuel = convert(frac)
        output = gauge(fuel)
        print(output)
    except (ValueError, ZeroDivisionError):
        main() 

def convert(frac):
    x, y = frac.split('/')
    x, y = int(x), int(y)
    if y == 0 or x > y:
        raise ValueError
    return x / y

def gauge(fuel):
    perc = fuel * 100
    if perc >= 99:
        return 'F'
    elif perc <= 1:
        return 'E'
    else:
        return f'{round(perc)}%'

if __name__ == "__main__":
    main()