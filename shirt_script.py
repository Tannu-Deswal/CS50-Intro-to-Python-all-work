#CS50 P-Shirt
import sys
import os
from PIL import Image, ImageOps
def main():
    try:
        if len(sys.argv)<3:
            print('Too few command-line arguments')
            sys.exit(1)
        elif len(sys.argv)>3:
            print('Too many command-line arguments')
            sys.exit(1)
        else:
            if sys.argv[1].lower().endswith(('.jpg', '.jpeg', '.png')) and sys.argv[2].lower().endswith(('.jpg', '.jpeg', '.png')):
                ext1 = os.path.splitext(sys.argv[1].lower())[1]
                ext2 = os.path.splitext(sys.argv[2].lower())[1]
                if ext1 == ext2:
                    shirt(sys.argv[1], sys.argv[2])
                else:
                    print('Input and output have different extensions')
                    sys.exit(1)
            else:
                print('Invalid input')
                sys.exit(1)
    except:
        sys.exit(1)
def shirt(before, after):
    try:
        before_img = Image.open(before)
        shirt_img = Image.open('shirt.png')
        before_img = ImageOps.fit(before_img, shirt_img.size)
        before_img.paste(shirt_img, shirt_img)
        return before_img.save(after)
    except FileNotFoundError:
        print('Input does not exist')
        return None
if __name__ == '__main__':
    main()