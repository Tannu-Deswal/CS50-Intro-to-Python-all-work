#Back to the Bank
def main():
    greetings = input('Greetings: ')
    ans = value(greetings)
    print(ans)
def value(greet):
    if greet.lower().startswith('hello'):
        return '$0'
    elif greet.lower().startswith('h'):
        return '$20'
    else:
        return '$100'
if __name__ == '__main__':
    main()