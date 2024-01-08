import sys
import csv
from tabulate import tabulate

# Validate command-line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    # Open file and create list from reader
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        table = list(reader)
except FileNotFoundError:
    sys.exit("File does not exist")

# Create ASCII table
print(tabulate(table[1:], table[0], tablefmt="grid"))
