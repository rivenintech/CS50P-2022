import sys
from random import choice

from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

# Pick random font
if len(sys.argv) == 1:
    font = choice(fonts)
elif len(sys.argv) == 3:
    # Check if there is "font" flag
    if sys.argv[1] not in {"-f", "--font"}:
        sys.exit("Invalid usage")

    # Check if provided font is valid
    font = sys.argv[2]

    if font not in fonts:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

figlet.setFont(font=font)

# Ask for text and print it
text = input("Input: ")
print(f"Output:\n{figlet.renderText(text)}")
