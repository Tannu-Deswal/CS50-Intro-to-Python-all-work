from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
fonts = figlet.getFonts()
def main():
    try:
        inp = 'Hello'
        if len(sys.argv)==1:
            fin_font = random.choice(fonts)
            figlet.setFont(font = fin_font)
            print(figlet.renderText(inp))
        elif len(sys.argv)==3 and sys.argv[1] == '-f' and sys.argv[2] in fonts:
            figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(inp))
        else:
            sys.exit(1)
            print('Invalid usage')
    except Exception as e:
        print(f'Error: {e}')
        return
    
main()