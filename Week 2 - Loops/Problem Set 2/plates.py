def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if plate is between 2 and 6 in length
    if not 2 <= len(s) <= 6:
        return False

    # Check if there are no digits in the first two positions
    if not s[0:2].isalpha():
        return False

    # Check if there are no periods, spaces, or punctuation marks
    if not s.isalnum():
        return False

    # Get index of the first digit
    for i, char in enumerate(s):
        if char.isdigit():
            # If first character is 0 - invalid
            if char == "0":
                return False

            # If there is a letter after digits - invalid
            if not s[i:].isdigit():
                return False

            break

    return True


main()
