#Testing my twttr
def main():
    inp = input('Input: ')
    out = shorten(inp)
    print(out)
def shorten(inp):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    result = ''
    for i in range(len(inp)):
        if inp[i] not in vowels:
            result = result+inp[i]
    return result
if __name__ == '__main__':
    main()