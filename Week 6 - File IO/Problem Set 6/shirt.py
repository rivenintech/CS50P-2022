import sys
from os.path import splitext

from PIL import Image, ImageOps

ext = {".jpg", ".jpeg", ".png"}

# Validate command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif splitext(sys.argv[1])[1] not in ext:
    sys.exit("Invalid input")
elif splitext(sys.argv[2])[1] not in ext:
    sys.exit("Invalid output")
elif splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
    sys.exit("Input and output have different extensions")

# Open input file
try:
    input_img = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")  # Open "shirt.png" file
img = ImageOps.fit(input_img, shirt.size)  # Resize input image
img.paste(shirt, shirt)  # Paste shirt on input image
img.save(sys.argv[2])  # Save output image
