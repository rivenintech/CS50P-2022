from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    inp_date = input("Date of Birth: ")

    if dt := get_datetime_obj(inp_date):
        print(minutes_as_words(dt))
    else:
        sys.exit("Invalid date")


# Check if date format is valid and return datetime object
def get_datetime_obj(inp_date):
    if dt := re.search(r"(\d{4})-(\d{2})-(\d{2})", inp_date):
        return date(int(dt.group(1)), int(dt.group(2)), int(dt.group(3)))
    else:
        return False


# Change date to minutes as words
def minutes_as_words(dt):
    # Convert to minutes
    minutes = (date.today() - dt).days * 24 * 60

    # Change minutes to words and capitalize the string
    num_to_words = p.number_to_words(minutes, andword="").capitalize()

    # Return string with word "minutes"
    return f"{num_to_words} minutes"


if __name__ == "__main__":
    main()
