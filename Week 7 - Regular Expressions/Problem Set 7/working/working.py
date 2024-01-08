import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d{1,2})(?:\:(\d{2}))? (AM|PM) to (\d{1,2})(?:\:(\d{2}))? (AM|PM)"

    if times := re.search(pattern, s):
        times = times.groups()  # returns: hour, minute, am/pm, hour, minute, am/pm

        # Get first and second time converted
        first = convert_to_24(times[0], times[1], times[2])
        second = convert_to_24(times[3], times[4], times[5])

        # Return converted time in one string
        return f"{first} to {second}"

    raise ValueError  # If no match


# Validate time and convert it
def convert_to_24(hour, minute, am_pm):
    # If minute is not provided assume it's 0
    minute = int(minute) if minute else 0
    hour = int(hour)

    # Validate hour and minute
    if not 1 <= hour <= 12:
        raise ValueError
    if not 0 <= minute <= 59:
        raise ValueError

    # Convert time
    if am_pm == "PM" and hour != 12:
        hour += 12

    elif am_pm == "AM" and hour == 12:
        hour = 0

    # Returns converted time with leading zeros
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
