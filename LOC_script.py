#Lines of Code
import sys
def main():
    try:
        if len(sys.argv)<2:
            print('Too few command-line arguments')
            sys.exit(1)
        elif len(sys.argv)>2:
            print('Too many command-line arguments')
            sys.exit(1)
        else:
            if sys.argv[1].endswith('.py'):
                lines = count_lines(sys.argv[1])
                print(lines)
            else:
                print('Not a Python file')
    except:
        sys.exit(1)
def count_lines(file):
    try:
        with open(file) as file:
            lines = file.readlines()
            return sum(1 for line in lines if line.lstrip() and not line.lstrip().startswith('#'))
    except FileNotFoundError:
        print('File does not exist')
        return None
if __name__ == '__main__':
    main()