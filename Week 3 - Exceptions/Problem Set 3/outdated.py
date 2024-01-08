months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Getting input until it's correct
while True:
    date = input("Date: ")

    # Number format
    if "/" in date:
        # Check if all are ints
        try:
            month, day, year = map(int, date.split("/"))
        except ValueError:
            continue

        if month > 12:
            continue
    # With month name
    else:
        month, day, year = date.split()

        if not "," in day:
            continue

        # Remove ","
        day = day.replace(",", "")

        # Change "year" and "day" to ints
        try:
            day, year = int(day), int(year)
        except ValueError:
            continue

        month = months.index(month) + 1

    if day > 31:
        continue

    print(f"{year}-{month:02}-{day:02}")
    break
