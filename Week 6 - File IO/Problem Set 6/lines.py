import sys

lines = 0

# Validate command-line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    # Open file, read it line by line, and check if it's not a comment/blank line
    with open(sys.argv[1]) as file:
        for line in file:
            if not line.isspace() and not line.lstrip().startswith("#"):
                lines += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(lines)
