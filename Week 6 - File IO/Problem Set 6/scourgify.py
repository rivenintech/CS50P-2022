import sys
import csv

# Validate command-line argument
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

rows = []

# Read file
try:
    with open(sys.argv[1]) as inp_file:
        reader = csv.DictReader(inp_file)

        # Loop through reader, split "name", and append them to list "rows"
        for row in reader:
            last, first = row["name"].split(", ")
            rows.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

# Write to file
with open(sys.argv[2], "w", newline="") as out_file:
    writer = csv.DictWriter(out_file, fieldnames=["first", "last", "house"])

    writer.writeheader()

    # loop through each row and write it to file
    for row in rows:
        writer.writerow(row)
