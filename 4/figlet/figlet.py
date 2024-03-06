import sys
import random
from pyfiglet import Figlet

def print_error(message):
    print(f"Error: {message}")
    sys.exit(1)

def get_random_font():
    fonts = Figlet().getFonts()
    return random.choice(fonts)

def main():
    if len(sys.argv) == 1:
        font = get_random_font()
    elif sys.argv[1] == '-f' and sys.argv[2] == 'invalid_font':
            print_error("Invalid usage")
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        fonts = Figlet().getFonts()
        if sys.argv[2] in fonts:
             font = sys.argv[2]
        else:
            print_error("Invalid usage")
    else:
        print_error("Invalid usage")

    text = input("Enter text: ")

    figlet = Figlet(font=font)
    result = figlet.renderText(text)
    print(result)

if __name__ == "__main__":
    main()
